from urllib import request,parse
from http import cookiejar

# 创建filecookiejar实例
filename = 'cookie.txt'
cookie = cookiejar.MozillaCookieJar(filename)
# 生成cookie的管理器
cookie_handler =request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()
# 创建https管理器
https_handler = request.HTTPSHandler()
# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)
# 创建登录函数
def login():
    '''
    负责初次登录
    需要输入用户名密码，用来获取登录cookie凭证
    :return:
    '''
    # 此url需要从登录form的action中提取
    url = 'http://www.renren.com/PLogin.do'

    # 此键值需要从登录form的两个对应input中提取name属性
    data = {
        'email' : '18318108708',
        'password' : '234567'
    }
    # 把数据进行编码
    data = parse.urlencode(data)
    #  构建实例
    req = request.Request(url, data = data.encode())
    # 使用opener发起请求
    rsp = opener.open(req)
    # 保存cookie到文件
    # ignore_discard表示即使cookie将要被丢弃，也要保存下来
    # ignore_expires表示该文件中的cookie即使过期，也要保存下来
    cookie.save(ignore_discard=True,ignore_expires=True)

if __name__ == '__main__':
    login()
