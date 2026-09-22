from dao.dao import DAO

class VehiculoDAO(DAO):
    def crear_tabla(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vehiculo (
                patente TEXT PRIMARY KEY,
                anio INTEGER NOT NULL,
                en_taller INTEGER NOT NULL,
                modelo_id INTEGER NOT NULL,
                FOREIGN KEY (modelo_id) REFERENCES modelo(id)
            )
        """)