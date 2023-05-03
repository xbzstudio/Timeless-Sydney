# BingAI-Client

BingAI-Client是一个基于[AngularJS](https://angular.cn/)的New Bing web客户端，只要您在本地完成New Bing的部署并运行服务端程序，即可开始使用BingAI-Client。

使用前，确保你拥有 `Python` 的稳定高版本（推荐3.10），一个 `VPN` ，还有一个可以使用New Bing的 `Microsoft账号` 。

相关链接：  
Python 3.10.10下载：[https://www.python.org/downloads/release/python-31010/](https://www.python.org/downloads/release/python-31010/)  
Geph迷雾通下载：[https://f001.backblazeb2.com/file/geph4-dl/geph-releases/windows-stable/4.7.10/geph-windows-setup.exe](https://f001.backblazeb2.com/file/geph4-dl/geph-releases/windows-stable/4.7.10/geph-windows-setup.exe)

## 1，安装BingAI-Client

首先确保你有高版本的Python（推荐3.10），这里不过多赘述。

首先下载本项目的ZIP压缩包，解压。

然后到浏览器中安装插件[Cookie Editor](https://microsoftedge.microsoft.com/addons/detail/cookie-editor/ajfboaconbpkglpfanbmlfgojgndmhmc)。

安装完成后，打开你的VPN，来到[New Bing官方网站](https://bing.com/new)，进入和bing聊天的界面。然后点开Cookie Editor，按下图片中的按钮：

![image](https://user-images.githubusercontent.com/119436353/235375933-d7e81988-fc6b-423b-841f-98575d310e32.png)

然后就可以了。按完之后，打开项目文件夹，打开BingAiServer文件夹底下的cookie.json，ctrl+v把刚才复制到的东西黏贴进去，保存文件，然后退出。

按下 `win + r` 会弹出一个窗口，在文本框中输入cmd，然后回车，就会进入终端。在终端中，依次输入这几个命令并回车：

```
pip install fastapi
pip install python-multipart
pip install uvicorn
pip install EdgeGPT
pip install BingImageCreator
```

过程可能会有点长。第三方包全部安装完毕后，在项目文件根目录中打开终端，然后输入命令 `python ./BingServer.py` ，如果没有报错，那就说明成功了。

<img width="586" alt="image" src="https://user-images.githubusercontent.com/119436353/235376222-16e7939b-7f6e-4c05-858f-46ec37ff3de5.png">

到这里，你就成功地部署在本地的New Bing。接下来，打开项目根目录下的"index.html"，就可以开始使用该客户端了！

记得在使用客户端的全过程中不要关闭终端。BingServer的连接十分稳定，请放心。

如果您有特殊需求，可以访问[BingAI-Client在线版](https://xbzstudio.github.io/BingAI-Client/) 。但是架在这个网站上的客户端的默认设置不能被你所更改，如果你既想要更改默认设置，又想在网站上使用到此客户端，可以将客户端部署到你的服务器（或Github Pages等）上，然后更改在服务器中BingAI-Client的默认设置。

## 2，配置New Bing

### 默认聊天设置更改

进入./src/js文件夹后，就可以看到一个名为“setting.js”的文件。打开这个文件，里面储存着一段代码，默认是这样：

```javascript
var setting = {

    autoTranslate:true, //是否默认启用自动翻译，true为是，false为否
    tokenToServer:true, //是否默认启用连续对话，true为是，false为否
    chatStyle:"creative", //与Bing AI聊天时选用的聊天风格，balanced代表平衡，creative代表创造力，precise代表精确性
    tips:"", //在新的主题开始时的第一条对话前插入的提示，null和空的英文双引号（""）表示没有。
    fontColor:"white", //你和Bing AI在消息框中的消息字体颜色
    nameColor:"#dadada", //你和Bing AI显示名字的颜色

};
```

接下来你只要根据这段代码的中文注释来更改配置即可更改你的默认设置。
在更改你的默认设置后，打开本地客户端时，你的聊天设置会更改为默认设置中的那样。例如你在默认设置中表示你想要让chatStyle更改为"balanced"，那么在打开本地客户端时，聊天设置中的chatStyle将会自动更改为balanced。

### 头像更改

进入./src/images文件夹，里面有两张图片，一个是`User.png`，一个是`Bing.png`，如果你想要更换你自己或New Bing的头像的话，就在这个文件夹中加入你想要更换的图片，并把它重命名为"User.png"或"Bing.png"。

# 结尾

## 鸣谢：

[Bing-Chat](https://github.com/XiaoXinYo/Bing-Chat)的开发者[XiaoXinYo](https://github.com/XiaoXinYo)  
本项目的[BingServer.py](https://github.com/xbzstudio/BingAI-Client/blob/main/BingAiSever/BingServer.py)就是他开发的！

## 链接：

[百度贴吧更新/闲聊/疑难解答帖](https://tieba.baidu.com/p/8388703977)  
