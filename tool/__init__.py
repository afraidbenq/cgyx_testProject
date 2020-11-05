"""
1.获取apk package 和 activity

aapt dump badging C:\Users\admin\Desktop\安卓apk\life_v1.0.18_2020-10-31_18_preview6.apk
appname: life_v1.0.18_2020-10-31_18_preview6.apk
appPackage: com.fanda.chungoulife
appActivity: com.ddz.component.welcome.WelcomeActivity


2.无线连接安卓设备进行appium自动化

有线连上手机
adb devices -l
开启无线连接端口（默认5555）
adb tcpip 5555
获取手机IP地址(手机和电脑要在同一个WiFi环境)
adb shell ip -f inet addr show wlan0 或 直接手机WiFi查看
31: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 10.1.101.229/23 brd 10.1.101.255 scope global wlan0
       valid_lft forever preferred_lft forever
无线连接手机地址
adb connect 10.1.101.229
返回connected to 10.1.101.229:5555表示连接成功

"""