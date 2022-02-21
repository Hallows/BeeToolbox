import time
import logging
import tkinter as tk
import pygubu
from Module import GoonsJabber
from Module import GoonsWorm
from Module import sysSQL


class MyApplication:
    def __init__(self):
        # 1: Create a builder
        self.builder = builder = pygubu.Builder()

        # 2: Load an ui file
        builder.add_from_file('gubugui.ui')

        # 3: Create the toplevel widget.
        self.mainwindow = builder.get_object('mainWindow')

        builder.connect_callbacks(self)

        guivars = ('jabberName', 'adName', 'passwd',
                   'loginNotice'
                   )

        builder.import_variables(self, guivars)

        self.mailAddr = ''
        self.jid = ''
        self.password = ''
        self.xmpp = None

    def quit(self, event=None):
        self.xmpp.disconnect(wait=True)
        self.mainwindow.quit()

    def run(self):
        self.mainwindow.mainloop()

    def on_button_readInfo_clicked(self):
        self.mailAddr = sysSQL.getMailAddr()
        if self.mailAddr is None:
            self.loginNotice.set('未能获取到AD用户名')
            return

        self.jid = sysSQL.getJabberName()
        if self.jid is None:
            self.loginNotice.set('未能获取到Jabber用户名')
            return

        self.password = sysSQL.getPassWord()
        if self.password is None:
            self.loginNotice.set('未能获取到密码')
            return

        self.jabberName.set(self.jid)
        self.adName.set(self.mailAddr)
        self.passwd.set(self.password)
        self.loginNotice.set('获取成功')

    def on_button_login_clicked(self):
        self.loginNotice.set('登录中...')
        self.jid = self.jabberName.get()
        self.mailAddr = self.adName.get()
        self.password = self.passwd.get()
        logging.basicConfig(level=logging.DEBUG,
                            format='%(levelname)-8s %(message)s')
        self.xmpp = GoonsJabber.EchoBot(clientJid=self.jid, toJid=sysSQL.getBotJid(), jabberPass=self.password)
        time.sleep(0.5)
        self.xmpp.connect()
        self.xmpp.process(block=False)
        time.sleep(3)
        print(self.xmpp.boundjid)
        self.loginNotice.set('已链接到Jabber')
        self.Button_checkPap.set

    def on_button_checkPap_clicked(self):
        GoonsWorm.getAdpap()
        self.xmpp.xmpp_send()