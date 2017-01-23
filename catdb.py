#!/usr/bin/env python3

import sqlite3
import os.path

import defs

db_name = 'cat.sqlite'

def init_db():
    if not os.path.isfile(db_name):
        print('Creating db: '+db_name)
        con = sqlite3.connect(db_name)
        with con:
            cur = con.cursor()
            cur.execute('CREATE TABLE Library(MultiHash BLOB UNIQUE, DiscogsRelease INTEGER, CatalogNumber TEXT, FormatEnum INTEGER)')
            con.commit()
        return True
    return False

def get_hash(search_term, format, is_discogs):
    if is_discogs:
        column = 'DiscogsRelease'
    else:
        column = 'CatalogNumber'

    con = sqlite3.connect(db_name)
    with con:
        cur = con.cursor()

        cur.execute('SELECT MultiHash FROM Library WHERE '+column+'=? AND FormatEnum=?', (search_term,defs.Formats[format].value))

        mh = cur.fetchone()
        return mh

def add_entry(mh,discogs,catno,format):
    con = sqlite3.connect(db_name)
    with con:
        cur = con.cursor()
        cur.execute('INSERT INTO Library VALUES(?,?,?,?)',(mh,discogs,catno,format))
