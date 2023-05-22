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