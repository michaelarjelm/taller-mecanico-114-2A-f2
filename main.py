from conectar import crear_conexion

from dao.marca_dao import MarcaDAO
from dao.modelo_dao import ModeloDAO
from dao.vehiculo_dao import VehiculoDAO
from dao.auto_dao import AutoDAO

# -- CÓDIGO DE PRUEBA DE BASE DE DATOS Y DAOs --
print("Iniciando prueba de base de datos...")
conexion = crear_conexion()

# Instanciar DAOs pasándoles la conexión
marca_dao = MarcaDAO(conexion)
modelo_dao = ModeloDAO(conexion)
vehiculo_dao = VehiculoDAO(conexion)
auto_dao = AutoDAO(conexion)

# Crear las tablas
marca_dao.crear_tabla()
modelo_dao.crear_tabla()
vehiculo_dao.crear_tabla()
auto_dao.crear_tabla()

# Confirmar cambios en la base de datos
conexion.commit()
print("¡Tablas creadas exitosamente en la base de datos taller.db!")

# ====================================================================
# CÓDIGO ANTERIOR COMENTADO PARA ANÁLISIS
# ====================================================================
"""
from model.vehiculo import Vehiculo # Importa la clase base Vehiculo desde vehiculo.py
from model.auto import Auto # Importa la clase Auto desde el archivo local auto.py
from model.moto import Moto # Importa la clase Moto desde el archivo local moto.py
from model.camion import Camion # Importa la clase Camion desde el archivo local camion.py
from model.marca import Marca
from model.modelo import Modelo

# Instanciación de objetos de dependencias
marca_toyota = Marca("Toyota")
modelo_yaris = Modelo("Yaris", marca_toyota)

marca_honda = Marca("Honda")
modelo_cbr = Modelo("CBR", marca_honda)

marca_volvo = Marca("Volvo")
modelo_fh = Modelo("FH", marca_volvo)

# Instanciación de objetos
vehiculo_base = Vehiculo("BASE01", 2015, modelo_yaris) # Instancia un objeto Vehiculo base

try:
    auto = Auto("AB12", 2018, modelo_yaris, 200) # Instancia un objeto Auto con capacidad de maletero
except ValueError as e:
    print(f"Error generado: {e}")
    auto = Auto("AB1234", 2018, modelo_yaris, 200) # Instancia válida para continuar la ejecución

moto = Moto("CD5678", 2020, modelo_cbr) # Instancia un objeto Moto
camion = Camion("EF9012", 2023, modelo_fh, 5000) # Instancia un objeto Camion con capacidad de carga

# Pruebas de ingreso al taller
print(auto.ingresar()) # Ejecuta ingresar() del auto
print(moto.ingresar()) # Ejecuta ingresar() de la moto
print(camion.ingresar()) # Ejecuta ingresar() del camión

# Pruebas de encapsulamiento y asignación de patente
pruebaEnc = camion.patente # Obtiene la patente del camión
camion.set_patente("EF9012") # Asigna una nueva patente válida usando el método setter
print(f"Patente obtenida: {pruebaEnc}") # Imprime la patente obtenida


# Pruebas de tarifa_hora()
print(f"Tarifa por hora Vehiculo Base: ${vehiculo_base.tarifa_hora()}") # Tarifa base (5000)
print(f"Tarifa por hora Auto: ${auto.tarifa_hora()}") # Tarifa sobreescrita Auto (25000)
print(f"Tarifa por hora Moto: ${moto.tarifa_hora()}") # Tarifa sobreescrita Moto (15000)
print(f"Tarifa por hora Camión: ${camion.tarifa_hora()}") # Tarifa sobreescrita Camion (40000)
"""
