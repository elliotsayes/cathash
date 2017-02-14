#!/usr/bin/env python3

import web
import json

import base58
import defs
import catdb

web.config.debug = False

urls = (
    '/', 'index',
    '/([cd])/(.*)/(.*)', 'raw',
    '/([cd])/([^\/]*)', 'json_dump',
    '/(.*)', 'blank'
)

def er(t):
    print('er: '+t)
    return bytes()

class index:
    def GET(self):
        return 'Usage: WIP'

class blank:
    def GET(self,name):
        return er('this page is intentionally left blank')

code_dict = {'c':defs.Lookups.catalog, 'd':defs.Lookups.discogs}

class raw:
    def GET(self,url_code,search_term,format):
        if not format in [f.name for f in defs.Formats]:
            return er('invalid format')
        format_enum = defs.Formats[format]
        lookup_enum = code_dict[url_code]

        mh = catdb.get_single_hash(lookup_enum,search_term,format_enum)
        if mh:
            return base58.b58encode(mh[0])
        else:
            return er('no hash for that format')

class json_dump:
    def GET(self,url_code,search_term):
        lookup_enum = code_dict[url_code]
        mh_list = catdb.get_multiple_hash(lookup_enum,search_term)
        mh_dict = {defs.Formats(x[1]).name : base58.b58encode(x[0]) for x in mh_list}

        if mh_dict:
            return json.dumps(mh_dict,separators=(',', ':'))
        else:
            return er('no hash for that code')

if __name__ == "__main__":
    catdb.init_db()

    app = web.application(urls, globals())
    app.run()
