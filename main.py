import sys

from repository import RotacionSaquesRepository


def simular_partido():
    
    print("=== Sistema de Rotación de Saques - Voleibol ===\n")
    repo = RotacionSaquesRepository()

    jugadores = ["Jugador 1", "Jugador 2", "Jugador 3",
                 "Jugador 4", "Jugador 5", "Jugador 6"]

    print("Formando la alineación inicial del equipo...")
    for jugador in jugadores:
        repo.agregar_jugador(jugador)
    print(f"Orden inicial de rotación: {repo.obtener_orden_actual()}")
    print(f"Cantidad de jugadores en cola: {repo.cantidad_jugadores()}\n")

    print("Simulando 8 saques consecutivos (el equipo mantiene el servicio):\n")
    for numero_saque in range(1, 9):
        jugador_actual = repo.obtener_jugador_actual()
        print(f"Saque #{numero_saque}: saca {jugador_actual}")
        repo.rotar_saque()
        print(f"   Nuevo orden: {repo.obtener_orden_actual()}\n")

    print("Simulando la salida de un jugador por sustitución...")
    jugador_sustituido = repo.retirar_jugador_actual()
    print(f"Sale de rotación: {jugador_sustituido}")
    print(f"Orden actualizado: {repo.obtener_orden_actual()}")
    print(f"Cantidad de jugadores en cola: {repo.cantidad_jugadores()}\n")

    print(f"¿La cola está vacía? {repo.esta_vacia()}")


if __name__ == "__main__":
    if "--consola" in sys.argv:
        simular_partido()
    else:
        from gui import iniciar_gui
        iniciar_gui()
