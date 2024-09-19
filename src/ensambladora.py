class Ensambladora:
    def __init__(self, builder):
        self.builder = builder

    def ensamblar_vehiculo(self):
        self.builder.crear_nuevo_vehiculo()
        self.builder.build_armas()
        self.builder.build_blindaje()
        self.builder.build_motor()
    def get_vehiculo(self):
        return self.builder.get_vehiculo()
