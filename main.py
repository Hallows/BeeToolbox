import time
import logging
from Module import GoonsJabber
from Module import GoonsWorm
import guizero as gui

proxy = '127.0.0.1:7890'
proxies = {
    "http": "http://%(proxy)s/" % {'proxy': proxy},
    "https": "http://%(proxy)s/" % {'proxy': proxy}
}

clientJid = 'azika_gaptain@goonfleet.com'
toJid = 'directorbot@goonfleet.com'
jabberPass = 'LOVE@alan1995'

if __name__ == '__main__':
    # Ideally use optparse or argparse to get JID,
    # password, and log level.

    # logging.basicConfig(level=logging.DEBUG,
    #                     format='%(levelname)-8s %(message)s')

    # xmpp = GoonsJabber.EchoBot()
    # xmpp.connect()
    # xmpp.process(block=False)
    # time.sleep(10)
    # print(xmpp.boundjid)
    # xmpp.xmpp_send()

    app = gui.App(title="BeeToolBox", layout='grid', width=750, height=500)
    title_box = gui.TitleBox(app, "title",)
    app.display()
