#!/usr/bin/env python3

import sqlite3
import os

def main():
    conn = sqlite3.connect('infomesas.db')
    cur = conn.cursor()
    ultima_lista_file = open("ultimalista.txt", "a")
    cur.execute("SELECT * from precios2")
    data = cur.fetchall()
    for item in data:
        if item[2] is None:
            fija = ' '
        else:
            fija = item[2]
        if item[3] is None:
            trampa = ' '
        else:
            trampa = item[3]
        ultima_lista_file.write("%s %s %s %s\n" % (item[1], fija, trampa, item[4]))

    ultima_lista_file.close()


if __name__ == '__main__':
    main()
