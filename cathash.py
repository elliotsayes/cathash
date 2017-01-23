#!/usr/bin/env python3

import re
import web

import catdb
import base58
import defs

#web.config.debug = False

urls = (
    '/', 'index',
    '/([cd])/(.*)/(.*)', 'single',
    '/([cd])/([^\/]*)', 'json',
    '/(.*)', 'blank'
)

def er(t):
    return t

class index:
    def GET(self):
        return 'Usage: WIP'

class blank:
    def GET(self,name):
        return er('this page is intentionally left blank')

class single:
    def GET(self,lookup_type,search_term,format):
        print('s\n'+lookup_type+'\n'+search_term+'\n'+format)
        if not format in [f.name for f in defs.Formats]:
            return er('invalid format')

        if lookup_type is 'd':
            mh = catdb.get_hash(search_term,format,True)
        elif lookup_type is 'c':
            mh = catdb.get_hash(search_term,format,False)

        if mh:
            return base58.b58encode(mh[0])
        else:
            return er('couldn\'t find hash')

class json:
    def GET(self,lookup_type,search_term):
        return er('json wip')

if __name__ == "__main__":
    catdb.init_db()

    app = web.application(urls, globals())
    app.run()
