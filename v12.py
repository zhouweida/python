from urllib import request

if __name__ == '__main__':
    url = 'https://www.zhihu.com/people/edit'

    headers = {
        'Cookie' : 'q_c1=38d67605fc744af09c8b0c37ce2477be|1525747650000|1525747650000; _zap=bb75b5d9-5b1c-4a33-81d2-6bdfe0b5bc44; z_c0="2|1:0|10:1525762823|4:z_c0|80:MS4xWG1qOUJRQUFBQUFtQUFBQVlBSlZUUWVaM2x1a1ZJVmJWaGhBenU1VkNfTVU2QWFveHZadFd3PT0=|4850e50cb358beda5679da6de6938b4b9998d8b73cc81bc20554b4f35c9a7718"; d_c0="AMAu238Skg2PTiGfMcLjTKtb7ZSQ0932pNM=|1525921043"; __utma=51854390.1749132575.1525921042.1525921042.1525922967.2; __utmz=51854390.1525922967.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20170920=1^3=entry_date=20170920=1; _xsrf=52692bd2-5d0c-4271-93c6-45882f981484'
    }

    req = request.Request(url, headers = headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()

    print(html)

