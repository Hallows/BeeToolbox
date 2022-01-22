import requests
from bs4 import BeautifulSoup
from . import sysSQL


def getAdpap(proxies):
    URL = sysSQL.getAdURL() + '/login'
    username = sysSQL.getMailAddr()
    password = sysSQL.getPassWord()
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
