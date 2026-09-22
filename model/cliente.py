from model.persona import Persona

class Cliente:
    def __init__(self, persona: Persona):
        self.__persona = persona

    @property
    def persona(self) -> Persona:
        return self.__persona

    def tiene_deuda(self) -> bool:
        return False
