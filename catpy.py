#!/usr/bin/env python3

import web

urls = (
    '/', 'index',
    '/c/(.*)', 'cat',
)

class index:
    def GET(self):
        return "Usage: WIP"

class cat:
    def GET(self, name):
        return "Hello, "+name+"!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
