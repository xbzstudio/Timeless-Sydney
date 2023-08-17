from typing import Union, Any, AsyncGenerator
from fastapi import FastAPI, WebSocket, Request, Response
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from EdgeGPT import EdgeGPT as gpt
from EdgeGPT.ImageGen import ImageGenAsync
import uvicorn
import json, asyncio
from pydantic import BaseModel

with open('./config/server.json', 'r', encoding="utf-8") as f: #获取服务端配置
    config = json.loads(f.read())

'''
服务端配置如下：
port：端口
host：0.0.0.0或127.0.0.1
useUserCookie：是否需要用户在网页客户端使用自己的cookie登录，如果为假，默认使用服务端设置的cookie.json
tips：每个键是一个人格的名称，键的值是对应的咒语，网页客户端可以使用指令切换人格
'''

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

class DrawTip(BaseModel):
    tip : str = "a cat"
    cookie : str = None

@app.get('/') #返回web客户端
async def Index() -> Response:
    return Response(open(f'./index.html', 'r', encoding="utf-8").read())

@app.get('/static/{filepath}') #返回静态文件
async def getFile(filepath : str) -> Response:
    if filepath[-4::] == '.jpg' or filepath[-4::] == '.png':
        return Response(open(f'./static/{filepath}', 'rb').read())
    else:
        return Response(open(f'./static/{filepath}', 'r', encoding="utf-8").read())


@app.websocket('/chat/ws') #返回bing的回答
async def wsStream(ws: WebSocket):
    """
    客户端发送格式:
    {
    "tipName" : 人格名称,
    "question" : 问题,
    "style" : 聊天风格,
    }
    """
    await ws.accept()
    if config.get('useUserCookie'):
        msg = await ws.receive_text()
        chatbot = await gpt.Chatbot.create(cookies = json.loads(msg))
    else:
        chatbot = await gpt.Chatbot.create(cookies = json.loads(open('./config/cookie.json', 'r', encoding='utf-8').read()))
    while True:
        try:
            msg = await ws.receive_json() #接收信息
            response = {  #向客户端发送的信息格式
                "answer" : "",
                "error" : "",
                "urls" : [],
                "done" : False,
                "suggested" : []
            }
            imageInfo = None
            async for final, ans in chatbot.ask_stream(
                prompt = msg.get('question'),
                conversation_style = msg.get('style'), 
                webpage_context = config.get('tips').get(msg.get('tipName')) if msg.get('tipName') in config.get('tips') else msg.get('tipName')):

                if not final:
                    response['answer'] = ans
                    imageInfo = ans
                    await ws.send_text(json.dumps(response))
                else:
                    response['done'] = True
                    if ans.get('item').get('result').get('value') == 'Throttled':
                        response['error'] = '已到达一天的最大聊天次数，无法继续聊天'
                        await ws.send_text(json.dumps(response))
                    if ans.get('item').get('result').get('value') == 'Success':
                        response['answer'] = ans['item']['messages'][-1]['adaptiveCards'][0]['body'][0]['text']
                        response['suggested'] = [i['text'] for i in ans['item']['messages'][-1]['suggestedResponses']]            
                        response['urls'] = [{'name' : i['providerDisplayName'], 'url' : i['seeMoreUrl']} for i in ans['item']['messages'][-1]['sourceAttributions']]
                        await ws.send_text(json.dumps(response))
                    else:
                        response['error'] = '未知错误，value：' + str(ans.get('item').get('result').get('value'))
                        await ws.send_text(json.dumps(response))
        except Exception as e:
            if e.args[0] == "adaptiveCards":
                response['answer'] = imageInfo
                response['done'] = True
                await ws.send_text(json.dumps(response))
            else:
                response['done'] = True
                response['error'] = '未知错误，服务端报错：' + str(e)
                await ws.send_text(json.dumps(response))
                print('Error:', e.args)

@app.post('/chat/image') #单独返回画图信息
async def aiDraw(drawTip : DrawTip) -> Response:
    '''
    返回格式：
    {
        "answer" : 回答,
        "error" : 错误
    }
    '''
    res = {
        "answer" : None,
        "error" : None
    }
    try:
        if config.get('useUserCookie'):
            cookie = drawTip.cookie
        else:
            cookie = json.loads(open('./config/cookie.json', 'r', encoding = 'utf-8').read())
        async with ImageGenAsync(all_cookies = cookie) as creator:
            images = await creator.get_images(drawTip.tip)
            res['answer'] = images
        return Response(json.dumps(res))
    except Exception as e:
        res['error'] = '未知错误，服务端报错：' + str(e)
        return Response(json.dumps(res))
    
@app.get('/chat/getTipNames') #获取人格名称列表
async def tipnames() -> Response:
    lst = [i for i in config.get('tips')]
    lst = [lst, config.get('useUserCookie')]
    return Response(json.dumps(lst))

@app.get('/config/{filepath}') #获取web客户端默认配置
async def clientjs(filepath) ->Response:
    if filepath == 'client.js':
        return Response(open('./config/client.js', 'r', encoding= 'utf-8').read())
    else:
        return Response('不允许查看该文件',  status_code = 404)

if __name__ == '__main__':
    print('Server Start')
    print('Go to http://127.0.0.1:' + str(config.get('port')) + "/ and start to chat!")
    uvicorn.run(app, host = config['host'], port = config['port']) #__，启动！
