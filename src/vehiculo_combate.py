class VehiculoCombate:
    def __init__(self):
        self.armas =  None
        self.blindaje = None
        self.motor = None

        def __str__(self):
            return f"Tipo: {self.tipo}, Armas: {self.armas}, Blindaje: {self.blindaje}, Motor: {self.motor}"
