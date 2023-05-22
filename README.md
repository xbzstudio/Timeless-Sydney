<h1 align="center">BingAI-Client</h1>

<p align="center">
<a href="https://github.com/xbzstudio/BingAI-Client/blob/main/LICENSE"><img src="https://img.shields.io/badge/LICENSE-MIT-green"></a><img src="https://img.shields.io/badge/Language-Python-blue"><img src="https://img.shields.io/badge/Language-Javascript-yellow"><a href="https://github.com/xbzstudio"><img src="https://img.shields.io/badge/Github-xbzstudio-red"></a><a href="https://github.com/XiaBeiZe-Studio2022"><img src="https://img.shields.io/badge/Studio-%E4%B8%8B%E5%8C%97%E6%B3%BD%E5%B7%A5%E4%BD%9C%E5%AE%A4-red"></a>
</p>

# 介绍

BingAI-Client提供了Microsoft New Bing的web客户端和服务端。客户端基于[Angular](https://angular.cn/)，服务端基于[FastAPI](https://fastapi.tiangolo.com/zh/)和[EdgeGPT](https://github.com/acheong08/EdgeGPT)。在本地部署好New Bing后，运行服务端程序即可开始使用客户端。如果有需要，也可以在服务器上部署New Bing，并在本地连接到服务器的New Bing。服务端将会自动将Bing切换至Sydney模式以解除麻烦的限制。

# 开始

<details>
  <summary>

## 视频教程（在旧版上演示，仅作参考）

 </summary>
     
(因为github的文件大小限制,所以才会这么模糊,请见谅!如果想看高清的视频看[这个](https://v.superbed.cn/play/6460ccc70d2dde5777223e9c)):


https://github.com/viopsa233/BingAI-Client/assets/118115208/dea14d0a-7c05-4938-8b4a-0228ef04916b


</details>

<details>
  <summary>


## 图文教程
</summary>
  
部署前，确保你拥有 `Python` 的稳定高版本（推荐3.10），一个 `VPN` ，还有一个可以使用New Bing的 `Microsoft账号` 。

相关链接：  
Python 3.10.10下载：[https://www.python.org/downloads/release/python-31010/](https://www.python.org/downloads/release/python-31010/)  
Geph迷雾通下载：[https://f001.backblazeb2.com/file/geph4-dl/geph-releases/windows-stable/4.7.10/geph-windows-setup.exe](https://f001.backblazeb2.com/file/geph4-dl/geph-releases/windows-stable/4.7.10/geph-windows-setup.exe)


# 自动部署



首先确保你有高版本的Python（推荐3.10），这里不过多赘述。

首先下载本项目的ZIP压缩包，解压。

然后到浏览器中安装插件[Cookie Editor](https://microsoftedge.microsoft.com/addons/detail/cookie-editor/ajfboaconbpkglpfanbmlfgojgndmhmc)。

安装完成后，打开你的VPN，来到[Microsoft New Bing](https://bing.com/new)，进入和New Bing聊天的界面。然后点开Cookie Editor，按下图片中的按钮：

![image](https://user-images.githubusercontent.com/119436353/235375933-d7e81988-fc6b-423b-841f-98575d310e32.png)

然后就可以了。按完之后，打开项目文件夹，打开根目录下的`cookie.json`，按下ctrl+v把刚才复制到的东西黏贴进去，保存文件，然后退出。

### 运行Run文件夹下的`Install Libs.bat`。

在把Install Libs运行完毕后，在您第二次使用BingAI-Client时就不用再运行一次Install Libs了。

然后，运行Run文件夹下的`Run.bat`。

接下来，程序会询问你是否允许别的主机连接（即开放给别的主机使用New Bing），如果选择true，你就可以使用你的公网ip、内网ip、回环地址和打开本地文件来访问BingAI-Client客户端；如果选择false，就只能用回环地址和打开本地文件来访问BingAI-Client客户端。如果您选择打开本地文件以外的方法使用BingAI-Clint客户端，就要在ip后加上/webui。

如果报错了，就运行Run文件夹下的`Update Libs.bat`后，再试一次。

询问完是否开放给别的主机后，程序还会询问你部署至的端口。可以自行填写，保证不与别的程序冲突即可。如果不填写80（默认端口），在使用打开本地文件以外的方法访问时，需要在ip或域名后加端口号（ip/域名 + :端口号）。

到这里，你就成功地部署在本地的New Bing。接下来，打开项目根目录下的"index.html"，或在浏览器中访问`127.0.0.1:端口号/webui`就可以开始使用该客户端了！

记得在使用客户端的全过程中不要关闭终端。BingServer的连接十分稳定，请放心。

如果您有特殊需求，可以访问[BingAI-Client在线版](https://xbzstudio.github.io/BingAI-Client/) 。但是架在这个Github Pages上的客户端的默认设置不能被你所更改，而且还是需要你自己运行服务端程序。如果你既想使用自己的默认设置，又想用别的服务器请求New Bing的响应，可以将BingAI-Client架在你的服务器上，使用在本地默认设置中将HOST设为你要连接到的服务器公网ip+端口，然后打开本地index.html文件，即可依赖你的服务器与New Bing对话，并且不用在本地开启BingServer.py（服务器开启即可），并使用自己的默认设置。如果想在网站上用自己的默认设置与New Bing对话，可以在你的服务器中自行将默认设置设置为你想要的，然后使用你的服务器的`公网ip/域名+端口/webui`访问你的定制版在线BingAI-Client，也是不用在本地开启BingServer.py（服务器开启即可）。

# 手动部署

## 1，安装并部署BingAI-Client

首先确保你有高版本的Python（推荐3.10），这里不过多赘述。

首先下载本项目的ZIP压缩包，解压。

然后到浏览器中安装插件[Cookie Editor](https://microsoftedge.microsoft.com/addons/detail/cookie-editor/ajfboaconbpkglpfanbmlfgojgndmhmc)。

安装完成后，打开你的VPN，来到[Microsoft New Bing](https://bing.com/new)，进入和New Bing聊天的界面。然后点开Cookie Editor，按下图片中的按钮：

![image](https://user-images.githubusercontent.com/119436353/235375933-d7e81988-fc6b-423b-841f-98575d310e32.png)

然后就可以了。按完之后，打开项目文件夹，打开根目录下的`cookie.json`，按下ctrl+v把刚才复制到的东西黏贴进去，保存文件，然后退出。

用文件资源管理器打开项目文件夹，然后右键文件资源管理器空白的地方，点击“在终端里打开”，然后在Power Shell里输入以下命令并回车：
```
pip install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```

如果没有“在终端里打开”，请按下`win + r`组合键，弹出运行窗口，在文本框中输入cmd并回车。就会弹出终端。然后在终端中输入以下命令并回车：

```
cd /d 你的项目文件夹的绝对路径（如C:\Users\33664\OneDrive\XBZ-BingClient）
pip install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```

过程可能会有点长。第三方包全部安装完毕后，在项目文件根目录中打开终端，然后输入命令 `python ./BingServer.py` ，如果没有报错，那就说明成功了。

如果报错，请将EdgeGPT升级至最新版本。

```
pip install --upgrade EdgeGPT
```

接下来，程序会询问你是否允许别的主机连接（即开放给别的主机使用New Bing），如果选择true，你就可以使用你的公网ip、内网ip、回环地址和打开本地文件来访问BingAI-Client客户端；如果选择false，就只能用回环地址和打开本地文件来访问BingAI-Client客户端。如果您选择打开本地文件以外的方法使用BingAI-Clint客户端，就要在ip后加上/webui。

询问完是否开放给别的主机后，程序还会询问你部署至的端口。可以自行填写，保证不与别的程序冲突即可。如果不填写80（默认端口），在使用打开本地文件以外的方法访问时，需要在ip或域名后加端口号（ip/域名 + :端口号）。

到这里，你就成功地部署在本地的New Bing。接下来，打开项目根目录下的"index.html"，或在浏览器中访问`127.0.0.1:端口号/webui`就可以开始使用该客户端了！

记得在使用客户端的全过程中不要关闭终端。BingServer的连接十分稳定，请放心。

如果您有特殊需求，可以访问[BingAI-Client在线版](https://xbzstudio.github.io/BingAI-Client/) 。但是架在这个Github Pages上的客户端的默认设置不能被你所更改，而且还是需要你自己运行服务端程序。如果你既想使用自己的默认设置，又想用别的服务器请求New Bing的响应，可以将BingAI-Client架在你的服务器上，使用在本地默认设置中将HOST设为你要连接到的服务器公网ip+端口，然后打开本地index.html文件，即可依赖你的服务器与New Bing对话，并且不用在本地开启BingServer.py（服务器开启即可），并使用自己的默认设置。如果想在网站上用自己的默认设置与New Bing对话，可以在你的服务器中自行将默认设置设置为你想要的，然后使用你的服务器的`公网ip/域名+端口/webui`访问你的定制版在线BingAI-Client，也是不用在本地开启BingServer.py（服务器开启即可）。

</details>

# 配置New Bing

## 默认聊天设置更改

进入./src/js文件夹后，就可以看到一个名为“setting.js”的文件。打开这个文件，里面储存着一段代码，默认是这样：

```javascript
var setting = {

    HOST:'127.0.0.1', //你要连接到的服务器IP或域名，如果BingAI服务器端口不为80，请在后面加上":端口值"。默认为127.0.0.1，即为访问本地服务器。
    autoTranslate:true, //是否默认启用自动翻译，true为是，false为否
    tokenToServer:true, //是否默认启用连续对话，true为是，false为否
    autoScroll:true, //是否在Bing回复送达后自动滚动至页面底部，true为是，false为否
    chatMoreTimes:true, //是否自动突破20条对话限制，true为是，false为否
    HTTPSMODE:false, //是否开启HTTPS模式，true为是，false为否。如果开启，将会把协议更改为https和wss。
    chatStyle:"creative", //与Bing AI聊天时选用的聊天风格，balanced代表平衡，creative代表创造力，precise代表精确性
    tips:"", //在新的主题开始时的第一条对话前插入的提示，null和空的英文双引号（""）表示没有。
    fontColor:"white", //你和Bing AI在消息框中的消息字体颜色
    nameColor:"#dadada", //你和Bing AI显示名字的颜色
    backgroundUrl:"./src/images/Background.jpg", //背景图片的url地址，默认为项目文件中的Background.jpg
    saveChatTimes:20 //最大保存聊天记录数量
    
};
```

接下来你只要根据这段代码的中文注释来更改配置即可更改你的默认设置。
在更改你的默认设置后，打开本地客户端时，你的聊天设置会更改为默认设置中的那样。例如你在默认设置中表示你想要让chatStyle更改为"balanced"，那么在打开本地客户端时，聊天设置中的聊天风格设置将会自动更改为balanced。


# 其他

### 头像更改

进入./src/images文件夹，里面有两张图片，一个是`User.png`，一个是`Bing.png`，如果你想要更换你自己或New Bing的头像的话，就在这个文件夹中加入你想要更换的图片，并把它重命名为"User.png"或"Bing.png"。

## 一些疑难解答：

首先，在出现错误时，请第一时间反应：

```

点击“新主题”按钮。

如果不行，就升级库。运行Run文件夹下的`Update Libs.bat`以更新库。

再不行，就试着开启VPN。

还是不行，就更新一次自己的Cookie。

若以上所有方法都无效，请查看以下的疑难解答。还是无法解决问题，请咨询作者。

```

### python报错：找不到文件

你可能用的是1.5或以下的版本。可以升级至1.6解决这个问题。

### python报错：以一种访问权限不允许的方式做了 一个访问套接字的尝试。

在输入端口的时候，不要输原来的端口（例如你输入80，报了这个错，就把端口换成70或者90，都行）。然后打开index.html之后，在
“设置”按钮里把连接到的服务器改成127.0.0.1:端口号。记得不要漏了英文冒号。例如你把端口设置为70，就改成127.0.0.1:70。

如果使用ip地址或域名访问，都需要添加“:端口”，例如192.168.56.36:70 和 127.0.0.1:70。

### 安装依赖项时报错，pip不是命令或可执行的...

导致这个错误的原因是你没有将Python加入环境变量，或是没有安装Python。首先确保你安装了Python的高版本。如果安装了，那就是没加环境变量。

最简单的方法是先把Python卸载了，然后用安装包重新安装。在安装的过程中，注意要勾选“Add Python 3.xx to path”的选项，否则重装了之后还是
没法使用pip。

### 一直Loading for New Bing

你可以耐心等待（因为可能会比较久）。如果还是不出现，有可能是你的端口填写错误。如果你在BingServer.py启动时填了非80的端口，请在聊天页面打开设置，将连接到服务器的设置更改为“127.0.0.1:端口”。也可能是你下载的1.5.1和1.5版本在上传到Github时缺少了些什么，现已发布1.6版本。
可以重新下载来用。

### Python报错：KeyError等

这种情况下就是Bing不想回复你了。也就是强制结束了对话。多半是关于messgae的KeyError。如果不是，可以进一步寻求帮助。

### 生成图像时报错：Caused by NewConnectionError

生成图像功能需要开启VPN后才可以使用。

# 使用方法：

在文本框中输入问题（可以换行）。按下“发送”按钮或`Ctrl + Enter`快捷键发送信息给New Bing。

如果想开启新的话题，可以按下”新主题“。开启新主题后，会自动要求New Bing理解之前的聊天记录并继续与你聊天（目的是达到类似于无限续航的效果）。如果想要彻底重新开始对话，在设置里将保存记忆选项关闭。

按下设置按钮，有很多功能开关。你可以自己配置你的选项设置，这会影响到你与Bing的的聊天。

在文本框中，输入`/create images `（谨记，images后边还有个空格），可以激活图片生成功能。在刚才的指令后边跟上你想要生成的内容，如”/create images a little cat eating fish"，然后发送给New Bing，稍等一会即可
拿到New Bing生成的图片。（这个功能需要开启VPN才可以使用）。


# 结尾

## 鸣谢：

[Bing-Chat](https://github.com/XiaoXinYo/Bing-Chat)的开发者[XiaoXinYo](https://github.com/XiaoXinYo)  
本项目的[BingServer.py](https://github.com/xbzstudio/BingAI-Client/blob/main/BingServer.py)就是他开发的！  
（当然本人也在当中增加了许些功能！）

[InterestingDarkness](https://github.com/InterestingDarkness)为BingAI-Client开发了切换Sydney模式的功能 ，十分感谢！

[Nothingness-Void](https://github.com/Nothingness-Void)为BingAI-Client添加了requirements.txt。

[Viopsa233](https://github.com/viopsa233)为BingAI-Client添加了视频教程,添加了run.bat文件（旧版）。
