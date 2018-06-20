from urllib import request,parse
from http import cookiejar

# 创建cookiejar实例
cookie = cookiejar.MozillaCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# 生成cookie的管理器
cookie_handler =request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()
# 创建https管理器
https_handler = request.HTTPSHandler()
# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)
# 创建登录函数

def getHomePage():
    url = 'http://www.renren.com/966348817/profile'

    # 如果已经执行了login函数，则opener自动已经包含相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()
    print(html)

if __name__ == '__main__':
    getHomePage()
