import time
import logging
from Module import GoonsJabber
from Module import GoonsWorm
from Module import sysSQL


def readInfo():
    mailAddr = sysSQL.getMailAddr()
    if mailAddr is None:
        result = -1
        return result

    jid = sysSQL.getJabberName()
    if jid is None:
        result = -2
        return result

    password = sysSQL.getPassWord()
    if password is None:
        result = -3
        return result

    result = {'mailAddr': mailAddr,
              'jid': jid,
              'password': password}
    return result

def login(jid,mailAddr,password):
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)-8s %(message)s')

    xmpp = GoonsJabber.EchoBot(clientJid=jid, toJid=sysSQL.getBotJid(), jabberPass=password)
    xmpp.connect()
    xmpp.process(block=False)
    time.sleep(10)
    print(xmpp.boundjid)
    xmpp.xmpp_send()
