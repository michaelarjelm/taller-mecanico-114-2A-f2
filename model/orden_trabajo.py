from model.vehiculo import Vehiculo
from model.usuario import Usuario
from model.linea_detalle import LineaDetalle

class OrdenTrabajo:
    def __init__(self, numero: int, descripcion: str, vehiculo: Vehiculo, usuario: Usuario):
        self.__numero = numero
        self.__descripcion = descripcion
        self.__horas = 0
        self.__cerrada = False
        self.__vehiculo = vehiculo
        self.__usuario = usuario
        self.__lineas_detalle = []

    @property
    def numero(self) -> int:
        return self.__numero

    @property
    def cerrada(self) -> bool:
        return self.__cerrada

    def agregar_horas(self, cantidad: int) -> None:
        if not self.__cerrada:
            self.__horas += cantidad

    def agregar_linea_detalle(self, linea: LineaDetalle) -> None:
        if not self.__cerrada:
            self.__lineas_detalle.append(linea)

    def cerrar(self) -> None:
        self.__cerrada = True

    def total(self) -> int:
        total_repuestos = sum(linea.subtotal() for linea in self.__lineas_detalle)
        total_horas = self.__horas * self.__vehiculo.tarifa_hora()
        return total_repuestos + total_horas
