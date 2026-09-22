class Rol:
    def __init__(self, nombre: str, permisos: list):
        self.__nombre = nombre
        self.__permisos = permisos

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def permisos(self) -> list:
        return self.__permisos

    def tiene_permiso(self, accion: str) -> bool:
        return accion in self.__permisos
