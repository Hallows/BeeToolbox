import tkinter as tk
import pygubu
import ui_processor

proxy = '127.0.0.1:7890'
proxies = {
    "http": "http://%(proxy)s/" % {'proxy': proxy},
    "https": "http://%(proxy)s/" % {'proxy': proxy}
}

clientJid = 'azika_gaptain@goonfleet.com'
toJid = 'directorbot@goonfleet.com'
jabberPass = 'LOVE@alan1995'


class MyApplication:
    def __init__(self):
        # 1: Create a builder
        self.builder = builder = pygubu.Builder()

        # 2: Load an ui file
        builder.add_from_file('gubugui.ui')

        # 3: Create the toplevel widget.
        self.mainwindow = builder.get_object('mainWindow')

        builder.connect_callbacks(self)

        guivars = ('jabberName', 'adName', 'password'
                   )

        builder.import_variables(self, guivars)


    def quit(self, event=None):
        self.mainwindow.quit()

    def run(self):
        self.mainwindow.mainloop()

    def on_button_readInfo_clicked(self):
        info = ui_processor.readInfo()
        self.jabberName.set(info['jid'])
        self.adName.set(info['mailAddr'])
        self.password.set(info['password'])


if __name__ == '__main__':
    app = MyApplication()
    app.run()
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

