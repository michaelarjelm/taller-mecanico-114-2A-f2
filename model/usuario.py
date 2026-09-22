from model.rol import Rol
from model.persona import Persona

class Usuario:
    def __init__(self, usuario: str, password_hash: str, rol: Rol, persona: Persona):
        self.__usuario = usuario
        self.__password_hash = password_hash
        self.__rol = rol
        self.__persona = persona

    @property
    def usuario(self) -> str:
        return self.__usuario

    @property
    def rol(self) -> Rol:
        return self.__rol

    @property
    def persona(self) -> Persona:
        return self.__persona

    def autenticar(self) -> bool:
        return True

    def puede(self, accion: str) -> bool:
        return self.__rol.tiene_permiso(accion)
