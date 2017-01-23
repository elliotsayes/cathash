#!/usr/bin/env python3

import re
import web

import catdb
import base58
import defs

#web.config.debug = False

urls = (
    '/', 'index',
    '/([cde])/(.*)/(.*)', 'single',
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

code_dict = {'c':defs.Lookups.catalog, 'd':defs.Lookups.discogs}

class single:
    def GET(self,url_code,search_term,format):
        if not format in [f.name for f in defs.Formats]:
            return er('invalid format')
        format_enum = defs.Formats[format]

        lookup_enum = code_dict[url_code]
        mh = catdb.get_single_hash(lookup_enum,search_term,format_enum)

        if mh:
            return base58.b58encode(mh[0])
        else:
            return er('couldn\'t find db entry')

class json:
    def GET(self,url_code,search_term):
        lookup_enum = code_dict[url_code]
        catdb.get_multiple_hash(lookup_enum,search_term)
        return er('json wip')

if __name__ == "__main__":
    catdb.init_db()

    app = web.application(urls, globals())
    app.run()
