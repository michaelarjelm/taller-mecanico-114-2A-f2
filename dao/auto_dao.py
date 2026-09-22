from dao.vehiculo_dao import VehiculoDAO

class AutoDAO(VehiculoDAO):
    def crear_tabla(self):
        super().crear_tabla()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS auto (
                patente TEXT,
                PRIMARY KEY (patente),
                FOREIGN KEY (patente) REFERENCES vehiculo(patente)
            )
        """)