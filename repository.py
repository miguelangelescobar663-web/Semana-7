from cola import Cola


class RotacionSaquesRepository:
   
    def __init__(self):
        self._cola = Cola()

    def agregar_jugador(self, jugador):
        """Agrega un jugador al final de la cola de rotación."""
        self._cola.encolar(jugador)

    def obtener_jugador_actual(self):
        """Consulta quién es el próximo jugador en sacar, sin removerlo."""
        return self._cola.ver_frente()

    def rotar_saque(self):
        jugador_actual = self._cola.desencolar()
        self._cola.encolar(jugador_actual)
        return jugador_actual

    def retirar_jugador_actual(self):
        """Elimina al jugador que está al frente de la cola de rotación."""
        return self._cola.desencolar()

    def esta_vacia(self):
        """Verifica si la cola de rotación está vacía."""
        return self._cola.esta_vacia()

    def cantidad_jugadores(self):
        """Retorna la cantidad de jugadores en la cola de rotación."""
        return self._cola.tamano()

    def obtener_orden_actual(self):
        """Retorna una representación en texto del orden de rotación actual."""
        return str(self._cola)
