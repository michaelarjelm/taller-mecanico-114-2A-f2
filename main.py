# Importa la clase base Vehiculo desde el módulo vehiculo
from vehiculo import Vehiculo
# Importa la clase derivada Auto desde el módulo auto
from auto import Auto
# Importa la clase derivada Moto desde el módulo moto
from moto import Moto
# Importa la clase derivada Camion desde el módulo camion
from camion import Camion

# Instancia un objeto de la clase base Vehiculo con patente "1234" y año 1930
v = Vehiculo("1234", 1930)
# Instancia un objeto de la clase derivada Auto con patente "auto1234" y año 1930
a = Auto("auto1234", 1930)

# Registra el ingreso del objeto Auto al taller cambiando su estado interno
a.ingresar_al_taller()

# Muestra en consola la patente del auto instanciado
print(a.patente)

# Registra el ingreso del objeto Vehiculo al taller cambiando su estado interno
v.ingresar_al_taller()
# Muestra un mensaje en consola indicando el ingreso al taller
print("Vehiculo en taller")

# Muestra en consola el estado del atributo protegido _en_taller del vehículo (True)
print(v._en_taller)

# Muestra en consola el valor retornado por el método tarifa_hora() del vehículo (5000)
print(v.tarifa_hora())

# Registra la entrega del vehículo al cliente cambiando su estado interno
v.entregar_al_cliente()

# Muestra en consola el estado del atributo protegido _en_taller del vehículo (False)
print(v._en_taller)