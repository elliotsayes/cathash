#!/usr/bin/env python3

import sqlite3
import os.path

db_name = 'cat.sqlite'

def init_db():
    if not os.path.isfile(db_name):
        print('Creating db: '+db_name)

        con = sqlite3.connect(db_name)
        with con:
            cur = con.cursor()
            cur.execute('CREATE TABLE Library(MultiHash BLOB UNIQUE, DiscogsRelease INTEGER UNIQUE, CatalogNumber TEXT, FormatEnum INTEGER)')
            con.commit()

        return True

    return False

def get_hash(search_term, is_discogs=True):
    con = sqlite3.connect(db_name)
    with con:
        cur = con.cursor()
        
        if is_discogs:
            cur.execute('SELECT MultiHash FROM Library WHERE DiscogsRelease=?', (search_term,))
        else:
            cur.execute('SELECT MultiHash FROM Library WHERE CatalogNumber=?', (search_term,))

        mh = cur.fetchone()
        return mh

def add_entry(mh,discogs,catno,format):
    con = sqlite3.connect(db_name)
    with con:
        cur = con.cursor()
        cur.execute('INSERT INTO Library VALUES(?,?,?,?)',(mh,discogs,catno,format))
