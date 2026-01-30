#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect("infomesas.db")
cur = conn.cursor()

cur.execute("""
SELECT
    p.descripcion,
    pp.precio,
    pp.fecha,
    CAST(julianday('now') - julianday(pp.fecha) AS INTEGER) AS dias_desde_precio
FROM productosSeguidos p
JOIN productosSeguidosPrecios pp
  ON p.idProducto = pp.idProducto
WHERE pp.fecha = (
    SELECT MAX(fecha)
    FROM productosSeguidosPrecios
    WHERE idProducto = p.idProducto
)
ORDER BY p.descripcion;
""")

for descripcion, precio, fecha, dias in cur.fetchall():
    print(f"{descripcion} {precio} -- {dias}")

conn.close()

