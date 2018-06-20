'''
URLError的使用
'''

from urllib import request,error

if __name__ == '__main__':
    url = 'www.baiiiiiiiidu.com'

    try:
        # 构建实例
        req = request.Request(url)
        # 打开实例
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print("HTTPError:{0}".format(e.reason))
        print("HTTPError:{0}".format(e))

    except error.URLError as e:
        print("URLError:{0}".format(e.reason))
        print("URLError:{0}".format(e))

    except Exception as e:
        print(e)