from vehiculo_combate_builder import VehiculoCombateBuilder

class VehiculoBlindadoLigeroBuilder(VehiculoCombateBuilder):
    def build_armas(self):
        self.vehiculo.armas = "Ametralladora ligera"
    def build_blindaje(self):
        self.vehiculo.blindaje = "Blindaje ligero de aleación"
    def build_motor(self):
        self.vehiculo.motor = "Motor híbrido de 500 caballos de fuerza"
    def crear_nuevo_vehiculo(self):
        super().crear_nuevo_vehiculo()
        self.vehiculo.tipo = "Vehiculo blindado ligero"