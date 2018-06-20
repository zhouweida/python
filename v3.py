import urllib
import chardet
if __name__ == '__main__':
    url = "https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E4%B8%8A%E6%B5%B7&kw=python&sm=0&p=1"
    rsp = urllib.request.urlopen(url)
    print("url:{0}".format(rsp.geturl()))
    print("info:{0}",format(rsp.info()))
    print("code:{0}",format(rsp.getcode()))
    html = rsp.read()
    #利用chardet自动检测
    cs = chardet.detect(html)
    #使用get取值保证不去出错
    html = html.decode(cs.get("encoding","utf-8"))
    print(html)