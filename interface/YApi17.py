import requests
import json
from config import Config

api_host = Config.API_HOST
headers = {'Content-Type': 'application/json;charset=UTF-8', 'X-Requested-With': 'XMLHttpRequest',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
           'Cookie': '_yapi_uid=141; _yapi_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjE0MSwiaWF0IjoxNTg4NzY2MDg2LCJleHAiOjE1ODkzNzA4ODZ9.O5Q_1C6nDmhRNd37xPM1wR-BThAvBoqepdJlzRMJJW0',
           'Host': 'cgyapi.chungoulife.com', 'Referer': 'https://cgyapi.chungoulife.com/project/17/interface/api'}


class Public:
    @classmethod
    def wx_getappid(cls, pay_name, pay_type):  # Author：haojin
        """
        16.获取appid
        :param pay_name: ['text', '1', 'wxPay', 'joinPay（汇聚） ，wxPay（微信支付）']
        :param pay_type: ['text', '1', 'appPay', 'appPay （app支付），jssdkpay （jssdk支付 ）']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'pay_name': pay_name,
            'pay_type': pay_type,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Wx/getAppId', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_getuserinfo(cls, access_token, login_platform):  # Author：haojin
        """
        18.取用户信息
        :param access_token: token
        :param login_platform: ['text', '1', 'h5', '登录平台，h5团长登录传:h5;  app传：app']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'login_platform': login_platform,
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/getUserInfo', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def wx_getsignpackage(cls, url):  # Author：haojin
        """
        19.获取jssdk签名
        :param url: ['text', '1', 'https://www/baidu.com?a=1', '确认url是页面完整的url(请在当前页面alert(location.href.split(‘#’)[0])确认)，包括’http(s)😕/‘部分，以及’？’后面的GET参数部分,但不包括’#’hash后面的部分。']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'url': url,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Wx/getSignPackage', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def _test(cls):  # Author：18814188357@163.com
        """
        跳转类型定义
        :return:
        """
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/test', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp


class SubCommissionGiftBag:
    @classmethod
    def member_getcommission(cls, access_token):  # Author：MikeLue
        """
        当月佣金数据
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Member/getCommission', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def member_getallfee(cls):  # Author：MikeLue
        """
        本月贡献值统计
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Member/getAllFee', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def cos_uploadimg(cls, file):  # Author：MikeLue
        """
        上传图片
        :param file: ['text', '1', None, '图片']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'file': file,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Cos/uploadImg', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def cos_getpictask(cls):  # Author：MikeLue
        """
        返回当月任务数
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Cos/getPicTask', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def cos_uploadurl(cls, url, type):  # Author：MikeLue
        """
        保存任务截图
        :param url: ['text', '1', None, '数组']
        :param type: ['text', '1', '', '截图类型 0培训截图 1社群截图']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'url': url,
            'type': type,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Cos/uploadUrl', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def cos_getpicinfo(cls, type):  # Author：MikeLue
        """
        返回当月任详情
        :param type: ['text', '1', None, '截图类型 0培训截图 1社群截图']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'type': type,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Cos/getPicInfo', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def cos_getpiclist(cls):  # Author：MikeLue
        """
        返回任务列表
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Cos/getPicList', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def contribution_index(cls, access_token):  # Author：MikeLue
        """
        贡献值h5首页
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Contribution/index', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def contribution_history(cls, access_token, year=None):  # Author：MikeLue
        """
        贡献值h5历史页面
        :param access_token: token
        :param year: ['text', '0', None, '年份，不传默认为当年，示例参数值：2019']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'year': year,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Contribution/history', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def contribution_geturl(cls, access_token):  # Author：MikeLue
        """
        获取贡献值h5链接
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Contribution/getUrl', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def contribution_getdetail(cls, access_token, p, date_type=None, status_type=None, sdate=None,
                               edate=None):  # Author：MikeLue
        """
        贡献值明细
        :param access_token: token
        :param p: ['text', '1', '', '页数']
        :param date_type: ['text', '0', None, '筛选时间段, 1-今日实时,2-昨天,3-近七天,4-近30天,5-自定义时间段']
        :param status_type: ['text', '0', '', '状态筛选, 1-待获取, 2-已获取, 3-已失效']
        :param sdate: ['text', '0', '', '开始日期']
        :param edate: ['text', '0', '', '结束时间']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'p': p,
            'date_type': date_type,
            'status_type': status_type,
            'sdate': sdate,
            'edate': edate,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Contribution/getDetail', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def contribution_historynew(cls, access_token, p=None):  # Author：MikeLue
        """
        贡献值历史列表
        :param access_token: token
        :param p: ['text', '0', None, '页码，不传默认为1，示例参数值：1']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'p': p,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Contribution/historyNew', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp


class LargeScaleDividend:
    @classmethod
    def member_getcurmonthplate(cls, access_token):  # Author：MikeLue
        """
        当月总的分红金额
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Member/getCurMonthPlate', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def member_getplatecount(cls, access_token):  # Author：MikeLue
        """
        用户参与的分红次数
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Member/getPlateCount', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def member_getplatemoney(cls, access_token):  # Author：MikeLue
        """
        当前用户参与的分红金额
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Member/getPlateMoney', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def member_getcurmonthog(cls, type):  # Author：MikeLue
        """
        用户当月的单数或礼包
        :param type: ['text', '1', None, '0购物单数 1推荐的礼包数']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'type': type,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Member/getCurMonthOg', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def member_getplatedish(cls, access_token, type):  # Author：MikeLue
        """
        用户的全民/精英收益
        :param access_token: token
        :param type: ['text', '1', None, None]
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'type': type,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Member/getPlateDish', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def member_getplatemax(cls, access_token):  # Author：MikeLue
        """
        当次的最高收益
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Member/getPlateMax', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def member_getplatelist(cls, type):  # Author：MikeLue
        """
        历史收益
        :param type: ['text', '1', None, '0 全部 1 一个月 2 三个月 3 半年']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'type': type,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Member/getPlateList', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp


class MyTeam:
    @classmethod
    def member_getallteam(cls, access_token):  # Author：MikeLue
        """
        我的好友总数
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Member/getAllTeam', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def member_getperdaycount(cls, access_token):  # Author：MikeLue
        """
        我的每日新增成员
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Member/getPerDayCount', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp


class PurchaseAnUpgradeRequest:
    @classmethod
    def user_levelequity(cls, access_token):  # Author：TZK
        """
        1.获取弹窗内容
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/levelEquity', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_v2alert(cls, access_token):  # Author：TZK
        """
        2.是否显示恭喜弹窗
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/v2Alert', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_closev2alert(cls, access_token):  # Author：TZK
        """
        3.设置恭喜弹窗不再显示
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/closeV2Alert', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_closev2webalert(cls, access_token):  # Author：TZK
        """
        4.H5设置恭喜弹窗不再显示
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/closeV2WebAlert', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_v2webalert(cls, access_token):  # Author：TZK
        """
        5.H5是否显示恭喜弹窗
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/v2WebAlert', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp


class NewSeckill:
    @classmethod
    def flashsale_flashsaledetail(cls, flash_sale_id, goods_id):  # Author：hfc
        """
        1.商品详情(新秒杀)
        :param flash_sale_id: ['text', '1', '240', '活动id']
        :param goods_id: ['text', '1', '1963', '商品id']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'flash_sale_id': flash_sale_id,
            'goods_id': goods_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Flashsale/flashSaleDetail', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def _index(cls):  # Author：hfc
        """
        2.秒杀首页
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/index', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def seckill_seckillarea(cls, access_token, flash_sale_id):  # Author：hfc
        """
        3.秒杀专区
        :param access_token: token
        :param flash_sale_id: ['text', '1', '240', '秒杀活动id']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'flash_sale_id': flash_sale_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Seckill/seckillArea', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def seckill_geturl(cls):  # Author：hfc
        """
        4.获取h5地址链接
        :return:
        """
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Seckill/getUrl', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def seckill_getseckillareashare(cls, access_token, flash_sale_id='240'):  # Author：hfc
        """
        5.秒杀专区h5分享
        :param access_token: token
        :param flash_sale_id: ['text', '0', '240', '秒杀活动id']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'flash_sale_id': flash_sale_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Seckill/getSeckillAreaShare', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def seckill_seckillareapage(cls):  # Author：hfc
        """
        6.秒杀专区-分页
        :return:
        """
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Seckill/seckillAreaPage', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def seckill_shareflashsaleinfo(cls, access_token):  # Author：hfc
        """
        7.弹幕信息
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Seckill/shareFlashsaleInfo', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def seckill_remind(cls, access_token, flash_sale_id, goods_id, status):  # Author：hfc
        """
        8.设置提醒
        :param access_token: token
        :param flash_sale_id: ['text', '1', '240', '活动id']
        :param goods_id: ['text', '1', '1963', '商品id']
        :param status: ['text', '1', '1', '0-取消提醒 1-设置提醒']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'flash_sale_id': flash_sale_id,
            'goods_id': goods_id,
            'status': status,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Seckill/remind', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def seckill_getshareparam(cls, access_token, flash_sale_id):  # Author：hfc
        """
        9.海报参数接口
        :param access_token: token
        :param flash_sale_id: ['text', '1', '240', '活动id']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'flash_sale_id': flash_sale_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Seckill/getShareParam', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp


