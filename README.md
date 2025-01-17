![](https://repository-images.githubusercontent.com/177628884/334b1080-8f94-11e9-9d0e-9b5d292bee8d)

# GameDevTools
游戏开发日常用到的工具集

将GameDevTools.bat 创建快捷方式 放到桌面就可以快速打开

网络慢的可以尝试下载Release版本

https://github.com/ThisisGame/GameDevTools/releases

# 搜索工具

比如我想查找打图集工具，关键词 texturepacker。
那么输入 texture 或者 pack 或者 tex ，只要输入关键词部分字母 即可查找。

输入工具序号，即可使用工具

# 新增工具
在GameDevTools.py 注册新的工具 与 关键字

```
toolSets=\
{
    # 注册程序 与 关键字，关键字有多个
    # Module:[['keyword1','keyword2'],'注释'],

    # 获取文件MD5
    GetFileMD5:[['md5','file md5','file'],u'获取文件MD5'],

    # 获取字符串MD5
    GetStrMD5:[['md5','string md5','string','str md5'],u'获取字符串MD5'],

    # 获取 10位 Unix时间戳 单位秒
    GetUnixTimeStamp:[['unix','time','timestamp'],u'获取 10位 Unix时间戳 单位秒'],

    # 获取 13位 Unix时间戳 单位毫秒
    GetUnixTimeStamp_ms:[['unix','time','timestamp','ms'],u'获取 13位 Unix时间戳 单位毫秒'],

    # 一键生成Android、IOS 多尺寸Icon
    MultiSizeIcon:[['icon','icon size'],u'一键生成Android、IOS 多尺寸Icon'],

    # 简单http服务器
    HttpServer:[['http','httpserver','http server'],u'简单http服务器'],

    # telnet 测试端口是否开启
    CheckServerPortOpen:[['telnet','checkserverportopen','port','network','server','net'],u'测试端口是否开启'],

    # 解压ZIP
    UnZipTools:[['zip','unzip','extra','extract'],u'解压ZIP'],

    # Unicode 转 普通中文显示 \u4eba\u751f\u82e6\u77ed\uff0cpy\u662f\u5cb8 人生苦短，py是岸
    UnicodeToChinese:[['unicode','gbk','chinese','\u','url','urlencode','code','codec'],u'Unicode 转 普通中文显示 \u4eba\u751f\u82e6\u77ed\uff0cpy\u662f\u5cb8 人生苦短，py是岸'],

    # 屏幕录制Gif
    ScreenCaptureGif:[['gif','screen','capture','rec','url','licecap','cap'],u'屏幕录制Gif'],

    # Notepad 文本编辑器
    Notepad:[['txt','exe','edit','note','notepad','text'],u'文本编辑器'],

    # PNGoo PNG无损压缩
    PNGoo_Win:[['png','compress','png compress','image','image compress','yasuo'],u'PNG无损压缩'],
}
```

# 更新日志

```
2019/6/15 phpStudy 2016版  集成最新的Apache+Nginx+LightTPD+PHP+MySQL+phpMyAdmin+Zend Optimizer+Zend Loader 官网 http://phpstudy.php.cn/wenda/407.html

2019/6/3 Win32DiskImager 写入ISO系统到U盘 树莓派安装系统 ,关键词 ['win32diskimager','iso','shumeipai','raspberrypi','raspberry pi']

2019/6/3 Archive7z 7z lzma压缩 ,关键词 ['7z','zip','rar','lzma','yasuo']

2019/6/3 Ex7z 7z lzma解压 ,关键词 ['7z','zip','rar','lzma','jieyasuo']

2019/5/28 Shadowsocks 代理 翻墙 VPN ,关键词 ['shadowsocks','vpn','fanqiang','daili','proxy']

2019/5/28 Everything 极速搜索电脑文件 ,关键词 ['Everything','find','search','file','dir','sousuo']

2019/5/17 HarExport H5网页游戏资源提取 ,关键词 ['harexport','h5','html','web']

2019/4/30 APKTools APK反编译工具套装 ,关键词 ['apktools','adb','jdjui','aapt']

2019/4/24 MergeVideo 视频合并工具 ,关键词 ['mergevideo','combine','add','mp4','flv','wmv','mkv']

2019/4/24 Audio_HZ_KBPS_Tools 音效格式转换工具 设置hz 比特率 ,关键词 ['audio_hz_kbps_bits','mp3','ogg','wav']

2019/4/24 ImageScale 图片缩放 指定比例,关键词 ['imagerescale','png','jpg','resize']

2019/4/24 ImageResize 图片缩放 指定尺寸,关键词 ['imageresize','png','jpg']

2019/4/19 to_JPG 图片转JPG工具 支持单文件与文件夹,关键词 ['image conv','webp','bmp','jpg','png']

2019/4/11 UnityAssetStudio Unity 资源导出工具,关键词 ['unityassetstudiogui','unitystudio','unityassetbundleexport']

2019/4/8 GetStrSHA1 sha1编码,关键词 ['sha1hash']

2019/4/8 GetStrBASE64 Base64编码,关键词 ['base64encode']

2019/4/8 BASE64_Decode Base64解码,关键词 ['base64decode']

2019/4/7 putty 远程Linux,关键词 ['putty','ssh']

2019/4/7 SqliteStudio 2.1.5 sqlite3管理软件,关键词 ['sqlitestudio_2_1_5','db','sqlite3']

2019/4/6 https://www.freesoundeffects.com/ 免费音效下载网站,关键词 ['visitfreesoundeffect','mp3','audio','wav','audio']

2019/4/6 新增SimpleDownload 单文件下载器，省的打开迅雷或者浏览器,关键词 ['http download','xunlei','xuanfeng','kuaiche','idm']

2019/4/6 新增GIMP 免费开源的图片编辑工具，替代Photoshop,关键词 ['gimp','png','image editor','jpg','photoshop','texture','ps']

2019/4/6 新增WinMerge 对比代码工具，也可以对比文件夹 文件，替代beyond compare,关键词 ['diff','beyond compare','winmerge']

2019/4/6 新增TextureMerger 打图集工具 提取自Egret,关键词 ['png','jpg','texturepacker','texturemerger']

2019/4/6 新增luac,关键词 ['luac','lua']

2019/4/6 新增lua,关键词 ['lua','LUA']

2019/4/6 新增PNG无损压缩工具 PNGoo_Win,关键词 ['png','compress','png compress','image','image compress','yasuo']

2019/4/4 新增文本编辑器 Notepad,关键词 ['txt','exe','edit','note','notepad','text']

2019/4/3 新增屏幕录制gif工具 ILCEcap,关键词 ['gif','screen','capture','rec','url','licecap','cap']
```
