from vehiculo_combate_builder import TanqueBuilder
from vehiculo_blindado_ligero_builder import VehiculoBlindadoLigeroBuilder
from ensambladora import Ensambladora

if __name__ == "__main__":
    # Estoy comentando para que veas que sí le muevo al Python
    # Ensamblamos un tanque
    tanque_builder = TanqueBuilder()
    ensambladora = Ensambladora(tanque_builder)
    ensambladora.ensamblar_vehiculo()
    tanque = ensambladora.get_vehiculo()
    print(tanque)

    # Ahora un vehículo blindado ligero
    vehiculo_blindado_builder = VehiculoBlindadoLigeroBuilder()
    ensambladora = Ensambladora(vehiculo_blindado_builder)
    ensambladora.ensamblar_vehiculo()
    vehiculo_blindado = ensambladora.get_vehiculo()
    print(vehiculo_blindado)