class Wallet:
    @classmethod
    def wallet_withdraw(cls, access_token, cashout_money, cashout_pwd, yzm):  # Author：文忠孝
        """
        提现申请
        :param access_token: token
        :param cashout_money: ['text', '1', '0.01', '提现金额（元），精确到小数点后两位']
        :param cashout_pwd: ['text', '1', '123456', '提现支付密码']
        :param yzm: ['text', '1', '123456', '验证码']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'cashout_money': cashout_money,
            'cashout_pwd': cashout_pwd,
            'yzm': yzm,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Wallet/withdraw', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def wallet_signcontract(cls, access_token):  # Author：文忠孝
        """
        用户签约
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Wallet/signContract', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def wallet_flow(cls, access_token, page='1', pagesize='10', type='0', date='2020-04'):  # Author：文忠孝
        """
        账户流水信息
        :param access_token: token
        :param page: ['text', '0', '1', '第几页，默认值1']
        :param pagesize: ['text', '0', '10', '页面数据条数，默认值10']
        :param type: ['text', '0', '0', '业务类型id 0-全部（默认值） 1-分润, 2-提现, 3-提现失败退回']
        :param date: ['text', '0', '2020-04', '流水时间范围 具体到月份，则返回当月流水；具体到日期，则返回当天流水；默认值：空字符串，空字符串时，返回所有流水']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'page': page,
            'pagesize': pagesize,
            'type': type,
            'date': date,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Wallet/flow', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def wallet_withdrawstatus(cls, access_token, order_id):  # Author：文忠孝
        """
        用户提现状态
        :param access_token: token
        :param order_id: ['text', '1', '1', '提现记录id']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'order_id': order_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Wallet/withdrawStatus', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def wallet_deletebankcard(cls, access_token, bank_id):  # Author：文忠孝
        """
        解绑银行卡
        :param access_token: token
        :param bank_id: ['text', '1', '1', '银行卡记录id']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'bank_id': bank_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Wallet/deleteBankCard', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp


class TencentCloud:
    @classmethod
    def upload_gettemptoken(cls):  # Author：孔佳男polaris
        """
        临时密钥获取
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/admin/upload/getTempToken', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp


class SignIn:
    @classmethod
    def index_reg(cls, username, verify_code, password, type, invite_code, login_platform=None):  # Author：TZK
        """
        1.注册
        :param username: ['text', '1', '', '用户名（手机号码）']
        :param verify_code: ['text', '1', '', '手机验证码']
        :param password: ['text', '1', '', '密码']
        :param type: ['text', '1', '', '1 需要提供密码 0 不许提供密码 默认是不需提供密码']
        :param invite_code: ['text', '1', '', '导师邀请码']
        :param login_platform: ['text', '0', '', '团长H5登录页面传：h5 ;app传：app']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'username': username,
            'verify_code': verify_code,
            'password': password,
            'type': type,
            'invite_code': invite_code,
            'login_platform': login_platform,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/reg', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_login(cls, username, verify_code, password, type, login_platform=None):  # Author：TZK
        """
        2.登录
        :param username: ['text', '1', '', '用户名（手机号码）']
        :param verify_code: ['text', '1', '', '手机验证码']
        :param password: ['text', '1', '', '密码']
        :param type: ['text', '1', '', '登录类型 1验证码登录 2手机号码登录 默认1']
        :param login_platform: ['text', '0', '', '团长H5登录页面传：h5 ;app传：app']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'username': username,
            'verify_code': verify_code,
            'password': password,
            'type': type,
            'login_platform': login_platform,
        }
        r = requests.post(api_host + '/index.php' + '/api/Index/login', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_forget(cls, username, verify_code, password):  # Author：TZK
        """
        3.忘记密码
        :param username: ['text', '1', '', '用户名（手机号码）']
        :param verify_code: ['text', '1', '', '手机验证码']
        :param password: ['text', '1', '', '新密码']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'username': username,
            'verify_code': verify_code,
            'password': password,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/forget', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_wxbind(cls, username, verify_code, openid, unionid, invite_code, header=None, nickname=None, sex=None,
                     login_platform=None):  # Author：TZK
        """
        4.绑定手机
        :param username: ['text', '1', '', '用户名（手机号码）']
        :param verify_code: ['text', '1', '', '手机验证码']
        :param openid: ['text', '1', '', 'openid']
        :param unionid: ['text', '1', '', 'unionid']
        :param invite_code: ['text', '1', '', '邀请码']
        :param header: ['text', '0', '', '性别']
        :param nickname: ['text', '0', '', '昵称']
        :param sex: ['text', '0', '', '用户性别 1男 2女 0未知']
        :param login_platform: ['text', '0', '', '团长H5登录页面传：h5 ;app传：app']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'username': username,
            'verify_code': verify_code,
            'openid': openid,
            'unionid': unionid,
            'invite_code': invite_code,
            'header': header,
            'nickname': nickname,
            'sex': sex,
            'login_platform': login_platform,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/wxBind', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_wxlogin(cls, username, verify_code, openid, unionid, invite_code, header=None, nickname=None, sex=None,
                      login_platform=None):  # Author：TZK
        """
        5.三方登录
        :param username: ['text', '1', '', '用户名（手机号码）']
        :param verify_code: ['text', '1', '', '手机验证码']
        :param openid: ['text', '1', '', 'openid']
        :param unionid: ['text', '1', '', 'unionid']
        :param invite_code: ['text', '1', '', '邀请码']
        :param header: ['text', '0', '', '性别']
        :param nickname: ['text', '0', '', '昵称']
        :param sex: ['text', '0', '', '用户性别 1男 2女 0未知']
        :param login_platform: ['text', '0', '', '团长H5登录页面传：h5 ;app传：app']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'username': username,
            'verify_code': verify_code,
            'openid': openid,
            'unionid': unionid,
            'invite_code': invite_code,
            'header': header,
            'nickname': nickname,
            'sex': sex,
            'login_platform': login_platform,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/wxLogin', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_checkusers(cls, username):  # Author：TZK
        """
        6.检查手机号码是否已注册
        :param username: ['text', '1', '', '用户名（手机号码）']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'username': username,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/checkUsers', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_loginout(cls):  # Author：TZK
        """
        7.退出登录
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/loginOut', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_setdefaultloginpass(cls, access_token, password, confirm_pass):  # Author：TZK
        """
        8.设置密码（淘宝联盟优化）
        :param access_token: token
        :param password: ['text', '1', None, '新密码']
        :param confirm_pass: ['text', '1', '', '确认密码']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'password': password,
            'confirm_pass': confirm_pass,
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/setDefaultLoginPass', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_searchinvitecode(cls, access_token, invite_code):  # Author：TZK
        """
        9.邀请码查找导师
        :param access_token: token
        :param invite_code: ['text', '1', '', '邀请码（可带可不带CG前缀）']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'invite_code': invite_code,
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/searchInviteCode', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_checkwxbindmobile(cls, access_token, username, unionid):  # Author：TZK
        """
        10.微信绑定-手机号码检测
        :param access_token: token
        :param username: ['text', '1', '', '手机号码']
        :param unionid: ['text', '1', '', 'unionid']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'username': username,
            'unionid': unionid,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/checkWxBindMobile', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp


