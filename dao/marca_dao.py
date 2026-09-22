from dao.dao import DAO


class MarcaDAO(DAO):
    def crear_tabla(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS marca (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL)
        """)
