# git源码：https://github.com/512433465/autotest_helper
# 安装教程
# 1、本工具和SDK自带Jar相同无需安卓。前提是您Mac或者Windows系统中已经安装并且配置好了Java1.8环境
# 2、Windows环境，复制该jar到您SDK安装目录uiautomatorviewer.jar所在的目录下(请先备份你原来的jar，一般目录在SDK的tools\lib下：\android-sdk-windows\tools\lib)
# 备份方法特别说明：SDK目录下只有一个uiautomatorviewer.jar的，把该jar后缀改为.zip,即改为uiautomatorviewer.jar==>uiautomatorviewer.zip，下载一个我二次开发的jar。把下载的jar放到该目录下即可。
# 有的同学SDK目录下有uiautomatorviewer.jar和uiautomatorviewer-26.0.0-dev.jar两个jar。把两个jar后缀都改为.zip即改为uiautomatorviewer.jar==>uiautomatorviewer.zip，uiautomatorviewer-26.0.0-dev.zip，先下载一个我二次开发的jar改为uiautomatorviewer-26.0.0-dev.jar，再下载一个我二次开发的jar。把两个jar放到该目录下即可。
# 所谓的备份，说白了，就是替换原有的jar的意思，大胆替换其实也是可以的，为了可以恢复为原来的jar起见，备份一下而已。
# 3、Mac环境，复制该jar到任意目录即可
# 4、安卓自动化：
# 复制 LvmamaXmlKit.jar到本地D盘根目录下，打开命令行窗口执行命令：adb push D:\LvmamaXmlKit.jar /data/local/tmp/
# (此处有一坑：LvmamaXmlKit.jar要push到/data/local/tmp/local/tmp/  下才能正常使用)
# 打开手机文件管理，到 /data/local/tmp/目录下，检查确保LvmamaXmlKit.jar是否复制到手机中（如图1）
# 模拟器中安装ADBKeyBoard.apk并设置设置默认输入法为ADBKeyBoard，并关闭硬件物理键盘（如图2）
# 打开您的app，点击uiautomatorviewer.bat 开启生成代码之旅。
#
# LvmamaXmlKit.jar一定要推送到手机里，截图，截取xml要用到这个jar