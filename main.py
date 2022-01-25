import logging

from sleekxmpp import ClientXMPP
from sleekxmpp.exceptions import IqError, IqTimeout
import time

proxy = '127.0.0.1:7890'
proxies = {
    "http": "http://%(proxy)s/" % {'proxy': proxy},
    "https": "http://%(proxy)s/" % {'proxy': proxy}
}

clientJid = 'azika_gaptain@jabber-server.goonfleet.com'
toJid = 'directorbot@jabber-server.goonfleet.com'
jabberPass = 'LOVE@alan1995'


class EchoBot(ClientXMPP):

    def __init__(self, jid, password):
        ClientXMPP.__init__(self, jid, password)

        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("message", self.message)

        # If you wanted more functionality, here's how to register plugins:
        self.register_plugin('xep_0030')  # Service Discovery
        self.register_plugin('xep_0004')  # Data Forms
        self.register_plugin('xep_0060')  # PubSub
        self.register_plugin('xep_0199')  # XMPP Ping

        # Here's how to access plugins once you've registered them:
        # self['xep_0030'].add_feature('echo_demo')

        # If you are working with an OpenFire server, you will
        # need to use a different SSL version:
        # import ssl
        # self.ssl_version = ssl.PROTOCOL_SSLv3

    def session_start(self, event):
        self.send_presence()
        try:
            self.get_roster()
        except IqError as err:
            logging.error('There was an error getting the roster')
            logging.error(err.iq['error']['condition'])
            self.disconnect()
        except IqTimeout:
            logging.error('Server is taking too long to respond')
            self.disconnect()

    def message(self, msg):
        print('get message!')
        if msg['type'] in ('chat', 'normal'):
            print(msg['body'])

    def xmpp_send(self, input):
        self.send_message(mto=toJid, mbody=input, mtype='chat')


if __name__ == '__main__':
    # Ideally use optparse or argparse to get JID,
    # password, and log level.

    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)-8s %(message)s')

    xmpp = EchoBot(clientJid, jabberPass)
    xmpp.connect()
    xmpp.process(block=False)
    time.sleep(10)
    print(xmpp.boundjid)
    #xmpp.xmpp_send('!me')
