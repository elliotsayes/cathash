#!/usr/bin/env python3

import web
import catdb

urls = (
    '/', 'index',
    '/c/(.*)', 'cat',
)

class index:
    def GET(self):
        return "Usage: WIP"

class cat:
    def GET(self, name):
        catdb.init_db()
        return "Hello, "+name+"!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
