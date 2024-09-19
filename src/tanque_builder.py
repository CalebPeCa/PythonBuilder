from builder import VehiculoCombateBuilder

class TanqueBuilder(VehiculoCombateBuilder):
    def build_armas(self):
        self.vehiculo.armas = "Cañón de 120mm y ametralladoras"
    def build_blindaje(self):
        self.vehiculo.blindaje = "Blindaje compuesto pesado"
    def build_motor(self):
        self.vehiculo.motor = "Motor diésel de 1500 caballos de fuerza"
    def crear_nuevo_vehiculo(self):
        super().crear