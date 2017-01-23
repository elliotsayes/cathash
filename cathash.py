#!/usr/bin/env python3

import web
import json as _json

import base58
import defs
import catdb

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

code_dict = {'c':defs.Lookups.catalog, 'd':defs.Lookups.discogs}

class single:
    def GET(self,url_code,search_term,format):
        if not format in [f.name for f in defs.Formats]:
            return er('invalid format')
        format_enum = defs.Formats[format]

        if not url_code in code_dict.keys():
            return er('invalid url code')
        lookup_enum = code_dict[url_code]

        mh = catdb.get_single_hash(lookup_enum,search_term,format_enum)
        if mh:
            return base58.b58encode(mh[0])
        else:
            return er('couldn\'t find db entry')

class json:
    def GET(self,url_code,search_term):
        lookup_enum = code_dict[url_code]
        mh_list = catdb.get_multiple_hash(lookup_enum,search_term)
        mh_dict = {defs.Formats(x[1]).name:base58.b58encode(x[0]) for x in mh_list}
        js = _json.dumps(mh_dict)
        return js

if __name__ == "__main__":
    catdb.init_db()

    app = web.application(urls, globals())
    app.run()
