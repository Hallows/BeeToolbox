from Module import login

proxy = '127.0.0.1:7890'
proxies = {
    "http": "http://%(proxy)s/" % {'proxy': proxy},
    "https": "http://%(proxy)s/" % {'proxy': proxy}
}

paps=login.getAdpap(proxies)
print("you got {} paps this months!".format(paps))