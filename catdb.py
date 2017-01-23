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

col_dict = {defs.Lookups.catalog:'CatalogNumber', defs.Lookups.discogs:'DiscogsRelease'}

def get_single_hash(lookup_enum, search_term, format_enum):
    column = col_dict[lookup_enum]

    con = sqlite3.connect(db_name)
    with con:
        cur = con.cursor()
        cur.execute('SELECT MultiHash FROM Library WHERE '+column+'=? AND FormatEnum=?', (search_term, format_enum.value))
        mh = cur.fetchone()

        return mh

def get_multiple_hash(lookup_enum, search_term):
    column = col_dict[lookup_enum]

    con = sqlite3.connect(db_name)
    with con:
        cur = con.cursor()
        cur.execute('SELECT MultiHash,FormatEnum FROM Library WHERE '+column+'=?', (search_term,))
        mh = cur.fetchall()
        
        return mh

def get_hash_webpy(search_term, format, is_discogs):
    if is_discogs:
        column = 'DiscogsRelease'
    else:
        column = 'CatalogNumber'

    myvar = dict(s=search_term,f=format)

    db = web.database(dbn='sqlite', db=db_name)
    result = db.select('Library', myvar, what='MultiHash', where=column+'=$s AND FormatEnum=$f')


def add_entry(mh,discogs,catno,format):
    con = sqlite3.connect(db_name)
    with con:
        cur = con.cursor()
        cur.execute('INSERT INTO Library VALUES(?,?,?,?)',(mh,discogs,catno,format))
