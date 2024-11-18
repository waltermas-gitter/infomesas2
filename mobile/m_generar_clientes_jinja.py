#!/bin/python3

import sqlite3
# from datetime import datetime, timedelta
import os
from jinja2 import Template, FileSystemLoader, Environment

env = Environment()
env.loader = FileSystemLoader('.')

def main():
    conn = sqlite3.connect('../infomesas.db')
    cur = conn.cursor()
    cur.execute("SELECT * from clientes ORDER BY nombre")
    clientes = []
    data = cur.fetchall()
    for item in data:
        nombreSinEspacios = item[1].replace(' ', '-')
        clientes.append((item[1], "/mobile/%s.html" % nombreSinEspacios, "/mobile/%s-deudas.html" % nombreSinEspacios))

    tmpl = env.get_template('clientes_template.html')
    html_template_string = tmpl.render(clientes=clientes)
    template_file = open("clientes.html", 'w').write(html_template_string)

    tmpl = env.get_template('cuentas_corrientes_template.html')
    html_template_string = tmpl.render(clientes=clientes)
    template_file = open("cuentascorrientes.html", 'w').write(html_template_string)

if __name__ == '__main__':
    main()