class My:
    @classmethod
    def user_index(cls, access_token):  # Author：wlybq
        """
        我的
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/index', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_upgradeimg(cls):  # Author：lihb
        """
        获取会员升级图片
        :return:
        """
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/User/upgradeImg', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_delgoodsvisit(cls, access_token, visit_ids):  # Author：郑凯
        """
        删除足迹
        :param access_token: token
        :param visit_ids: ['text', '1', None, None]
        :return:
        """
        headers['Content-Type'] = 'application/json'
        headers['access-token'] = access_token
        data = {
            'visit_ids': visit_ids,
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/delGoodsVisit', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_delgoodscollect(cls, access_token):  # Author：web前端-邓晓桢
        """
        删除关注
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/json'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/delGoodsCollect', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_goodscollect(cls, access_token):  # Author：郑凯
        """
        我的收藏
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/json'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/goodsCollect', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_goodsvisit(cls, access_token):  # Author：wlybq
        """
        我的足迹
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/goodsVisit', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_nopasspay(cls, access_token, status, verify_code='string'):  # Author：liyong
        """
        设置免密支付
        :param access_token: token
        :param status: ['text', '1', 'number', '1 开启免密支付 0关闭免密支付']
        :param verify_code: ['text', '0', 'string', '手机验证码']
        :return:
        """
        headers['Content-Type'] = 'application/json'
        headers['access-token'] = access_token
        data = {
            'status': status,
            'verify_code': verify_code,
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/noPassPay', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_edituserinfo(cls, access_token):  # Author：web前端-邓晓桢
        """
        修改个人资料
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/json'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/editUserInfo', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_setpaypass(cls, access_token, paypass, verify_code=None):  # Author：liyong
        """
        设置支付密码
        :param access_token: token
        :param paypass: ['text', '1', '', '支付密码']
        :param verify_code: ['text', '0', '', '手机验证码']
        :return:
        """
        headers['Content-Type'] = 'application/json'
        headers['access-token'] = access_token
        data = {
            'paypass': paypass,
            'verify_code': verify_code,
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/setPaypass', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_setloginpass(cls, access_token, verify_code, loginpass):  # Author：wlybq
        """
        设置登录密码
        :param access_token: token
        :param verify_code: ['text', '1', '1026', '手机验证码']
        :param loginpass: ['text', '1', '4564564156156', '登录密码']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'verify_code': verify_code,
            'loginpass': loginpass,
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/setLoginpass', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_changemobile(cls, access_token, verify_code, mobile, scene, old_mobile, old_verify_code):  # Author：wlybq
        """
        更换手机号码
        :param access_token: token
        :param verify_code: ['text', '1', '1024', '手机验证码']
        :param mobile: ['text', '1', '13657719754', '手机号码']
        :param scene: ['text', '1', '1', '发送场景 传入4 更换手机号码']
        :param old_mobile: ['text', '1', '13657719754', '老的手机（1.3.x的新需求加的参数）']
        :param old_verify_code: ['text', '1', '2096', '老手机收到的验证码（1.3.x的新需求加的参数）']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'verify_code': verify_code,
            'mobile': mobile,
            'scene': scene,
            'old_mobile': old_mobile,
            'old_verify_code': old_verify_code,
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/changeMobile', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_helpcate(cls, access_token):  # Author：郑凯
        """
        帮助中心首页
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/helpCate', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_helpdetail(cls):  # Author：郑凯
        """
        帮助中心详情
        :return:
        """
        headers['Content-Type'] = 'application/json'
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/helpDetail', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_about(cls, access_token):  # Author：liyong
        """
        关于我们
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/about', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_bindleader(cls, access_token):  # Author：liyong
        """
        绑定导师
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/json'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/bindLeader', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_feedbacktype(cls, access_token, msg_type):  # Author：web前端-邓晓桢
        """
        提交问题反馈
        :param access_token: token
        :param msg_type: ['text', '1', None, None]
        :return:
        """
        headers['Content-Type'] = 'application/json'
        headers['access-token'] = access_token
        data = {
            'msg_type': msg_type,
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/feedbackType', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_feedback(cls, access_token):  # Author：web前端-邓晓桢
        """
        获取问题反馈类型
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/feedback', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_accountrecordsum(cls, access_token):  # Author：web前端-邓晓桢
        """
        账户汇总统计
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/json'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/accountRecordSum', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_getshareurl(cls, access_token):  # Author：liyong
        """
        邀请成为团长
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/json'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/getShareUrl', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_paycodelist(cls, access_token):  # Author：web前端-邓晓桢
        """
        纯码待支付列表
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/payCodeList', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def wallet_amount(cls, access_token):  # Author：liyong
        """
        钱包首页
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/json'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Wallet/amount', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def wallet_amountdetail(cls, access_token):  # Author：wyleLeung
        """
        钱包明细
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/json'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Wallet/amountDetail', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_chuncode(cls, access_token, is_used, page='1', is_order='1'):  # Author：wlybq
        """
        我的纯码
        :param access_token: token
        :param is_used: ['text', '1', '1', ' \t是否使用 1未使用 2已使用']
        :param page: ['text', '0', '1', ' \t默认1']
        :param is_order: ['text', '0', '1', ' \t默认1 如果是购买礼包过来的，传入2（不显示超级码）']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'is_used': is_used,
            'page': page,
            'is_order': is_order,
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/chunCode', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_waitpaycode(cls, access_token):  # Author：wlybq
        """
        检查有无待支付纯码
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/waitPayCode', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def wallet_authenticate(cls, access_token):  # Author：wyleLeung
        """
        个人认证
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/json'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Wallet/authenticate', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_account(cls, access_token):  # Author：郑凯
        """
        我的账户
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/json'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/account', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_accountrecord(cls):  # Author：郑凯
        """
        我的账户（余额明细）
        :return:
        """
        headers['Content-Type'] = 'application/json'
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/accountRecord', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def wallet_changbankcard(cls, access_token):  # Author：wyleLeung
        """
        检查银行卡是否有业务
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/json'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Wallet/changBankCard', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def wallet_idcardrecognition(cls, access_token):  # Author：web前端-邓晓桢
        """
        AI身份证图片识别
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/json'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Wallet/IDCardRecognition', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def wallet_idcardrecognitionback(cls, access_token):  # Author：wyleLeung
        """
        AI身份证国徽页图片识别
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/json'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Wallet/IDCardRecognitionBack', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def wallet_bankcardrecognition(cls, access_token):  # Author：web前端-邓晓桢
        """
        AI银行卡图片识别字符串
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/json'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Wallet/BankCardRecognition', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def wallet_bindbankcard(cls, access_token, bank_name, bank_username, bank_no, bank_mobile, yzm,
                            bank_id):  # Author：wlybq
        """
        绑定银行卡
        :param access_token: token
        :param bank_name: ['text', '1', '建设银行', '开户银行']
        :param bank_username: ['text', '1', '张三', '开户人']
        :param bank_no: ['text', '1', '641261561231526154', '银行卡号']
        :param bank_mobile: ['text', '1', '13657719754', '银行预留手机号']
        :param yzm: ['text', '1', '1645', '短信验证码']
        :param bank_id: ['text', '1', '1', ' \t换绑需要传银行列表id']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'bank_name': bank_name,
            'bank_username': bank_username,
            'bank_no': bank_no,
            'bank_mobile': bank_mobile,
            'yzm': yzm,
            'bank_id': bank_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Wallet/bindBankCard', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def wallet_cashout(cls, access_token, cashout_money, pay_password, yzm):  # Author：wlybq
        """
        提现
        :param access_token: token
        :param cashout_money: ['text', '1', '25000.00', '提现金额']
        :param pay_password: ['text', '1', '49454564', '支付密码']
        :param yzm: ['text', '1', '5654', '短信验证码']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'cashout_money': cashout_money,
            'pay_password': pay_password,
            'yzm': yzm,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Wallet/cashout', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def wallet_bankcardlist(cls, access_token):  # Author：郑凯
        """
        银行卡列表
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Wallet/bankCardList', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def wallet_userauthinfo(cls, access_token):  # Author：郑凯
        """
        个人认证信息
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Wallet/userAuthInfo', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def wallet_sendsms(cls, access_token):  # Author：liyong
        """
        钱包实名、绑卡短信验证码
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/json'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Wallet/sendSms', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def wallet_authsmsverify(cls, access_token):  # Author：liyong
        """
        实名窗口短信校验码验证
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/json'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Wallet/authSmsVerify', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_closepopup(cls, access_token):  # Author：郑凯
        """
        用户关闭弹窗提示
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/json'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/closePopup', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def share_reg(cls):  # Author：liyong
        """
        分享APP用户注册
        :return:
        """
        headers['Content-Type'] = 'application/json'
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Share/reg', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def share_createqrcode(cls, access_token):  # Author：郑凯
        """
        分享app获取海报
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Share/createQrcode', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def share_sendmsg(cls):  # Author：web前端-邓晓桢
        """
        分享APP下发短信
        :return:
        """
        headers['Content-Type'] = 'application/json'
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Share/sendMsg', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def share_userinfo(cls):  # Author：web前端-邓晓桢
        """
        分享APP用户信息
        :return:
        """
        headers['Content-Type'] = 'application/json'
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Share/userInfo', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_getdemotiontask(cls, access_token):  # Author：wlybq
        """
        团长降级审核任务获取接口
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/getDemotionTask', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_submitaudittask(cls, access_token, img1_url, img2_url):  # Author：wlybq
        """
        团长降级审核任务提交
        :param access_token: token
        :param img1_url: ['text', '1', 'https://images/xxxxx/ghadhkslangjka13u21.jpg', '第一张截图']
        :param img2_url: ['text', '1', 'https://images/xxxxx/ghadhkslangjka13gga.jpg', '第二张截图']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'img1_url': img1_url,
            'img2_url': img2_url,
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/submitAuditTask', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp


class WelfareSociety:
    @classmethod
    def welfaregoods_getlists(cls):  # Author：zyj
        """
        商品列表
        :return:
        """
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/WelfareGoods/getLists', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def welfaregoods_getmemberstatus(cls):  # Author：zyj
        """
        获取会员到期状态
        :return:
        """
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/WelfareGoods/getMemberStatus', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def welfaregoods_getjpgoodslists(cls):  # Author：zyj
        """
        获取弹窗商品列表
        :return:
        """
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/WelfareGoods/getJpGoodsLists', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def welfaregoods_getbuyloglists(cls):  # Author：zyj
        """
        获取购买记录列表
        :return:
        """
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/WelfareGoods/getBuyLogLists', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp


class LiveBroadcast:
    @classmethod
    def live_takegoods(cls, page='1', l_id='1', keyword='名称'):  # Author：18814188357@163.com
        """
        带货商品
        :param page: ['text', '0', '1', '分页(默认1)']
        :param l_id: ['text', '0', '1', '直播记录(用于商品列表修改直播商品)']
        :param keyword: ['text', '0', '名称', '商品名称']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'page': page,
            'l_id': l_id,
            'keyword': keyword,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Live/takeGoods', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def live_preplay(cls, title, content, cover, preplay_time, goods_ids):  # Author：18814188357@163.com
        """
        预播
        :param title: ['text', '1', None, '标题']
        :param content: ['text', '1', '', '内容']
        :param cover: ['text', '1', '', '封面']
        :param preplay_time: ['text', '1', '', '开播时间(时间戳)']
        :param goods_ids: ['text', '1', '[123,456]', '商品id（数组）']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'title': title,
            'content': content,
            'cover': cover,
            'preplay_time': preplay_time,
            'goods_ids': goods_ids,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Live/prePlay', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def live_cancel(cls, l_id):  # Author：18814188357@163.com
        """
        直播取消
        :param l_id: ['text', '1', '1', '直播记录id']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'l_id': l_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Live/cancel', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def live_start(cls, l_id):  # Author：18814188357@163.com
        """
        直播开始
        :param l_id: ['text', '1', '', '直播记录id']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'l_id': l_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Live/start', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def live_pause(cls, l_id):  # Author：18814188357@163.com
        """
        直播暂停
        :param l_id: ['text', '1', None, '直播记录id']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'l_id': l_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Live/pause', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def live_resume(cls, l_id):  # Author：18814188357@163.com
        """
        直播恢复
        :param l_id: ['text', '1', None, '直播记录id']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'l_id': l_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Live/resume', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def live_stop(cls, l_id):  # Author：18814188357@163.com
        """
        直播结束
        :param l_id: ['text', '1', None, '直播记录id']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'l_id': l_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Live/stop', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def live_sublists(cls, live_user_id, page=None):  # Author：18814188357@163.com
        """
        订阅直播列表
        :param live_user_id: ['text', '1', '', '订阅的主播id']
        :param page: ['text', '0', None, '分页(默认1)']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'live_user_id': live_user_id,
            'page': page,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Live/subLists', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def live_mylists(cls, search_type, page=None):  # Author：18814188357@163.com
        """
        我的直播列表
        :param search_type: ['text', '1', '', '筛选类型 plan-直播计划 record-历史记录']
        :param page: ['text', '0', '', '页码(默认1)']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'search_type': search_type,
            'page': page,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Live/myLists', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def live_detail(cls, l_id):  # Author：18814188357@163.com
        """
        直播详情
        :param l_id: ['text', '1', None, '直播记录id']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'l_id': l_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Live/detail', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def live_setadmin(cls, l_id, user_id, type=None):  # Author：18814188357@163.com
        """
        主播设置管理员
        :param l_id: ['text', '1', None, '直播记录id']
        :param user_id: ['text', '1', '', '备选管理员id']
        :param type: ['text', '0', '', '操作类型 0-取消 1-设置(默认)']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'l_id': l_id,
            'user_id': user_id,
            'type': type,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Live/setAdmin', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def live_subscribe(cls, live_user_id, type, l_id=None):  # Author：18814188357@163.com
        """
        用户订阅主播
        :param live_user_id: ['text', '1', '', '主播id']
        :param type: ['text', '1', '', '操作类型 0-取消 1-订阅(默认)']
        :param l_id: ['text', '0', None, '直播id，主播中心可不传']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'live_user_id': live_user_id,
            'type': type,
            'l_id': l_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Live/subscribe', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def live_kickout(cls, l_id, op_user_id, type):  # Author：18814188357@163.com
        """
        直播踢人
        :param l_id: ['text', '1', None, '直播id']
        :param op_user_id: ['text', '1', '', '被踢用户id']
        :param type: ['text', '1', '', '操作类型 0-取消 1-设置(默认)']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'l_id': l_id,
            'op_user_id': op_user_id,
            'type': type,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Live/kickOut', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def live_forbidtalk(cls, l_id, op_user_id, type):  # Author：18814188357@163.com
        """
        直播禁言
        :param l_id: ['text', '1', None, '直播id']
        :param op_user_id: ['text', '1', '', '被禁言用户id']
        :param type: ['text', '1', '', '操作类型 0-取消 1-设置(默认)']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'l_id': l_id,
            'op_user_id': op_user_id,
            'type': type,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Live/forbidTalk', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def live_blackbook(cls, l_id):  # Author：18814188357@163.com
        """
        直播黑名单
        :param l_id: ['text', '1', None, '直播id']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'l_id': l_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Live/blackBook', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def live_getimusersign(cls):  # Author：18814188357@163.com
        """
        获取IM用户签名(移动端直播sdk使用)
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Live/getIMUserSign', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def live_livecenter(cls):  # Author：18814188357@163.com
        """
        主播中心
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Live/liveCenter', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp


class NotificationMessage:
    @classmethod
    def message_setting(cls, access_token):  # Author：lihb
        """
        消息设置
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Message/setting', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def message_setswitch(cls, access_token, switch_type, is_open):  # Author：lihb
        """
        消息开关
        :param access_token: token
        :param switch_type: ['text', '1', '1', None]
        :param is_open: ['text', '1', '1', '']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'switch_type': switch_type,
            'is_open': is_open,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Message/setSwitch', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def message_index(cls, access_token):  # Author：lihb
        """
        获取消息列表
        :param access_token: token
        :return:
        """
        headers['access-token'] = access_token
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Message/index', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def message_detail(cls, access_token):  # Author：lihb
        """
        消息详情
        :param access_token: token
        :return:
        """
        headers['access-token'] = access_token
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Message/detail', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def message_del(cls, access_token):  # Author：lihb
        """
        删除消息
        :param access_token: token
        :return:
        """
        headers['access-token'] = access_token
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Message/del', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def message_read(cls):  # Author：lihb
        """
        读取消息
        :return:
        """
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Message/read', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def message_center(cls):  # Author：lihb
        """
        通知中心
        :return:
        """
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Message/center', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp


class LazyWelfare:
    @classmethod
    def welfare_index(cls, access_token):  # Author：hfc
        """
        1.懒人福利社落地页
        :param access_token: token
        :return:
        """
        headers['access-token'] = access_token
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Welfare/index', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def welfare_getentrance(cls, access_token):  # Author：hfc
        """
        2.福利社落地页入口
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Welfare/getEntrance', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def welfare_getshare(cls, access_token):  # Author：hfc
        """
        3.福利社h5分享
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Welfare/getShare', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def welfare_getposterparams(cls, access_token):  # Author：hfc
        """
        4.获取合成海报的参数
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Welfare/getPosterParams', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def lazy_getlazyurl(cls, access_token, route, idfa=None, imei=None):  # Author：hfc
        """
        5.获取福利社链接
        :param access_token: token
        :param route: ['text', '1', 'oil/home', '懒人福利社路由']
        :param idfa: ['text', '0', '', 'ios序列号(ios和安卓二选一,不填有默认值)']
        :param imei: ['text', '0', '', '安卓序列号(ios和安卓二选一,不填有默认值)']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'route': route,
            'idfa': idfa,
            'imei': imei,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Lazy/getLazyUrl', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def welfare_handlecard(cls, access_token):  # Author：hfc
        """
        6.获取福利社商品id
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Welfare/handleCard', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def welfare_getwhitelist(cls, access_token):  # Author：hfc
        """
        7.获取域名白名单
        :param access_token: token
        :return:
        """
        headers['access-token'] = access_token
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Welfare/getWhiteList', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def welfare_isvalid(cls, access_token):  # Author：hfc
        """
        8.判断是否福利社会员
        :param access_token: token
        :return:
        """
        headers['access-token'] = access_token
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Welfare/isValid', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def welfare_getwelfareurl(cls, access_token):  # Author：hfc
        """
        9.获取所有h5链接
        :param access_token: token
        :return:
        """
        headers['access-token'] = access_token
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Welfare/getWelfareUrl', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp


class HomePage:
    @classmethod
    def index_thematiclist(cls, thematic_id='2', goods_id='1903'):  # Author：文忠孝
        """
        专题列表
        :param thematic_id: ['text', '0', '2', '专题ID，默认0']
        :param goods_id: ['text', '0', '1903', '推荐的商品ID，默认0']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'thematic_id': thematic_id,
            'goods_id': goods_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/thematicList', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_index(cls):  # Author：文忠孝
        """
        首页
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/index', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_slider(cls, pid):  # Author：文忠孝
        """
        轮播图
        :param pid: ['text', '1', '537', '位置id']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'pid': pid,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/slider', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_headcate(cls):  # Author：文忠孝
        """
        首页头部分类
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/headCate', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_categorypage(cls, cid):  # Author：文忠孝
        """
        分类首页（品质生鲜）
        :param cid: ['text', '1', '15', '分类id']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'cid': cid,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/categoryPage', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_midcategory(cls, cid, goods_id='1899'):  # Author：文忠孝
        """
        精选分类
        :param cid: ['text', '1', '9', '导航ID']
        :param goods_id: ['text', '0', '1899', '预览商品id']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'cid': cid,
            'goods_id': goods_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/midCategory', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_message(cls, access_token):  # Author：文忠孝
        """
        我的消息
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/message', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_brand_index_list(cls):  # Author：文忠孝
        """
        首页品牌大促
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/brand_index_list', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_midcategoryv2(cls, cid, tag_id, goods_id):  # Author：文忠孝
        """
        精选分类V2(单独获取商品信息)
        :param cid: ['text', '1', '44', '导航ID']
        :param tag_id: ['text', '1', '', '分类id，默认全部']
        :param goods_id: ['text', '1', '', '预览商品id']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'cid': cid,
            'tag_id': tag_id,
            'goods_id': goods_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/midCategoryV2', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_midcategorytag(cls, cid):  # Author：文忠孝
        """
        精选分类标签
        :param cid: ['text', '1', '94', '导航id']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'cid': cid,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/midCategoryTag', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_hometaskpopup(cls):  # Author：文忠孝
        """
        降级任务弹窗
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/homeTaskPopup', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_indexv2(cls):  # Author：文忠孝
        """
        首页V2
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/indexV2', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_indexunlimitedgoods(cls, page='1'):  # Author：文忠孝
        """
        首页无限商品列表
        :param page: ['text', '0', '1', '分页，默认为1']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'page': page,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/indexUnlimitedGoods', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_indexgroupmsg(cls):  # Author：文忠孝
        """
        首页开团信息
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/indexGroupMsg', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_getbarrage(cls, type='0'):  # Author：文忠孝
        """
        获取弹幕
        :param type: ['text', '0', '0', '弹幕类型 0-默认所有 1-普通商品 2-抢购']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'type': type,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/getBarrage', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_testpay(cls, order_id, extension_code):  # Author：TZK
        """
        虚拟支付
        :param order_id: ['text', '1', '0', '']
        :param extension_code: ['text', '1', '', '']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'order_id': order_id,
            'extension_code': extension_code,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/testpay', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_gethomeshare(cls):  # Author：18814188357@163.com
        """
        首页分享
        :return:
        """
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Index/getHomeShare', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp


class Commodity:
    @classmethod
    def goods_newcategory(cls):  # Author：TZK
        """
        1.分类
        :return:
        """
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Goods/newCategory', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def goods_catepage(cls):  # Author：TZK
        """
        2.分类分页
        :return:
        """
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Goods/catePage', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def goods_index(cls):  # Author：TZK
        """
        3.搜索结果（商品列表）
        :return:
        """
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Goods/index', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def goods_detail(cls):  # Author：zyj
        """
        4.商品详情（普通商品）
        :return:
        """
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Goods/detail', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_guess(cls, access_token):  # Author：TZK
        """
        5.猜你喜欢（搜索页）
        :param access_token: token
        :return:
        """
        headers['access-token'] = access_token
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Index/guess', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def goods_flashdetail(cls):  # Author：TZK
        """
        6.商品详情（抢购）
        :return:
        """
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Goods/flashDetail', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def goods_commentlist(cls):  # Author：TZK
        """
        7.商品评论列表
        :return:
        """
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Goods/commentList', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def goods_collect(cls, access_token, goods_id):  # Author：TZK
        """
        8.收藏商品
        :param access_token: token
        :param goods_id: ['text', '1', None, '商品ID']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'goods_id': goods_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Goods/collect', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def goods_brandpage(cls, access_token, id):  # Author：TZK
        """
        9.品牌首页
        :param access_token: token
        :param id: ['text', '1', None, '品牌ID']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'id': id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Goods/brandPage', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def goods_brandpage_1586418000143(cls, access_token, id):  # Author：TZK
        """
        9.品牌首页_copy
        :param access_token: token
        :param id: ['text', '1', None, '品牌ID']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'id': id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Goods/brandPage_1586418000143', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp


class ShoppingCart:
    @classmethod
    def cart_addcart(cls, access_token, goods_id, goods_num, item_id):  # Author：lihb
        """
         1.加入购物车
        :param access_token: token
        :param goods_id: ['text', '1', '1780', None]
        :param goods_num: ['text', '1', '1', '']
        :param item_id: ['text', '1', '4721', '']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'goods_id': goods_id,
            'goods_num': goods_num,
            'item_id': item_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Cart/addCart', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def cart_changenum(cls, access_token, cart_id, goods_num):  # Author：lihb
        """
        2.改变购物车商品数量
        :param access_token: token
        :param cart_id: ['text', '1', '302328', None]
        :param goods_num: ['text', '1', '2', '']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'cart_id': cart_id,
            'goods_num': goods_num,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Cart/changeNum', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def cart_index(cls, access_token):  # Author：lihb
        """
        3.我的购物车
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Cart/index', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def cart_delcart(cls, access_token):  # Author：lihb
        """
        4.删除购物车内容
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Cart/delCart', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_favourite(cls, access_token):  # Author：lihb
        """
        5.猜你喜欢
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Index/favourite', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_addresslist(cls):  # Author：lihb
        """
        6.我的地址
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/User/addressList', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_addaddress(cls, access_token, consignee, province, city, district, address, mobile, label,
                        address_id):  # Author：lihb
        """
        7.新增/编辑地址
        :param access_token: token
        :param consignee: ['text', '1', None, None]
        :param province: ['text', '1', '', '']
        :param city: ['text', '1', '', '']
        :param district: ['text', '1', '', '']
        :param address: ['text', '1', '', '']
        :param mobile: ['text', '1', '', '']
        :param label: ['text', '1', '', '']
        :param address_id: ['text', '1', '', '']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'consignee': consignee,
            'province': province,
            'city': city,
            'district': district,
            'address': address,
            'mobile': mobile,
            'label': label,
            'address_id': address_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/addAddress', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_deladdress(cls, access_token, address_id):  # Author：lihb
        """
        8.删除地址
        :param access_token: token
        :param address_id: ['text', '1', '', None]
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'address_id': address_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/delAddress', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_setdefaultaddress(cls, access_token, address_id):  # Author：lihb
        """
        9.设置为默认地址
        :param access_token: token
        :param address_id: ['text', '1', '10', None]
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'address_id': address_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/setDefaultAddress', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_addresslabel(cls, access_token):  # Author：lihb
        """
        10.地址标签
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/User/addressLabel', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_addaddresslabel(cls, access_token, name, id):  # Author：lihb
        """
        11.新增/编辑 地址标签
        :param access_token: token
        :param name: ['text', '1', 'school', None]
        :param id: ['text', '1', '10086', '']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'name': name,
            'id': id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/addAddressLabel', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def user_deladdresslabel(cls, access_token, id):  # Author：lihb
        """
        12.删除 地址标签
        :param access_token: token
        :param id: ['text', '1', '10086', None]
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'id': id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/User/delAddressLabel', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def cart_getaddress(cls, access_token):  # Author：lihb
        """
        13.获取地址信息（确认订单）
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Cart/getAddress', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def cart_submitorder(cls, access_token, address_id, goods_id, goods_num, act='get_price', action='buy_cart',
                         flash_sale_id=None):  # Author：lihb
        """
        14.提交订单/获取订单价格
        :param access_token: token
        :param address_id: ['text', '1', '540785', None]
        :param goods_id: ['text', '1', '', '']
        :param goods_num: ['text', '1', '', '']
        :param act: ['text', '0', 'get_price', '']
        :param action: ['text', '0', 'buy_cart', '']
        :param flash_sale_id: ['text', '0', '', '']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'address_id': address_id,
            'goods_id': goods_id,
            'goods_num': goods_num,
            'act': act,
            'action': action,
            'flash_sale_id': flash_sale_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Cart/submitOrder', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def cart_setcartgoods(cls, access_token, cart_ids):  # Author：lihb
        """
        15.确认订单2
        :param access_token: token
        :param cart_ids: ['text', '1', None, None]
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'cart_ids': cart_ids,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Cart/setCartGoods', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def cart_getcartnum(cls, access_token):  # Author：lihb
        """
        16.获取购物车商品数量
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Cart/getCartNum', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def address_matchaddress(cls, access_token, address):  # Author：haojin
        """
        17.地址匹配
        :param access_token: token
        :param address: ['text', '1', '北京市市辖区朝阳区北苑路甲13号北辰泰岳大厦，15914534628', '匹配地址']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'address': address,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Address/matchAddress', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def cart_checkpromgoods(cls):  # Author：lihb
        """
        18.检查活动商品状态
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Cart/checkPromGoods', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp


class Order:
    @classmethod
    def order_orderlist(cls, access_token, type='0'):  # Author：李青
        """
        1.我的订单列表
        :param access_token: token
        :param type: ['text', '0', '0', '0 全部 1待付款 2待发货 3已发货 4待评论 5已退款 6拒绝退款 7申请退款 8退款/售后']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'type': type,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Order/orderList', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def order_orderdetail(cls, access_token, order_id):  # Author：李青
        """
        2.订单详情
        :param access_token: token
        :param order_id: ['text', '1', '41513', None]
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'order_id': order_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Order/orderDetail', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def order_cancelorder(cls, access_token, order_id):  # Author：李青
        """
        3.取消订单
        :param access_token: token
        :param order_id: ['text', '1', '46803', None]
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'order_id': order_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Order/cancelOrder', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def order_delorder(cls, access_token, order_id):  # Author：李青
        """
        4.删除订单
        :param access_token: token
        :param order_id: ['text', '1', '43490', None]
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'order_id': order_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Order/delOrder', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def order_confirmorder(cls, access_token, order_id):  # Author：李青
        """
        5.确认收货
        :param access_token: token
        :param order_id: ['text', '1', '43379', None]
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'order_id': order_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Order/confirmOrder', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def order_editaddress(cls, access_token, order_id, consignee, mobile, province, city, district,
                          address):  # Author：李青
        """
        6.编辑订单收货信息
        :param access_token: token
        :param order_id: ['text', '1', '19799', None]
        :param consignee: ['text', '1', '李先生', '']
        :param mobile: ['text', '1', '13212345678', '']
        :param province: ['text', '1', '广东省', '']
        :param city: ['text', '1', '广州市', '']
        :param district: ['text', '1', '天河区', '']
        :param address: ['text', '1', '中和广场31楼', '']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'order_id': order_id,
            'consignee': consignee,
            'mobile': mobile,
            'province': province,
            'city': city,
            'district': district,
            'address': address,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Order/editAddress', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def order_refund(cls, access_token, order_id, reason, info, refund_mobile, refund_money):  # Author：李青
        """
        7.申请退款
        :param access_token: token
        :param order_id: ['text', '1', '41506', '订单id']
        :param reason: ['text', '1', '不想要了', '退款原因']
        :param info: ['text', '1', '就是不想要了', '退款说明']
        :param refund_mobile: ['text', '1', '18522225678', '手机号']
        :param refund_money: ['text', '1', '0.01', '退款金额']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'order_id': order_id,
            'reason': reason,
            'info': info,
            'refund_mobile': refund_mobile,
            'refund_money': refund_money,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Order/refund', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def order_expresscompany(cls, access_token, order_id):  # Author：haojin
        """
        8.通过单号获取快递公司
        :param access_token: token
        :param order_id: ['text', '1', '43595', '订单id']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'order_id': order_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Order/expressCompany', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def order_expresscompanysimplename(cls, access_token, company):  # Author：haojin
        """
        9.获取快递公司简称
        :param access_token: token
        :param company: ['text', '1', '韵达', '快递公司名称']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'company': company,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Order/expressCompanySimpleName', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def order_logisticsinfo(cls, access_token, order_id, invoice_no):  # Author：haojin
        """
        10.获取物流信息
        :param access_token: token
        :param order_id: ['text', '1', '43432', '订单id']
        :param invoice_no: ['text', '1', '651313213213', '物流单号']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'order_id': order_id,
            'invoice_no': invoice_no,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Order/logisticsInfo', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def order_ordernum(cls, access_token):  # Author：李青
        """
        11.我的订单数量（我的-待付款，待发货，待收货）
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Order/orderNum', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def aftersale_applytype(cls, access_token):  # Author：李青
        """
        12.客户申请售后类型
        :param access_token: token
        :return:
        """
        headers['access-token'] = access_token
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Aftersale/applyType', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def aftersale_applyprocess(cls, access_token, order_id):  # Author：李青
        """
        13.售后消息列表
        :param access_token: token
        :param order_id: ['text', '1', '46781', None]
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'order_id': order_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Aftersale/applyProcess', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def aftersale_apply(cls, access_token, order_id, goods_status, type, reason_id, explain=None,
                        evidence=None):  # Author：李青
        """
        14.客户售后申请
        :param access_token: token
        :param order_id: ['text', '1', '15394', None]
        :param goods_status: ['text', '1', '1', '']
        :param type: ['text', '1', '1', '']
        :param reason_id: ['text', '1', '1', '']
        :param explain: ['text', '0', '', '']
        :param evidence: ['text', '0', '', '']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'order_id': order_id,
            'goods_status': goods_status,
            'type': type,
            'reason_id': reason_id,
            'explain': explain,
            'evidence': evidence,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Aftersale/apply', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def aftersale_applyinvoiceno(cls, access_token, order_id, invoice_no, express_name='申通快递', express_price='6.3',
                                 alipay_name='支付宝姓名', alipay_account='支付宝账号'):  # Author：李青
        """
        15.售后-录入退换货单号
        :param access_token: token
        :param order_id: ['text', '1', '16388', None]
        :param invoice_no: ['text', '1', '3344444545464254', '']
        :param express_name: ['text', '0', '申通快递', '']
        :param express_price: ['text', '0', '6.3', '']
        :param alipay_name: ['text', '0', '支付宝姓名', '']
        :param alipay_account: ['text', '0', '支付宝账号', '']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'order_id': order_id,
            'invoice_no': invoice_no,
            'express_name': express_name,
            'express_price': express_price,
            'alipay_name': alipay_name,
            'alipay_account': alipay_account,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Aftersale/applyInvoiceNo', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def order_getoverseasauth(cls, access_token):  # Author：李青
        """
        16.全球购实名信息
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Order/getOverseasAuth', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def order_overseasauth(cls, access_token, realname, id_card, order_id='16388'):  # Author：李青
        """
        17.全球购实名(目前只支持大陆证件)
        :param access_token: token
        :param realname: ['text', '1', '小狗', '证件姓名']
        :param id_card: ['text', '1', '431002564578965412', '证件号']
        :param order_id: ['text', '0', '16388', '(修改未支付订单实名信息时)']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'realname': realname,
            'id_card': id_card,
            'order_id': order_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Order/OverseasAuth', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp


class Payment:
    @classmethod
    def pay_info(cls, access_token, order_id, mode, pay_way='appPay', pay_pass='123456', pay_what='order', openid=None,
                 pay_name=None, return_url=None):  # Author：李青
        """
        1.获取支付信息/余额支付
        :param access_token: token
        :param order_id: ['text', '1', '46815', '订单ID']
        :param mode: ['text', '1', 'alipay', '支付方式 wechat 微信支付/汇聚支付 alipay 支付宝 user_money_pay 余额支付,新版本传（api/pay/payList接口返回的pay_code）']
        :param pay_way: ['text', '0', 'appPay', '支付方式 appPay,jssdkpay （汇聚支付传appPay）,有数支付APPmppay，有数小程序传minipay，h5传jspay']
        :param pay_pass: ['text', '0', '123456', '支付密码 如果是余额支付，需要提供支付密码(暂时未用到)']
        :param pay_what: ['text', '0', 'order', '默认‘order’商品订单支付 纯码支付 ‘chun_code’']
        :param openid: ['text', '0', '', 'pay_way=jssdkpay时，必传']
        :param pay_name: ['text', '0', '', '公司名（api/pay/payList接口返回的）']
        :param return_url: ['text', '0', '', '有数H5支付之后跳转的URL地址']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'order_id': order_id,
            'mode': mode,
            'pay_way': pay_way,
            'pay_pass': pay_pass,
            'pay_what': pay_what,
            'openid': openid,
            'pay_name': pay_name,
            'return_url': return_url,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Pay/info', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def pay_notify(cls):  # Author：李青
        """
        2.微信/支付宝官方支付支付回调
        :return:
        """
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Pay/notify', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def pay_paylist(cls, pay_type):  # Author：李青
        """
        3.支付列表
        :param pay_type: ['text', '1', 'appPay', '支付方式： app支付-appPay,网页支付-jssdkpay （汇聚支付传appPay）,minipay-小程序支付']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'pay_type': pay_type,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Pay/payList', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def pay_jsapipaydisplay(cls):  # Author：李青
        """
        4.防封公众号支付页面
        :return:
        """
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Pay/jsapiPayDisplay', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def pay_youthsgetappid(cls):  # Author：haojin
        """
        5.获取有数支付appid
        :return:
        """
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Pay/youthsGetAppid', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp


class EquityCenter:
    @classmethod
    def equity_slider(cls, access_token):  # Author：MikeLue
        """
        权益中心轮播图
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/Equity/slider', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def equity_goodslist(cls, access_token, page='1'):  # Author：MikeLue
        """
        权益中心商品
        :param access_token: token
        :param page: ['text', '0', '1', '页数']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'page': page,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Equity/goodsList', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def equity_goodsdetail(cls, id):  # Author：MikeLue
        """
        权益中心商品详情
        :param id: ['text', '1', '111', '商品ID']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'id': id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Equity/goodsDetail', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp


