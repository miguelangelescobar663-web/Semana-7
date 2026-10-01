import json
import os

from cola import Cola


class RotacionSaquesRepository:


    def __init__(self, ruta_archivo=None):
        self._cola = Cola()
        self._ruta_archivo = ruta_archivo
        self._cargar()

    # ---------- Persistencia ----------
    def _guardar(self):
        """Escribe el orden actual de la cola en el archivo JSON."""
        if self._ruta_archivo is None:
            return
        datos = {"jugadores": self._cola.a_lista()}
        with open(self._ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=2)

    def _cargar(self):
        """Lee el archivo JSON (si existe) y reconstruye la cola."""
        if self._ruta_archivo is None or not os.path.exists(self._ruta_archivo):
            return
        try:
            with open(self._ruta_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
            for jugador in datos.get("jugadores", []):
                self._cola.encolar(jugador)
        except (json.JSONDecodeError, OSError, AttributeError):
            # Archivo dañado o ilegible: se inicia con una cola vacía.
            self._cola = Cola()

    # ---------- Operaciones del dominio ----------
    def agregar_jugador(self, jugador):
        """Agrega un jugador al final de la cola de rotación."""
        self._cola.encolar(jugador)
        self._guardar()

    def obtener_jugador_actual(self):
        """Consulta quién es el próximo jugador en sacar, sin removerlo."""
        return self._cola.ver_frente()

    def rotar_saque(self):
        """El jugador del frente saca y pasa al final de la fila."""
        jugador_actual = self._cola.desencolar()
        self._cola.encolar(jugador_actual)
        self._guardar()
        return jugador_actual

    def retirar_jugador_actual(self):
        """Elimina al jugador que está al frente de la cola de rotación."""
        jugador = self._cola.desencolar()
        self._guardar()
        return jugador

    def esta_vacia(self):
        """Verifica si la cola de rotación está vacía."""
        return self._cola.esta_vacia()

    def cantidad_jugadores(self):
        """Retorna la cantidad de jugadores en la cola de rotación."""
        return self._cola.tamano()

    def obtener_lista_jugadores(self):
        """Retorna la lista de jugadores en orden de saque."""
        return self._cola.a_lista()

    def obtener_orden_actual(self):
        """Retorna una representación en texto del orden de rotación actual."""
        return str(self._cola)
