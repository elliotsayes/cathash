#!/usr/bin/env python3

import web
import catdb
import base58

#web.config.debug = False

urls = (
    '/', 'index',
    '/c/(.*)', 'cat',
)

class index:
    def GET(self):
        return "Usage: WIP"

class cat:
    def GET(self, name):
        mh = catdb.get_hash(name,False)

        if mh:
            mh58 = base58.b58encode(mh[0])
            return mh58
        else:
            return bytes()

if __name__ == "__main__":
    catdb.init_db()

    app = web.application(urls, globals())
    app.run()
