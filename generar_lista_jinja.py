#!/usr/bin/env python3

import sqlite3
# from datetime import datetime, timedelta
import os

from jinja2 import Template, FileSystemLoader, Environment

env = Environment()
env.loader = FileSystemLoader('.')


def main(mes):
    conn = sqlite3.connect('infomesas.db')
    cur = conn.cursor()

    cur.execute("SELECT * from precios2 WHERE modelo='nro 100'")
    data = cur.fetchall()
    nro100 = []
    for item in data:
        nro100.append((item[2], item[3], item[4]))

    cur.execute("SELECT * from precios2 WHERE modelo='recta'")
    data = cur.fetchall()
    recta = []
    for item in data:
        recta.append((item[2], item[3], item[4]))
    cur.execute("SELECT * from precios2 WHERE modelo='con vidrios' OR modelo='con patas 10*10'")
    data = cur.fetchall()
    for item in data:
        recta.append((item[1], item[3], item[4]))
    
    cur.execute("SELECT * from precios2 WHERE modelo='redonda'")
    data = cur.fetchall()
    redonda = []
    for item in data:
        redonda.append((item[2], item[3], item[4]))

    cur.execute("SELECT * from precios2 WHERE modelo='escandinava' OR modelo='escandinava redonda'")
    data = cur.fetchall()
    escandinava = []
    for item in data:
       escandinava.append((item[2], item[3], item[4]))

    cur.execute("SELECT * from precios2 WHERE modelo='ratona' OR modelo='ratona escandinava'")
    data = cur.fetchall()
    ratona = []
    for item in data:
       ratona.append((item[2], item[3], item[4]))

    tmpl = env.get_template('lista_template.html')
    # html_template_string = tmpl.render(nro100=nro100, recta=recta, redonda=redonda, escandinava=escandinava, ratona=ratona, mes='2/2024')
    html_template_string = tmpl.render(nro100=nro100, recta=recta, redonda=redonda, escandinava=escandinava, ratona=ratona, mes=mes)
    template_file = open("lista.html", 'w').write(html_template_string)

if __name__ == '__main__':
    main()
