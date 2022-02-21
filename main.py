
import ui_processor

proxy = '127.0.0.1:7890'
proxies = {
    "http": "http://%(proxy)s/" % {'proxy': proxy},
    "https": "http://%(proxy)s/" % {'proxy': proxy}
}

if __name__ == '__main__':
    app = ui_processor.MyApplication()
    app.run()
    # Ideally use optparse or argparse to get JID,
    # password, and log level.
