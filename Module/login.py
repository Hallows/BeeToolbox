import requests
from . import sql


def getAuth():
    URL = sql.getForumsURL()
    ips_username = sql.getMailAddr()
    ips_password = sql.getPassWord()
    print(URL)
    res = requests.get(URL, verify=False)
    cookies = res.cookies
    print(res)
    print(cookies)
    headers = {':authority': 'my-app/0.0.1'}
