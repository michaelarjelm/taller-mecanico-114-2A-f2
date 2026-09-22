from dao.dao import DAO


class ModeloDAO(DAO):
    def crear_tabla(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS modelo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                marca_id INTEGER NOT NULL,
                FOREIGN KEY (marca_id) REFERENCES marca(id)
            )
        """)