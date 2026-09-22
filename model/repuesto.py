class Repuesto:
    def __init__(self, codigo: str, nombre: str, stock: int, es_importado: bool):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__stock = stock
        self.__es_importado = es_importado

    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def stock(self) -> int:
        return self.__stock

    @property
    def es_importado(self) -> bool:
        return self.__es_importado

    def hay_stock(self) -> bool:
        return self.__stock > 0
