import requests
from . import sql


def getAuth():
    URL = sql.getForumsURL()
    ips_username = sql.getMailAddr()
    ips_password = sql.getPassWord()
    print(URL)
    res = requests.get(URL, verify=False)
    print(res)
