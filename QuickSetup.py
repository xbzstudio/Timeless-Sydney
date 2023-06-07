import json

print("---QuickSetup---")
print('''1.服务端设置
2.客户端设置''')
i=int(input("请输入选项:"))
match i:
    case 1:
        print("---QuickSetup---")
        print('''1.cookie设置
2.设置服务端是否对外开放
3.设置服务器端口''')
        i=int(input("请输入选项:"))
        match i:
            case 1:
                with open("./config/cookie.json",'w', encoding="utf8") as cf:
                    cf.write(input("请粘贴您的cookie:"))
                print("OK")
            case 2:
                print("---QuickSetup---")
                print("1.开放\n\
2.不开放")
                i=input("请输入选项:")
                with open("./config/server.json",'r', encoding="utf8") as cf:
                    yuan=json.load(cf)
                with open("./config/server.json",'w', encoding="utf8") as cf:
                    if i=='1':
                        yuan["AllowConnect"]=True
                        cf.write(json.dumps(yuan))
                    elif i=='2':
                        yuan["AllowConnect"]=False
                        cf.write(json.dumps(yuan))
                print('OK')
            case 3:
                print("---QuickSetup---")
                i=input("请输入端口:")
                with open("./config/server.json",'r', encoding="utf8") as cf:
                    yuan=json.load(cf)
                with open("./config/server.json",'w', encoding="utf8") as cf:
                    yuan["Port"]=int(i)
                    cf.write(json.dumps(yuan))
                
                print('OK')
    case 2:
        HOST="127.0.0.1:80"
        autoTranslate="true"
        tokenToServer="true"
        autoScroll="true"
        chatMoreTimes="true"
        HTTPSMODE="false"
        chatStyle="creative"
        tips=""
        fontColor="white"
        nameColor="#dadada"
        backgroundUrl="./images/Background.jpg"
        saveChatTimes="20"
        
        print("---QuickSetup---")
        print('''1.设置你要连接到的服务器IP或域名
2.是否默认启用自动翻译
3.是否默认启用连续对话
4.是否在Bing回复送达后自动滚动至页面底部
5.是否自动突破20条对话限制
6.是否开启HTTPS模式
7.设置与Bing AI聊天时选用的聊天风格
8.设置在新的主题开始时的第一条对话前插入的提示
9.你和Bing AI在消息框中的消息字体颜色
10.你和Bing AI显示名字的颜色
11.背景图片的url地址
12.最大保存聊天记录数量(不太有用)''')
        i=int(input("请输入选项:"))
        match i:
            case 1:
                print("---QuickSetup---")
                i=input("请输入地址(域名/ip:端口):")
                HOST=i
            case 2:
                print("---QuickSetup---")
                i=input("请输入true/false:")
                autoTranslate=i.lower()
            case 3:
                print("---QuickSetup---")
                i=input("请输入true/false:")
                tokenToServer=i.lower()
            case 4:
                print("---QuickSetup---")
                i=input("请输入true/false:")
                autoScroll=i.lower()
            case 5:
                print("---QuickSetup---")
                i=input("请输入true/false:")
                chatMoreTimes=i.lower()
            case 6:
                print("---QuickSetup---")
                i=input("请输入true/false:")
                HTTPSMODE=i.lower()
            case 7:
                print("---QuickSetup---")
                i=input("请输入balanced(平衡)/creative(创造力)/precise(精确):")
                chatMoreTimes=i
            case 8:
                print("---QuickSetup---")
                i=input("请输入提示词:")
                tips=i
            case 9:
                print("---QuickSetup---")
                i=input("请输入颜色色号:")
                fontColor=i
            case 10:
                print("---QuickSetup---")
                i=input("请输入颜色色号:")
                nameColor=i
            case 11:
                print("---QuickSetup---")
                i=input("请输入图片的url地址(可以是本地地址):")
                backgroundUrl=i
            case 12:
                print("---QuickSetup---")
                i=input("请输入最大保存聊天记录数量:")
                saveChatTimes=i
        a=f'''var setting = {{

    HOST:'{HOST}', //你要连接到的服务器IP或域名，如果BingAI服务器端口不为80，请在后面加上":端口值"。默认为127.0.0.1，即为访问本地服务器。
    autoTranslate:{autoTranslate}, //是否默认启用自动翻译，true为是，false为否
    tokenToServer:{tokenToServer}, //是否默认启用连续对话，true为是，false为否
    autoScroll:{autoScroll}, //是否在Bing回复送达后自动滚动至页面底部，true为是，false为否
    chatMoreTimes:{chatMoreTimes}, //是否自动突破20条对话限制，true为是，false为否
    HTTPSMODE:{HTTPSMODE}, //是否开启HTTPS模式，true为是，false为否。如果开启，将会把协议更改为https和wss。
    chatStyle:"{chatMoreTimes}", //与Bing AI聊天时选用的聊天风格，balanced代表平衡，creative代表创造力，precise代表精确性
    tips:"{tips}", //在新的主题开始时的第一条对话前插入的提示，null和空的英文双引号（""）表示没有。
    fontColor:"{fontColor}", //你和Bing AI在消息框中的消息字体颜色
    nameColor:"{nameColor}", //你和Bing AI显示名字的颜色
    backgroundUrl:"{backgroundUrl}", //背景图片的url地址，默认为项目文件中的Background.jpg
    saveChatTimes:{saveChatTimes} //最大保存聊天记录数量
    
}};'''
        with open("./static/js/setting.js",'w', encoding="utf8") as cf:
            cf.write(a)
        print("OK")