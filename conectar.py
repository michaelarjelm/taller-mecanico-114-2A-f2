import sqlite3
from marca import Marca
from modelo import Modelo
from auto import Auto

conexion = sqlite3.connect("taller.db")
cursor = conexion.cursor()

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS vehiculo (
    patente TEXT PRIMARY KEY,
    anio INTEGER,
    en_taller INTEGER
)
""")

marca = Marca("Toyota")
modelo=Modelo("Corolla", marca)
auto=Auto("123457", 2006, modelo,200)

cursor.execute("""INSERT INTO vehiculo (patente, anio, en_taller)
VALUES (?,?,?)""",(auto.patente, auto.anio, int(auto.en_taller)))



conexion.commit()