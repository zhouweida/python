from urllib import request,parse
'''
掌握对url进行参数编码的方法
需要使用parse模块
'''
if __name__ == '__main__':
    #url格式：http//www.baidu.com/s?wd=大熊猫
    url = "http://www.baidu.com/s?"
    wd = input("Input your keyword:")
    qs = {
        "wd": wd
    }
    qs = parse.urlencode(qs)
    print(qs)
    fullurl = url + qs
    print(fullurl)
    rsp = request.urlopen(fullurl)
    html = rsp.read()
    html = html.decode()
    print(html)