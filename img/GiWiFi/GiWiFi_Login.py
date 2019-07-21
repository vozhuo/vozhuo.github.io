import urllib
from urllib.parse import urlparse

import requests


def login():

    url_redirect = 'http://10.12.0.9:8062/redirect?oriUrl=http://www.baidu.com?ua=Mozilla'

    headers_get = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6,en-US;q=0.4,en;q=0.2',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    }
    direct_web = requests.get(url_redirect, headers=headers_get)
    login_web = requests.get(direct_web.url, headers=headers_get)

    print(login_web.url)

    p = urlparse(login_web.url)

    url_info = urllib.parse.parse_qs(p[4])
    ip = url_info['ip'][0]
    mac = url_info['mac'][0]
    apmac = url_info['apmac'][0]


    headers_post = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6,en-US;q=0.4,en;q=0.2',
        'Connection': 'keep-alive',
        'Content - Length': '807',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://login.gwifi.com.cn',
        'Referer': login_web.url,
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    }

    data = {
        'PHPSESSID': '',
        'access_type': '0',
        'acsign': '4214a9d5a003f41db893751e9eeb7934',
        'apinfo': '',
        'btype': 'pc',
        'client_mac': 'B8:EE:65:0A:2F:D5',
        'contact_phone': '400-038-5858',
        'devicemode': '',
        'gw_address': '10.12.0.9',
        'gw_id': 'GWIFI-qingdaoshankeda09',
        'gw_port': '8060',
        'ip': ip,
        'is_signed': '2',
        'lastaccessurl': login_web.url,
        'logout_reason': '8',
        'mac': 'B8:EE:65:0A:2F:D5',
        'name': '17854258224',
        'olduser': '0',
        'online_time': '36',
        'page_time': '1491994922',
        'password': 'MrQgwif8',
        'station_cloud': 'login.gwifi.com.cn',
        'station_sn': '0090fb573f56',
        'suggest_phone': '400-038-5858',
        'url': 'http://www.baidu.com?ua=Mozilla',
        'user_agent': ''
    }
    print('Authorizing…')
    url_tar = 'http://login.gwifi.com.cn/cmps/admin.php/api/loginaction'
    requests.post(url_tar, data=data, headers=headers_post, cookies=login_web.cookies)

    url_token = 'http://10.12.0.9:8060/wifidog/auth?token=7ba9a1553b53f049e7a983750e887b0654c491b5&info=MiTfci4wNgTQyNTgyMjQsLDIwMTcwNDEyMTkwMjE4'
    url_final = 'http://login.gwifi.com.cn/cmps/admin.php/api/portal/?gw_id=GWIFI-qingdaoshankeda09&token=7ba9a1553b53f049e7a983750e887b0654c491b5&apmac=00:90:fb:57:3f:56&ssid='
    requests.get(url_token, headers=headers_get)
    requests.get(url_final, headers=headers_get)


def check():
    try:
        requests.get('http://www.baidu.com/')
    except requests.exceptions.ConnectionError:
        print('Login Failed!')
    else:
        print('Login Successfully!')


if __name__=="__main__":
    login()
    check()
