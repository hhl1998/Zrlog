import requests
from utils.logutil import logger

# 定义HTTP请求类
class RequestSend:
    # 封装requests请求函数
    def api_run(self, url, method, data=None, headers=None, cookies=None):
        # 定义变量，获取响应结果
        res = None
        # 打印日志
        logger.info("请求的url为{},类型为{}".format(url, type(url)))
        logger.info("请求的method为{},类型为{}".format(method, type(method)))
        logger.info("请求的data为{},类型为{}".format(headers, type(headers)))
        logger.info("请求的cookies为{}，类型为{}".format(cookies, type(cookies)))
        # 判断请求方法
        if method == "get":
            # 如果是get方法，则执行下列命令，发送HTTP请求，方法为get
            res=requests.get(url, data=data, headers=headers, cookies=cookies)
        elif method == "post":
            # 判断请求的数据类型是否为json格式
            if headers == {"Content-Type": "application/json"}:
                # 发送HTTP请求，方法为post，参数使用为json=data
                res=requests.post(url, json=data, headers=headers,
                                  cookies=cookies)
            elif headers == {"Content-Type":"application/x-www-form-urlencoded"}:
                # 发送HTTP请求，方法为post，参数使用为data=data
                res=requests.post(url, data=data, headers=headers,
                                  cookies=cookies)
        # 获取请求响应状态码
        code = res.status_code
        # 获取请求响应中的cookies
        cookies = res.cookies.get_dict()
        # 定义字典
        dict1 = dict()
        # 异常处理
        try:
            # 获取响应结果json格式
            body = res.json()
        # 捕获异常
        except:
            # 获取响应结果text格式
            body = res.text
        # 自定义参数code写入字典
        dict1['code'] = code
        # 自定义参数body写入字典
        dict1['body'] = body
        # 自定义参数cookies写入字典
        dict1['cookies'] = cookies
        # 返回自定义字典
        return dict1

    # 对外调用方法，**kwargs传入参数是dict类型
    def send(self, url, method, **kwargs):
        # 调用自定义方法
        return self.api_run(url=url, method=method, **kwargs)


if __name__ == '__main__':
    url = "http://192.168.217.130/zrlog/admin/login"
    data = {"username": "admin", "password": "akg", "https": False,
            "key": 1606792942688}
    method = "post"
    headers = {"Content-Type":"application/json"}
    print(RequestSend().send(url=url, method=method, headers=headers,
                             data=data))