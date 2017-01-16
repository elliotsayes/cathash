#!/usr/bin/env python3

import web

urls = (
    '/c/(.*)', 'cat'
)

class cat:
    def GET(self, name):
        return "Hello, "+name+"!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
