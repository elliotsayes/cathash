#!/usr/bin/env python3

import web
import catdb
import base58

#web.config.debug = False

urls = (
    '/', 'index',
    '/c/(.*)', 'catalog',
    '/d/(.*)', 'discogs'
)

class index:
    def GET(self):
        return "Usage: WIP"

def lookup(name,is_discogs):
    mh = catdb.get_hash(name,is_discogs)

    if mh:
        return base58.b58encode(mh[0])
    else:
        return bytes()

class discogs:
    def GET(self,name):
        return lookup(name,True)

class catalog:
    def GET(self, name):
        return lookup(name,False)

if __name__ == "__main__":
    catdb.init_db()

    app = web.application(urls, globals())
    app.run()
