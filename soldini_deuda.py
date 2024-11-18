#!/usr/bin/env python3

import sqlite3
from datetime import datetime, timedelta
import os

def main():
    conn = sqlite3.connect('infomesas.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM deudas WHERE proveedor = 1")
    data_raw = cur.fetchall()
    data = []
    total = 0
    for item in data_raw:
        total += item[4]
        # print(item)
        fecha = datetime.strptime(item[2], "%Y-%m-%d %H:%M:%S")
        fechap = "%s-%s-%s" % (fecha.day, fecha.month, fecha.year)
        if item[4] >= 0:
            data.append((fechap, item[3], item[4], " ", total))
        else:
            data.append((fechap, item[3], " ", item[4], total))
    deuda_pendiente = []
    total_general = total
    data_raw.reverse() 
    for item in data_raw:
        if item[4] > 0:
            if total > 0 :
                fecha = datetime.strptime(item[2], "%Y-%m-%d %H:%M:%S")
                fechap = "%s-%s-%s" % (fecha.day, fecha.month, fecha.year)
                demora = datetime.today() - fecha
                demora_txt = "%s" % (demora.days)
                if total < item[4]:
                    # deuda_pendiente.append((fechap, item[3], total, "%s dias" % demora_txt))
                    deuda_pendiente.append("%s %s %s %s dias" % (fechap, item[3], total, demora_txt))
                else:
                    # deuda_pendiente.append((fechap, item[3], item[4], "%s dias" % demora_txt))
                    deuda_pendiente.append("%s %s %s %s dias" % (fechap, item[3], item[4], demora_txt))
            total -= item[4]
    deuda_pendiente.reverse()

    # print(deuda_pendiente)
    return(deuda_pendiente)


if __name__ == '__main__':
    main()

