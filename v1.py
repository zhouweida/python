from urllib import request
'''
使用urllib.request请求一个网页内容，并把内容打印出来
'''
if __name__ == '__main__':
    url = "https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E4%B8%8A%E6%B5%B7&kw=python&sm=0&p=1"
    #打开相应的url并把相应页面作为返回
    rsp = request.urlopen(url)
    #把返回的结果读取出来
    html = rsp.read()
    #如果想要把bytes内容转成字符串，需要解码
    html = html.decode()
    print(type(html))
    print(html)