import sqlite3

def crear_conexion():
    conexion = sqlite3.connect("taller.db")
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion



