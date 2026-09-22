from model.vehiculo import Vehiculo # Importa la clase base Vehiculo desde vehiculo.py
from model.modelo import Modelo

class Camion(Vehiculo): # Define la clase Camion heredando de Vehiculo
    def __init__(self, patente: str, anio: int, modelo: Modelo, capacidad_carga: int): # Constructor de Camion
        super().__init__(patente, anio, modelo) # Llama al constructor de la clase padre Vehiculo para inicializar patente, año y modelo
        self.__capacidad_carga: int = capacidad_carga # Guarda la capacidad de carga en kilos como atributo privado

    def tarifa_hora(self) -> int: # Método que sobrescribe la tarifa por hora para Camion
        return 40000 # Retorna un valor fijo de 40000 para camion
