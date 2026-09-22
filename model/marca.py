class Marca:
    def __init__(self, nombre: str):
        self.__nombre = nombre

    @property
    def nombre(self) -> str:
        return self.__nombre
