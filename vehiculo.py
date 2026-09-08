# Definición de la clase base Vehiculo para representar los vehículos en el sistema
class Vehiculo:
    # Método constructor que inicializa los atributos de instancia de Vehiculo
    def __init__(self, patente: str, anio: int) -> None:
        # Asigna la patente del vehículo (tipo texto) a la instancia
        self.patente: str = patente
        # Asigna el año de fabricación (tipo entero) a la instancia
        self.anio: int = anio
        # Inicializa el atributo protegido que indica si está en taller en False (tipo booleano)
        self._en_taller: bool = False

    # Método para registrar el ingreso del vehículo al taller
    def ingresar(self) -> None:
        # Cambia el estado del atributo protegido a True indicando que está en el taller
        self._en_taller = True

    # Método para registrar la entrega y salida del vehículo del taller
    def entregar(self) -> None:
        # Cambia el estado del atributo protegido a False indicando que ya no está en el taller
        self._en_taller = False
