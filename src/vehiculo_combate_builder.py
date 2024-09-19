from vehiculo_combate import VehiculoCombate

class VehiculoCombateBuilder:
    def crear_nuevo_vehiculo(self):
        self.vehiculo = VehiculoCombate()

    def build_armas(self):
        raise NotImplementedError
    def build_blindaje(self):
        raise NotImplementedError
    def build_motor(self):
        raise NotImplementedError
    def get_vehiculo(self):
        return self.vehiculo

class TanqueBuilder(VehiculoCombateBuilder):
    def build_armas(self):
        self.vehiculo.armas = "Cañón de 120mm y ametralladoras"
    def build_blindaje(self):
        self.vehiculo.blindaje = "Blindaje compuesto pesado"
    def build_motor(self):
        self.vehiculo.motor = "Motor diésel de 1500 caballos de fuerza"
    def crear_nuevo_vehiculo(self):
        super().crear_nuevo_vehiculo()
        self.vehiculo.tipo = "Tanque"