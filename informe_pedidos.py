#!/usr/bin/env python3

import sqlite3
from datetime import datetime, timedelta, date
import calendar
from dateutil.relativedelta import relativedelta

def main():
    conn = sqlite3.connect('infomesas.db')
    cur = conn.cursor()
    totalesFecha = []
    totalesMes = []

    diaDesdeDT = datetime.strptime("2020-09-01 00:00:00", "%Y-%m-%d %H:%M:%S")
    
    while datetime.today() > diaDesdeDT:
        diaDesdeString = diaDesdeDT.strftime("%Y-%m-%d")
        diaHastaString = datetime.strftime(diaDesdeDT, "%Y-%m-")
        ultimoDiaMes = calendar.monthrange(int(datetime.strftime(diaDesdeDT,"%y")), int(datetime.strftime(diaDesdeDT,"%m")))[1]
        diaHastaString = diaHastaString + str(ultimoDiaMes) + " 23:59:59"
        queryStringFecha = "SELECT COUNT(idPedido) FROM pedidos WHERE (fecha >= '" + diaDesdeString + "'AND fecha <= '" + diaHastaString + "')"
        cur.execute(queryStringFecha)
        data = cur.fetchall()[0][0]
        # print(datetime.strftime(diaDesdeDT, "%Y-%m"))
        # print(data)
        totalesFecha.append(datetime.strftime(diaDesdeDT, "%Y-%m"))
        totalesMes.append(data)

        diaDesdeDT = diaDesdeDT + relativedelta(months=+1)

    return totalesFecha, totalesMes 
   

if __name__ == '__main__':
    main()
