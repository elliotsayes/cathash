#!/usr/bin/env python3

import sqlite3
import os.path

db_name = 'cat.sql'

def init_db():
    if not os.path.isfile(db_name):

        print('Creating db: '+db_name)

        con = None
        try:
            con = sqlite3.connect(db_name)

            cur = con.cursor()
            cur.execute("CREATE TABLE Catalog(CatNo TEXT, MH_SHA256 NONE)")

            con.commit()

        except (lite.Error, e):
            print ("Error %s:" % e.args[0])
            sys.exit(1)

        finally:
            if con:
                con.close()

def cat2hash():
    con = None
    try:
        con = sqlite3.connect(db_name)

        cur = con.cursor()
        cur.execute('SELECT SQLITE_VERSION()')

        data = cur.fetchone()

        print("SQLite version: %s" % data)

    except (lite.Error, e):
        print ("Error %s:" % e.args[0])
        sys.exit(1)

    finally:
        if con:
            con.close()
