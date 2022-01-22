import requests
from bs4 import BeautifulSoup
from . import sql


def formumsLogin(proxies):
    URL = sql.getForumsURL()
    ips_username = sql.getMailAddr()
    ips_password = sql.getPassWord()
    print(URL)
    res = requests.get(URL, verify=False, proxies=proxies)
    cookies = res.cookies
    print(res.text)
    print(cookies)
    headers = {':authority': 'my-app/0.0.1'}


def getAdpap(proxies):
    URL = sql.getAdURL() + '/login'
    username = sql.getMailAddr()
    password = sql.getPassWord()
    print(URL)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/97.0.4692.99 Safari/537.36',
        'DNT': '1'}
    # post的数据
    data = {'Email address': username, 'Password': password}
    res = requests.post(URL, headers=headers, data=data, verify=False, proxies=proxies)
    soup = BeautifulSoup(res.text, 'html.parser')
    node = soup.findAll('tr', class_='success')
    if node is not None:
        pap = 0
        for i in node:
            chaNum = i.find('td').get_text()
            pap = pap+int(chaNum)
        return pap
    else:
        return 0
