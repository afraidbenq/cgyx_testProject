import requests
import json
import random
from config import Config


api_host = Config.API_HOST

# 浏览器头
# headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
#            'X-Requested-With': 'XMLHttpRequest',
#            'Connection': 'keep-alive',
#            'Referer': 'http://' + api_host,
#            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
#                          '79.0.3945.88 Safari/537.36'}

# 手机头
headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
           'X-Requested-With': 'XMLHttpRequest',
           'Connection': 'keep-alive',
           'Referer': 'http://' + api_host,
           'User-Agent': 'chun gou yan xuan/1.4.5 (iPhone; iOS 12.1; Scale/3.00)'}


class Common():
    @classmethod
    def sendMsg(self, mobile, scene):  # 1.发送验证码 scene为 0登录 1注册 2修改密码 3修改支付密码 4更换绑定手机 5忘记密码 6查看供应商 7 绑定银行卡 8微信绑定
        data = {'mobile': mobile, 'scene': scene}
        r = requests.post(api_host + '/index.php/' + 'Api/Index/sendMsg', headers=headers, data=data)
        status = r.status_code
        # resp = r.content
        resp = r.text
        # print(r.encoding)
        # print(status)
        # print(resp)
        # {"code":1,"msg":"OK","data":{"sid":"2019:3627002443808031913","fee":1}}

    def agreement(self, id):  # 2.各种协议 ID = 1 注册协议 （登录注册页面）ID = 2 支付协议（银行卡页面）
        data = {'id': id}
        r = requests.post(api_host + '/index.php/' + 'Api/Index/agreement', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def checkVerifyCode(self, mobile, verify_code, scene):  # 3.检查验证码
        data = {'mobile': mobile, 'verify_code': verify_code, 'scene': scene}
        r = requests.post(api_host + '/index.php/' + 'Api/Index/checkVerifyCode', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)
        # {"code":1,"msg":"验证码正确","data":[]}

    def getShareInfo(self, goods_id):  # 4.获取商品分享信息
        data = {'goods_id': goods_id}
        r = requests.post(api_host + '/index.php/' + 'Api/Goods/getShareInfo', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def getContactInfo(self, access_token):  # 5.获取店铺联系人信息
        data = {'access-token': access_token}
        r = requests.post(api_host + '/index.php/' + 'Api/Index/getContactInfo', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def merge(self, code):  # 6.合并
        data = {'code': code}
        r = requests.post(api_host + '/index.php/' + 'Api/Chuncode/merge', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def shareCode(self, code):  # 7.转赠或分享
        data = {'code': code}
        r = requests.post(api_host + '/index.php/' + 'Api/Chuncode/shareCode', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def getNextTaskInfo(self, ):  # 8.获取下一等级任务
        data = {'code': code}
        r = requests.post(api_host + '/index.php/' + 'Api/Member/getNextTaskInfo', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def getTC(self):  # 9.获取直属团长数
        data = {'code': code}
        r = requests.post(api_host + '/index.php/' + 'Api/Member/getTC', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def getTCs(self):  # 10.获取团长总数
        data = {'code': code}
        r = requests.post(api_host + '/index.php/' + 'Api/Member/getTCs', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def appStatus(self, version):  # 11.app审核开关
        data = {'version': version}
        r = requests.post(api_host + '/index.php/' + 'Api/Index/appStatus', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def getNewMission(self):  # 12.获取等级任务
        data = {'version': version}
        r = requests.post(api_host + '/index.php/' + 'Api/Member/getNewMission', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def buyGiftUpLevel(self):  # 13.团长升级接口
        data = {'version': version}
        r = requests.post(api_host + '/index.php/' + 'Api/Member/buyGiftUpLevel', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def getVersion(self, platform):  # 14.APP版本控制
        data = {'platform': platform}
        r = requests.post(api_host + '/index.php/' + 'Api/Version/getVersion', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def getRegionJsonFile(self, version, h5):  # 15 更新地址库
        data = {'version': version, 'h5': h5}
        r = requests.post(api_host + '/index.php/' + 'Api/Index/getRegionJsonFile', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def getAppId(self, pay_name, pay_type):  # 16.获取appid
        data = {'pay_name': pay_name, 'pay_type': pay_type}
        r = requests.post(api_host + '/index.php/' + 'api/wx/getAppId', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def put_device(self, device_type, device_jpush, device_info, version, access_token):  # 17.提交设备信息
        data = {'device_type': device_type, 'device_jpush': device_jpush, 'device_info': device_info,
                'version': version, 'access-token': access_token, }
        r = requests.post(api_host + '/index.php/' + 'api/Index/put_device', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def getUserInfo(self, login_platform):  # 18.获取用户信息
        data = {'login_platform': login_platform}
        r = requests.get(api_host + '/index.php/' + 'api/user/getUserInfo', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def getSignPackage(self, url):  # 19.获取jssdk签名
        data = {'url': url}
        r = requests.post(api_host + '/index.php/' + 'api/wx/getSignPackage', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)


class LoginReg():
    @classmethod
    def reg(self, username, verify_code, password, type, login_platform):  # 1.注册
        data = {'username': username, 'verify_code': verify_code, 'password': password, 'type': type,
                'login_platform': login_platform}
        r = requests.post(api_host + '/index.php/' + 'Api/Index/reg', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    # {"code":1,"msg":"操作成功","data":{"token":"13823417742.1583377767.66442.c42d7166408ce0c43ce8c9b71df10ea6",
    # "user_id":508072,"seller":0,"nickname":"13823417742","head_pic":"","sex":0,"user_money":"0.00",
    # "frozen_money":"0.00","mobile":"13823417742","level":2,"push_id":"","first_leader":0,"is_bind":1,
    # "level_name":"超级VIP","level_amount":1,"is_auth":0,"invite_code":"CG3906927","oauth":"","openid":"",
    # "unionid":"","have_pass":1}}
    @classmethod
    def login(self, username, verify_code, password, type, login_platform):  # 2.用户登录
        data = {'username': username, 'verify_code': verify_code, 'password': password, 'type': type,
                'login_platform': login_platform}
        r = requests.post(api_host + '/index.php/' + 'Api/Index/login', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        # resp = r.content
        # resp = json.loads(resp.decode())
        print(status)
        print(resp)
        return resp

    @classmethod
    def login1(self, username, password):  # 2.用户手机密码登录
        data = {'username': username, 'password': password, 'type': 2}
        r = requests.post(api_host + '/index.php/' + 'Api/Index/login', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        # print(resp.startswith('', 0, 3))
        # if resp.startswith('', 0, 3):
        #     resp = json.loads(resp.encode()[3:].decode())  # 灰度需去掉BOM头处理
        # else:
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    def forget(self, username, verify_code, password):  # 3.忘记密码
        data = {'username': username, 'verify_code': verify_code, 'password': password}
        r = requests.post(api_host + '/index.php/' + 'Api/Index/forget', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def wxLogin(self, type, openid, unionid, invite_code, login_platform):  # 4.三方登录
        data = {'type': type, 'openid': openid, 'unionid': unionid, 'invite_code': invite_code,
                'login_platform': login_platform}
        r = requests.post(api_host + '/index.php/' + 'Api/Index/wxLogin', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def wxBind(self, username, verify_code, openid, unionid, header, nickname, sex, invite_code,
               login_platform):  # 5.绑定手机
        data = {'username': username, 'verify_code': verify_code, 'openid': openid, 'unionid': unionid,
                'header': header, 'nickname': nickname, 'sex': sex, 'invite_code': invite_code,
                'login_platform': login_platform}
        r = requests.post(api_host + '/index.php/' + 'Api/Index/wxBind', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def thirdPartyUnBind(self, type, openid):  # 6.解除绑（无用）
        data = {'type': type, 'openid': openid}
        r = requests.post(api_host + '/index.php/' + 'Api/ThirdParty/thirdPartyUnBind', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def checkUsers(self, username):  # 7.检查手机号码是否已注册
        data = {'username': username}
        r = requests.post(api_host + '/index.php/' + 'Api/Index/checkUsers', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def loginOut(self, access_token):  # 8.退出登录
        headers['Access-token'] = access_token
        r = requests.post(api_host + '/index.php/' + 'Api/User/loginOut', headers=headers)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def setDefaultLoginPass(self, access_token, password, confirm_pass):  # 9.设置密码（淘宝联盟优化）
        headers['Access-token'] = access_token
        data = {'password': password, 'confirm_pass': confirm_pass}
        r = requests.post(api_host + '/index.php/' + 'Api/User/setDefaultLoginPass', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def searchInviteCode(self, access_token, invite_code):  # 10.邀请码查找导师
        headers['Access-token'] = access_token
        data = {'invite_code': invite_code}
        r = requests.post(api_host + '/index.php/' + 'Api/User/searchInviteCode', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)


class Index():
    def index(self):  # 1.首页
        r = requests.post(api_host + '/index.php/' + 'Api/Index/index', headers=headers)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def slider(self, pid):  # 2.轮播图
        data = {'pid': pid}
        r = requests.post(api_host + '/index.php/' + 'Api/Index/slider', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def headCate(self):  # 3.首页头部分类
        r = requests.post(api_host + '/index.php/' + 'Api/Index/headCate', headers=headers)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def categoryPage(self, cid):  # 4.分类首页（品质生鲜）
        data = {'cid': cid}
        r = requests.post(api_host + '/index.php/' + 'Api/Index/categoryPage', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def midCategory(self, cid):  # 5.精选分类
        data = {'cid': cid}
        r = requests.post(api_host + '/index.php/' + 'Api/Index/midCategory', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def message(self, access_token):  # 6.我的消息
        headers['Access-token'] = access_token
        r = requests.post(api_host + '/index.php/' + 'Api/Index/message', headers=headers)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def brand_index_list(self):  # 7.首页品牌大促
        r = requests.post(api_host + '/index.php/' + 'Api/Index/brand_index_list', headers=headers)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def midCategoryV2(self, cid, tag_id):  # 8.精选分类V2(单独获取商品信息)
        data = {'cid': cid, 'tag_id': tag_id}
        r = requests.post(api_host + '/index.php/' + 'Api/Index/midCategoryV2', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def midCategoryTag(self, cid):  # 9.精选分类标签
        data = {'cid': cid}
        r = requests.post(api_host + '/index.php/' + 'Api/Index/midCategoryTag', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def homeTaskPopup(self):  # 10.降级任务弹窗
        r = requests.post(api_host + '/index.php/' + 'api/Index/homeTaskPopup', headers=headers)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def indexV2(self, Device_Type):  # 11.首页V2
        headers['Device-Type'] = Device_Type  # 1-android 2-ios 3-winphone 4-H5 5-微信小程序
        r = requests.post(api_host + '/index.php/' + 'Api/Index/indexV2', headers=headers)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def indexUnlimitedGoods(self, page):  # 13.首页无限商品列表
        data = {'page': page}
        r = requests.post(api_host + '/index.php/' + 'Api/Index/indexUnlimitedGoods', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def indexGroupMsg(self):  # 14.首页开团信息
        r = requests.post(api_host + '/index.php/' + 'Api/Index/indexGroupMsg', headers=headers)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def thematicList(self, thematic_id, goods_id):  # 15.专题列表
        data = {'thematic_id': thematic_id, 'goods_id': goods_id}
        r = requests.post(api_host + '/index.php/' + 'Api/Index/thematicList', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def getBarrage(self):  # 16.获取弹幕
        r = requests.post(api_host + '/index.php/' + 'Api/Index/getBarrage', headers=headers)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)


class Goods():
    def category(self):  # 1.分类
        r = requests.post(api_host + '/index.php/' + 'Api/Goods/category', headers=headers)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def index(self, page, keyword, cate_id):  # 2.搜索结果（商品列表）
        data = {'page': page, 'keyword': keyword, 'cate_id': cate_id}
        r = requests.post(api_host + '/index.php/' + 'Api/Goods/index', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def detail(self, id):  # 3.商品详情
        data = {'id': id}
        r = requests.post(api_host + '/index.php/' + 'Api/Goods/detail', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def guess(self, access_token):  # 4.猜你喜欢（搜索页）
        headers['access-token'] = access_token
        r = requests.post(api_host + '/index.php/' + 'Api/Index/guess', headers=headers)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def flashDetail(self, id):  # 5.商品详情（秒杀抢购）
        data = {'id': id}
        r = requests.post(api_host + '/index.php/' + 'Api/Goods/flashDetail', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def commentList(self, goods_id, page):  # 5.商品评论列表
        data = {'goods_id': goods_id, 'page': page}
        r = requests.post(api_host + '/index.php/' + 'Api/Goods/commentList', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def collect(self, access_token, goods_id):  # 6.收藏商品
        headers['access-token'] = access_token
        data = {'goods_id': goods_id}
        r = requests.post(api_host + '/index.php/' + 'Api/Goods/collect', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def brandPage(self, id):  # 7.品牌首页
        data = {'id': id}
        r = requests.post(api_host + '/index.php/' + 'Api/Goods/brandPage', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def goodsRemind(self, access_token, prom_id, prom_type):  # 8.添加商品提醒
        headers['access-token'] = access_token
        data = {'prom_id': prom_id, 'prom_type': prom_type}
        r = requests.post(api_host + '/index.php/' + 'Api/Goods/goodsRemind', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def maxCount(self):  # 9.单次购买商品的最大数
        r = requests.post(api_host + '/index.php/' + 'Api/Goods/maxCount', headers=headers)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def check_goods_stock(self, goods_id, item_id, goods_num):  # 10.检查商品库存数量
        data = {'goods_id': goods_id, 'item_id': item_id, 'goods_num': goods_num}
        r = requests.post(api_host + '/index.php/' + 'Api/Goods/check_goods_stock', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def newCategory(self):  # 11.分类（新）
        r = requests.post(api_host + '/index.php/' + 'Api/Goods/newCategory', headers=headers)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def catePage(self, category_id, page):  # 12.分类分页（新）
        data = {'category_id': category_id, 'page': page}
        r = requests.post(api_host + '/index.php/' + 'Api/Goods/catePage', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def miniIndexGoods(self):  # 13.小程序首页商品
        r = requests.post(api_host + '/index.php/' + 'Api/Goods/miniIndexGoods', headers=headers)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def goodsCheck(self, goods_id):  # 14.商品结算页弹窗
        data = {'goods_id': goods_id}
        r = requests.post(api_host + '/index.php/' + 'api/tips/goodsCheck', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)


class Cart():

    def addCart(self, goods_id, goods_num, item_id, flash_sale_id):  # 1.加入购物车
        data = {'goods_id': goods_id, 'goods_num': goods_num, 'item_id': item_id, 'flash_sale_id': flash_sale_id}
        r = requests.post(api_host + '/index.php/' + 'Api/Cart/addCart', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def changeNum(self, cart_id, goods_num):  # 2.改变购物车商品数量
        data = {'cart_id': cart_id, 'goods_num': goods_num}
        r = requests.post(api_host + '/index.php/' + 'Api/Cart/changeNum', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    @classmethod
    def addressList(self, access_token, page):  # 6.我的地址
        headers['access-token'] = access_token
        data = {'page': page}  # 还有keyword未用到
        r = requests.post(api_host + '/index.php/' + 'Api/User/addressList', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        # if resp.startswith('', 0, 3):
        #     resp = json.loads(resp.encode()[3:].decode())  # 灰度需去掉BOM头处理
        # else:
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def addAddress(self, access_token, consignee, province, city, district, address, mobile, label):  # 6.新增地址
        headers['access-token'] = access_token
        data = {'consignee': consignee, 'province': province, 'city': city, 'district': district, 'address': address,
                'mobile': mobile, 'label': label, }
        r = requests.post(api_host + '/index.php/' + 'Api/User/addAddress', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def addAddress1(self, access_token, consignee, province, city, district, address, mobile, label,
                    address_id):  # 6.编辑地址
        headers['access-token'] = access_token
        data = {'consignee': consignee, 'province': province, 'city': city, 'district': district, 'address': address,
                'mobile': mobile, 'label': label, 'address_id': address_id}
        r = requests.post(api_host + '/index.php/' + 'Api/User/addAddress', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    @classmethod
    def setDefaultAddress(self, access_token, address_id):  # 8.设置为默认地址
        headers['access-token'] = access_token
        data = {'address_id': address_id}
        r = requests.post(api_host + '/index.php/' + 'Api/User/setDefaultAddress', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    @classmethod
    def submitOrder(self, access_token, address_id, goods_id, goods_num, item_id, act='submit_order'):  # 13.提交订单
        headers['access-token'] = access_token
        data = {'address_id': address_id, 'goods_id': goods_id, 'goods_num': goods_num,
                'item_id': item_id, 'act': act}
        r = requests.post(api_host + '/index.php/' + 'Api/Cart/submitOrder', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    @classmethod
    def submitOrder1(self, access_token, address_id, goods_id, goods_num, item_id,
                     action, act='get_price'):  # 13.获取订单价格
        headers['access-token'] = access_token
        data = {'address_id': address_id, 'goods_id': goods_id, 'goods_num': goods_num,
                'item_id': item_id, 'action': action, 'act': act}
        r = requests.post(api_host + '/index.php/' + 'Api/Cart/submitOrder', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

    def submitOrder2(self, access_token, address_id, user_money, pay_pwd, user_note, goods_id, goods_num, item_id,
                     prom_type, prom_id, action, act, realname, id_card, order_type,
                     related_id):  # 13.提交订单/获取订单价格  使用余额纯点
        headers['access-token'] = access_token
        data = {'address_id': address_id, 'user_money': user_money, 'pay_pwd': pay_pwd, 'user_note': user_note,
                'goods_id': goods_id, 'goods_num': goods_num, 'item_id': item_id, 'prom_type': prom_type,
                'prom_id': prom_id, 'action': action, 'act': act, 'realname': realname, 'id_card': id_card,
                'order_type': order_type, 'related_id': related_id}
        r = requests.post(api_host + '/index.php/' + 'Api/Cart/submitOrder', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)


class My():
    @classmethod
    def bindLeader(self, access_token, invite_code):  # 23.绑定导师
        headers['access-token'] = access_token
        data = {'invite_code': invite_code}
        r = requests.post(api_host + '/index.php/' + 'Api/User/bindLeader', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp


class Order():
    @classmethod
    def orderList(self, access_token, type):
        headers['access-token'] = access_token
        data = {'type': type}
        r = requests.post(api_host + '/index.php/' + 'Api/Order/orderList', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        # if resp.startswith('', 0, 3):
        #     resp = json.loads(resp.encode()[3:].decode())  # 灰度需去掉BOM头处理
        # else:
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def refund(self, access_token, order_id, reason, info, refund_mobile, refund_money):  # 11.申请退款
        headers['access-token'] = access_token
        data = {'order_id': order_id, 'reason': reason, 'info': info, 'refund_mobile': refund_mobile,
                'refund_money': refund_money}
        r = requests.post(api_host + '/index.php/' + 'Api/Order/refund', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)


class Pay():
    def payList(self, access_token, pay_type):  # 3.支付列表
        headers['access-token'] = access_token
        data = {'pay_type': pay_type}
        r = requests.post(api_host + '/index.php/' + 'Api/Pay/payList', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)

        # {"code":1,"msg":"操作成功","data":[{"front_name":"微信支付","pay_name":"youths","pay_code":"wxPay","is_default":1,"logo":"https:\/\/testimg.chungoulife.com\/201910\/pic3349a1c1a50fd9ea7c4e82f3a8e3df68.png"},{"front_name":"支付宝","pay_name":"alipay","pay_code":"alipay","is_default":0,"logo":"https:\/\/testimg.chungoulife.com\/201910\/picf02d67137dfff10411be26743507ee32.png"}]}

    @classmethod
    def testpay(self, access_token, order_id):  # 虚拟支付
        headers['access-token'] = access_token
        extension_code = '02019100722001433940' + str(random.randint(1, 1000000000))
        data = {'order_id': order_id, 'extension_code': extension_code}
        r = requests.post(api_host + '/index.php/' + 'api/index/testpay', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        print(status)
        print(resp)


if __name__ == '__main__':
    c = Common()
    # c.sendMsg(13823417742, 0)
    # c.sendMsg(19100500086, 0)
    # with MysqlDb() as db:
    #     sql = "SELECT code FROM `chungou`.`cg_sms_log` WHERE `mobile` = '13823417742' ORDER BY `id` DESC LIMIT 0,1"
    #     rt = db.query(sql)
    #     code = rt[0]['code']
    #     print(code)
    # c.agreement(1)
    # c.checkVerifyCode(13823417742, 3517, 1)
    # c.getNextTaskInfo()
    # c.appStatus(1.0)
    l = LoginReg()

    # l.reg()
    r = l.login1(13823417742, 123456)
    # r = l.login(19100500086, code, 'a123456', 1, 'app')
    token = r['data']['token']
    print(token)
    token = '13823417742.1583739380.76273.30af73e75d70ad6eccfd3861ac946a71'

    # 新增地址
    ca = Cart()
    # ca.addAddress(token,'卢俊杰',1,2,3,'中和广场31楼',13823417742,'家')
    # 获取地址id
    r = ca.addressList(token, 1)
    addressid = r['data']['data'][0]['address_id']
    print(addressid)
    # 设为默认地址
    # ca.setDefaultAddress(token, addressid)
    # 计算订单
    ca.submitOrder1(token, addressid, 1940, 1, 0, 'buy_now')
    # # 提交订单
    ca.submitOrder(token, addressid, 1940, 1, 0)

    o = Order()
    # 我的订单列表
    r = o.orderList(token, 1)
    orderid = r['data']['data'][0]['order_id']
    print(orderid)

    p = Pay()
    # 虚拟支付
    # p.testpay(token, orderid)

    # 申请退款
    # o.refund(token, orderid, '不想要了', '就是不想要了', 13823417742, 0.01)

    # sleep(5)
    # l.loginOut(token)
    # i = Index()
    # i.index()
