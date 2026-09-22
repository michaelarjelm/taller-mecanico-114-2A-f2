from model.vehiculo import Vehiculo # Importa la clase base Vehiculo desde vehiculo.py
from model.modelo import Modelo

class Auto(Vehiculo): # Define la clase Auto heredando de Vehiculo
    def __init__(self, patente: str, anio: int, modelo: Modelo, capacidad_maletero: int): # Constructor de Auto
        super().__init__(patente, anio, modelo) # Llama al constructor de la clase padre Vehiculo para inicializar patente, año y modelo
        self.__capacidad_maletero: int = capacidad_maletero # Guarda la capacidad del maletero en litros como atributo privado

    def tarifa_hora(self) -> int: # Método que sobrescribe la tarifa por hora para Auto
        return 25000 # Retorna un valor fijo de 25000 para auto
