# BingAI-Client

BingAI-Client是一个基于[AngularJS](https://angular.cn/)和的New Bing web客户端，只要您在本地完成New Bing的部署并运行服务端程序，或连接到一个部署了BingAI-Client并开启了服务端程序的服务器，即可开始使用BingAI-Client。

部署前，确保你拥有 `Python` 的稳定高版本（推荐3.10），一个 `VPN` ，还有一个可以使用New Bing的 `Microsoft账号` 。

相关链接：  
Python 3.10.10下载：[https://www.python.org/downloads/release/python-31010/](https://www.python.org/downloads/release/python-31010/)  
Geph迷雾通下载：[https://f001.backblazeb2.com/file/geph4-dl/geph-releases/windows-stable/4.7.10/geph-windows-setup.exe](https://f001.backblazeb2.com/file/geph4-dl/geph-releases/windows-stable/4.7.10/geph-windows-setup.exe)

## 1，安装并部署BingAI-Client

首先确保你有高版本的Python（推荐3.10），这里不过多赘述。

首先下载本项目的ZIP压缩包，解压。

然后到浏览器中安装插件[Cookie Editor](https://microsoftedge.microsoft.com/addons/detail/cookie-editor/ajfboaconbpkglpfanbmlfgojgndmhmc)。

安装完成后，打开你的VPN，来到[New Bing官方网站](https://bing.com/new)，进入和bing聊天的界面。然后点开Cookie Editor，按下图片中的按钮：

![image](https://user-images.githubusercontent.com/119436353/235375933-d7e81988-fc6b-423b-841f-98575d310e32.png)

然后就可以了。按完之后，打开项目文件夹，打开根目录下的`cookie.json`，ctrl+v把刚才复制到的东西黏贴进去，保存文件，然后退出。

按下 `win + r` 会弹出一个窗口，在文本框中输入cmd，然后回车，就会进入终端。在终端中，依次输入这几个命令并回车：

```
pip install fastapi
pip install python-multipart
pip install uvicorn
pip install EdgeGPT
pip install BingImageCreator
```

过程可能会有点长。第三方包全部安装完毕后，在项目文件根目录中打开终端，然后输入命令 `python ./BingServer.py` ，如果没有报错，那就说明成功了。

如果报错，请将EdgeGPT升级至最新版本：

```
pip install --upgrade EdgeGPT
```

接下来，程序会询问你是否允许别的主机连接（即开放给别的主机使用New Bing），如果选择true，你就可以使用你的公网ip、内网ip、回环地址和打开本地文件来访问BingAI-Client客户端；如果选择false，就只能用回环地址和打开本地文件夹来访问BingAI-Client客户端。

如果您选择打开本地文件以外的方法使用BingAI-Clint客户端，就要在ip后加上/webui。

另外，请使用http协议访问。暂不支持https。

询问完是否开放给别的主机后，程序还会询问你部署至的端口。可以自行填写，保证不与别的程序冲突即可。如果不填写80（默认端口），在使用打开本地文件以外的方法访问时，需要在ip或域名后加端口号（ip/域名 + :端口号）。

到这里，你就成功地部署在本地的New Bing。接下来，打开项目根目录下的"index.html"，或在浏览器中访问`127.0.0.1:端口号/webui`就可以开始使用该客户端了！

记得在使用客户端的全过程中不要关闭终端。BingServer的连接十分稳定，请放心。

如果您有特殊需求，可以访问[BingAI-Client在线版](https://xbzstudio.github.io/BingAI-Client/) 。但是架在这个Github Pages上的客户端的默认设置不能被你所更改，而且还是需要你自己运行服务端程序。如果你既想使用自己的默认设置，又想用别的服务器请求New Bing的响应，可以将BingAI-Client架在你的服务器上，使用在本地默认设置中将HOST设为你要连接到的服务器公网ip+端口，然后打开本地index.html文件，即可依赖你的服务器与New Bing对话，并且不用在本地开启BingServer.py（服务器开启即可）。如果想在网站上用自己的默认设置与New Bing对话，可以在你的服务器中自行将默认设置设置为你想要的，然后使用你的服务器的`公网ip/域名+端口/webui`访问你的定制版在线BingAI-Client，也是不用在本地开启BingServer.py（服务器开启即可）。

## 2，配置New Bing

### 默认聊天设置更改

进入./src/js文件夹后，就可以看到一个名为“setting.js”的文件。打开这个文件，里面储存着一段代码，默认是这样：

```javascript
var setting = {

    HOST:'127.0.0.1', //你要连接到的服务器IP或域名，如果BingAI服务器端口不为80，请在后面加上":端口值"。默认为127.0.0.1，即为访问本地服务器。
    autoTranslate:true, //是否默认启用自动翻译，true为是，false为否
    tokenToServer:true, //是否默认启用连续对话，true为是，false为否
    chatStyle:"creative", //与Bing AI聊天时选用的聊天风格，balanced代表平衡，creative代表创造力，precise代表精确性
    tips:"", //在新的主题开始时的第一条对话前插入的提示，null和空的英文双引号（""）表示没有。
    fontColor:"white", //你和Bing AI在消息框中的消息字体颜色
    nameColor:"#dadada", //你和Bing AI显示名字的颜色
    backgroundUrl:"./src/images/Background.jpg" //背景图片的url地址，默认为项目文件中的Background.jpg

};
```

接下来你只要根据这段代码的中文注释来更改配置即可更改你的默认设置。
在更改你的默认设置后，打开本地客户端时，你的聊天设置会更改为默认设置中的那样。例如你在默认设置中表示你想要让chatStyle更改为"balanced"，那么在打开本地客户端时，聊天设置中的聊天风格设置将会自动更改为balanced。

### 头像更改

进入./src/images文件夹，里面有两张图片，一个是`User.png`，一个是`Bing.png`，如果你想要更换你自己或New Bing的头像的话，就在这个文件夹中加入你想要更换的图片，并把它重命名为"User.png"或"Bing.png"。

# 结尾

## 鸣谢：

[Bing-Chat](https://github.com/XiaoXinYo/Bing-Chat)的开发者[XiaoXinYo](https://github.com/XiaoXinYo)  
本项目的[BingServer.py](https://github.com/xbzstudio/BingAI-Client/blob/main/BingServer.py)就是他开发的！  
（当然本人也在当中增加了许些功能！）
