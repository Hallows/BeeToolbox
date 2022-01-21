import requests
import sql


def getAuth():
    URL = sql.getForumsURL() + 'index.php?app=core&module=global&section=login&do=process'
    ips_username = sql.getMailAddr()
    ips_password = sql.getPassWord()
    print(URL)
    res = requests.post(URL, headers=h, data=json.dumps(d), verify=False)
