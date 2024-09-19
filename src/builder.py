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