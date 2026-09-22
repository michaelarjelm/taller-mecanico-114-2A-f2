from model.vehiculo import Vehiculo # Importa la clase base Vehiculo desde vehiculo.py
from model.modelo import Modelo

class Moto(Vehiculo): # Define la clase Moto heredando de Vehiculo
    def __init__(self, patente: str, anio: int, modelo: Modelo):
        super().__init__(patente, anio, modelo)

    def tarifa_hora(self) -> int: # Método que sobrescribe la tarifa por hora para Moto
        return 15000 # Retorna un valor fijo de 15000 para moto