class WechatRelated:
    @classmethod
    def wx_auth(cls):  # Author：haojin
        """
        0.微信公众号授权
        :return:
        """
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/Wx/auth', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_wxcodetoaccess(cls, code):  # Author：haojin
        """
        1.获取微信accesstoken
        :param code: ['text', '1', 'gsdgeswgfdsgd', '授权获取的code']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'code': code,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/wxCodeToAccess', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def index_wxgetuserinfo(cls, openid, access_token):  # Author：haojin
        """
        2.拉取用户信息
        :param openid: ['text', '1', 'sfsadfsdaf', '用户opneid']
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'openid': openid,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Index/wxGetUserInfo', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def wx_minilogin(cls, js_code, iv, encrypted_data, invite_code, platform):  # Author：haojin
        """
        3.小程序授权登录
        :param js_code: ['text', '1', None, '授权码']
        :param iv: ['text', '1', '', '手机号iv加密算法向量']
        :param encrypted_data: ['text', '1', '', '手机号加密数据']
        :param invite_code: ['text', '1', '', '邀请码']
        :param platform: ['text', '1', 'live', '小程序渠道 live-直播 shop-商城']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'js_code': js_code,
            'iv': iv,
            'encrypted_data': encrypted_data,
            'invite_code': invite_code,
            'platform': platform,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Wx/miniLogin', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def wx_miniperfectinfo(cls, js_code, mobile, iv, encrypted_data, platform):  # Author：haojin
        """
        4.小程序完善信息
        :param js_code: ['text', '1', 'efdv', '授权码']
        :param mobile: ['text', '1', '12314534628', '手机号']
        :param iv: ['text', '1', '122', '微信用户iv加密算法向量']
        :param encrypted_data: ['text', '1', 'assfsdafsadfsdaf', '微信用户加密数据']
        :param platform: ['text', '1', 'live', '小程序渠道 live-直播 shop-商城']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'js_code': js_code,
            'mobile': mobile,
            'iv': iv,
            'encrypted_data': encrypted_data,
            'platform': platform,
        }
        r = requests.post(api_host + '/index.php' + '/Api/Wx/miniPerfectInfo', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp


class TeamManagement:
    @classmethod
    def teammanage_todayperformance(cls, access_token):  # Author：haojin
        """
        1.今日业绩
        :param access_token: token
        :return:
        """
        headers['access-token'] = access_token
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/TeamManage/todayPerformance', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def teammanage_goodssaleanalyze(cls, access_token):  # Author：haojin
        """
        2.首页商品销量分析
        :param access_token: token
        :return:
        """
        headers['access-token'] = access_token
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/TeamManage/goodsSaleAnalyze', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def teammanage_teamsaleanalyze(cls, access_token):  # Author：haojin
        """
        3.首页团队销售分析
        :param access_token: token
        :return:
        """
        headers['access-token'] = access_token
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/TeamManage/teamSaleAnalyze', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def teammanage_goodssaleanalyzedetail(cls, access_token, time_type, type, page, start_time='2020-02-10',
                                          end_time='2020-02-20'):  # Author：haojin
        """
        4。商品销量分析
        :param access_token: token
        :param time_type: ['text', '1', '0', '时间 今日实时：0，昨日：1，7日：2，30日：3，自定义：4']
        :param type: ['text', '1', 'sale_num', '排行榜 商品榜：sale_num， 成交额：sale_money, 退货商品：refund_num']
        :param page: ['text', '1', '1', '分页']
        :param start_time: ['text', '0', '2020-02-10', 'time_type=4 时必传 ,开始时间， 例如：2020-02-10']
        :param end_time: ['text', '0', '2020-02-20', 'time_type=4 时必传 ,开始时间， 例如：2020-02-10']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'time_type': time_type,
            'type': type,
            'page': page,
            'start_time': start_time,
            'end_time': end_time,
        }
        r = requests.post(api_host + '/index.php' + '/Api/TeamManage/goodsSaleAnalyzeDetail', headers=headers,
                          data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def teammanage_getusergoodssalelist(cls, access_token, time_type, type, goods_id, order='0'):  # Author：haojin
        """
        5.查看团队成员销售情况
        :param access_token: token
        :param time_type: ['text', '1', '0', '时间范围']
        :param type: ['text', '1', 'sale_num ', '\tsale_num 销量，sale_money 金额，refund_num 退款数，refund_money 退款金额']
        :param goods_id: ['text', '1', '3213', '\t商品id']
        :param order: ['text', '0', '0', '排序，默认又多到少 1正序， 0 或者不传 倒序']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'time_type': time_type,
            'type': type,
            'goods_id': goods_id,
            'order': order,
        }
        r = requests.post(api_host + '/index.php' + '/Api/TeamManage/getUserGoodsSaleList', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def teammanage_searchgoods(cls, access_token, goods_name, goods_id='123'):  # Author：haojin
        """
        6.搜索商品
        :param access_token: token
        :param goods_name: ['text', '1', 'gdsgds', '\t商品名']
        :param goods_id: ['text', '0', '123', '商品id,优先以商品id查询，两个参数必传一个']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'goods_name': goods_name,
            'goods_id': goods_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/TeamManage/searchGoods', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def teammanage_teamsaleanalyzedetail(cls, access_token, time_type, type, start_time, end_time, page,
                                         order):  # Author：haojin
        """
        7.团队销售分析
        :param access_token: token
        :param time_type: ['text', '1', '0', '\t时间 今日实时：0，昨日：1，7日：2，30日：3，自定义：4']
        :param type: ['text', '1', 'sale_money', '排行榜 商品榜：sale_num， 成交额：sale_money']
        :param start_time: ['text', '1', '2020-02-10', '\ttime_type=4 时必传 ,开始时间， 例如：2020-02-10']
        :param end_time: ['text', '1', '2020-02-10', 'time_type=4 时必传 ，结束时间，例如：2020-02-10']
        :param page: ['text', '1', '1', '第几页']
        :param order: ['text', '1', '0', '排序，默认倒序， 1正序， 0 或者不传 倒序']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'time_type': time_type,
            'type': type,
            'start_time': start_time,
            'end_time': end_time,
            'page': page,
            'order': order,
        }
        r = requests.post(api_host + '/index.php' + '/Api/TeamManage/teamSaleAnalyzeDetail', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def teammanage_getteamgoodssalelist(cls, access_token, user_id, type, page, order='0'):  # Author：haojin
        """
        8.查看商品销售情况
        :param access_token: token
        :param user_id: ['text', '1', '12313', '\t用户id']
        :param type: ['text', '1', 'sale_num', '排行榜 商品榜：sale_num， 成交额：sale_money']
        :param page: ['text', '1', '1', '页数']
        :param order: ['text', '0', '0', '排序，默认倒序， 1正序， 0 或者不传 倒序']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'user_id': user_id,
            'type': type,
            'page': page,
            'order': order,
        }
        r = requests.post(api_host + '/index.php' + '/Api/TeamManage/getTeamGoodsSaleList', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def teammanage_sumsaleandrefund(cls, access_token, type, date):  # Author：haojin
        """
        9.销退货汇总
        :param access_token: token
        :param type: ['text', '1', '0', '汇总类型 日汇总：0， 月汇总：1']
        :param date: ['text', '1', '2020-03', '时间，例如：type=0时传YYYY-mm， type=1时传YYYY']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'type': type,
            'date': date,
        }
        r = requests.post(api_host + '/index.php' + '/Api/TeamManage/sumSaleAndRefund', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def teammanage_team(cls, access_token):  # Author：haojin
        """
        10.团队
        :param access_token: token
        :return:
        """
        headers['access-token'] = access_token
        data = {
        }
        r = requests.get(api_host + '/index.php' + '/Api/TeamManage/team', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def teammanage_getmemberinfo(cls, access_token, user_id):  # Author：haojin
        """
        11.查看团员详情
        :param access_token: token
        :param user_id: ['text', '1', '43267', '团员id']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'user_id': user_id,
        }
        r = requests.post(api_host + '/index.php' + '/Api/TeamManage/getMemberInfo', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def teammanage_ordermanage(cls, access_token, type, status):  # Author：haojin
        """
        12,订单管理
        :param access_token: token
        :param type: ['text', '1', '0', '我的订单：0， 下级订单：1']
        :param status: ['text', '1', '0', '进行中：0，已完成：1，已关闭：2']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'type': type,
            'status': status,
        }
        r = requests.post(api_host + '/index.php' + '/Api/TeamManage/orderManage', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def teammanage_searchorders(cls, access_token, keyword):  # Author：haojin
        """
        13。搜索订单
        :param access_token: token
        :param keyword: ['text', '1', '1312', '订单编号或者商品名称']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'keyword': keyword,
        }
        r = requests.post(api_host + '/index.php' + '/Api/TeamManage/searchOrders', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def teammanage_newmember(cls, access_token, time_type, start_time='2020-02-10',
                             end_time='2020-02-10'):  # Author：haojin
        """
        14.新增人数
        :param access_token: token
        :param time_type: ['text', '1', '0', '今日实时：0，昨日：1，7日：2，30日：3，自定义：4']
        :param start_time: ['text', '0', '2020-02-10', 'time_type=4 时必传 ,开始时间， 例如：2020-02-10']
        :param end_time: ['text', '0', '2020-02-10', 'time_type=4 时必传 ，结束时间，例如：2020-02-10']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'time_type': time_type,
            'start_time': start_time,
            'end_time': end_time,
        }
        r = requests.post(api_host + '/index.php' + '/Api/TeamManage/newMember', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def teammanage_waitaudit(cls, access_token):  # Author：haojin
        """
        15，待审核任务总数
        :param access_token: token
        :return:
        """
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/TeamManage/waitAudit', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def teammanage_waitauditlist(cls, access_token, page):  # Author：haojin
        """
        16，待审核任务列表
        :param access_token: token
        :param page: ['text', '1', '1', '页数']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'page': page,
        }
        r = requests.post(api_host + '/index.php' + '/Api/TeamManage/waitAuditList', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def teammanage_audittask(cls, access_token, id, audit_status, remarks):  # Author：haojin
        """
        17，审核任务
        :param access_token: token
        :param id: ['text', '1', '1', '任务id']
        :param audit_status: ['text', '1', '2', '通过：2，不通过：3']
        :param remarks: ['text', '1', 'afdsdafsa', '备注']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
            'id': id,
            'audit_status': audit_status,
            'remarks': remarks,
        }
        r = requests.post(api_host + '/index.php' + '/Api/TeamManage/auditTask', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def teammanage_isshare(cls, access_token):  # Author：haojin
        """
        18，分享设置
        :param access_token: token
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['access-token'] = access_token
        data = {
        }
        r = requests.post(api_host + '/index.php' + '/Api/TeamManage/isShare', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def teammanage_fans(cls, type, page):  # Author：haojin
        """
        19,我的粉丝
        :param type: ['text', '1', '1', '1直邀，2团长']
        :param page: ['text', '1', '1', '第几页']
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'type': type,
            'page': page,
        }
        r = requests.post(api_host + '/index.php' + '/Api/TeamManage/fans', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp

    @classmethod
    def teammanage_searchfans(cls, keyword):  # Author：haojin
        """
        20,搜索粉丝
        :param keyword: ['text', '1', '18594902906', None]
        :return:
        """
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {
            'keyword': keyword,
        }
        r = requests.post(api_host + '/index.php' + '/Api/teamManage/searchFans', headers=headers, data=data)
        status = r.status_code
        resp = r.text
        resp = json.loads(resp)
        print(status)
        print(resp)
        return resp
