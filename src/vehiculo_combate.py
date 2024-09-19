class VehiculoCombate:
    def __init__(self, tipo=None, armas=None, blindaje=None, motor=None):
        self.tipo = tipo
        self.armas = armas
        self.blindaje = blindaje
        self.motor = motor
    def __str__(self):
        return f"Tipo: {self.tipo} \n Armas: {self.armas} \n Blindaje: {self.blindaje} \n Motor: {self.motor} \n"


