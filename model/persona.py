class Persona:
    def __init__(self, rut: str, nombre: str):
        self.__rut = rut
        self.__nombre = nombre

    @property
    def rut(self) -> str:
        return self.__rut

    @property
    def nombre(self) -> str:
        return self.__nombre
