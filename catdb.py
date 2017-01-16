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
            cur.execute("CREATE TABLE Catalog(CatNo TEXT, MultiHash NONE)")
            con.commit()

        return True

    return False

def cat2hash(catno):
    con = sqlite3.connect(db_name)
    with con:
        cur = con.cursor()
        cur.execute('SELECT MultiHash FROM Catalog WHERE CatNo=?', (catno,))

        mh = cur.fetchone()
        return mh

def add_entry(cat,mh):
    con = sqlite3.connect(db_name)
    with con:
        cur = con.cursor()
        cur.execute('INSERT INTO Catalog VALUES(?,?)',(cat,mh))
