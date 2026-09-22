from model.repuesto import Repuesto

class LineaDetalle:
    def __init__(self, cantidad: int, precio_unitario: int, repuesto: Repuesto):
        self.__cantidad = cantidad
        self.__precio_unitario = precio_unitario
        self.__repuesto = repuesto

    @property
    def cantidad(self) -> int:
        return self.__cantidad

    @property
    def precio_unitario(self) -> int:
        return self.__precio_unitario

    @property
    def repuesto(self) -> Repuesto:
        return self.__repuesto

    def subtotal(self) -> int:
        return self.__cantidad * self.__precio_unitario
