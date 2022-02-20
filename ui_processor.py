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

