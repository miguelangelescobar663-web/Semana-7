import unittest

from cola import Cola
from repository import RotacionSaquesRepository


class TestCola(unittest.TestCase):
    """Pruebas unitarias para la estructura de datos Cola."""

    def setUp(self):
        self.cola = Cola()

    def test_cola_nueva_esta_vacia(self):
        self.assertTrue(self.cola.esta_vacia())
        self.assertEqual(self.cola.tamano(), 0)

    def test_encolar_agrega_elemento(self):
        self.cola.encolar("Jugador 1")
        self.assertFalse(self.cola.esta_vacia())
        self.assertEqual(self.cola.tamano(), 1)
        self.assertEqual(self.cola.ver_frente(), "Jugador 1")

    def test_orden_fifo(self):
        self.cola.encolar("Jugador 1")
        self.cola.encolar("Jugador 2")
        self.cola.encolar("Jugador 3")
        self.assertEqual(self.cola.desencolar(), "Jugador 1")
        self.assertEqual(self.cola.desencolar(), "Jugador 2")
        self.assertEqual(self.cola.desencolar(), "Jugador 3")

    def test_desencolar_reduce_cantidad(self):
        self.cola.encolar("Jugador 1")
        self.cola.encolar("Jugador 2")
        self.cola.desencolar()
        self.assertEqual(self.cola.tamano(), 1)

    def test_ver_frente_no_elimina_elemento(self):
        self.cola.encolar("Jugador 1")
        self.cola.encolar("Jugador 2")
        primero = self.cola.ver_frente()
        self.assertEqual(primero, "Jugador 1")
        self.assertEqual(self.cola.tamano(), 2)

    def test_desencolar_cola_vacia_lanza_excepcion(self):
        with self.assertRaises(IndexError):
            self.cola.desencolar()

    def test_ver_frente_cola_vacia_lanza_excepcion(self):
        with self.assertRaises(IndexError):
            self.cola.ver_frente()

    def test_cola_vuelve_a_estar_vacia_tras_vaciarla(self):
        self.cola.encolar("Jugador 1")
        self.cola.desencolar()
        self.assertTrue(self.cola.esta_vacia())


class TestRotacionSaquesRepository(unittest.TestCase):
    """Pruebas unitarias para el patrón Repository aplicado a la rotación."""

    def setUp(self):
        self.repo = RotacionSaquesRepository()
        for jugador in ["J1", "J2", "J3", "J4", "J5", "J6"]:
            self.repo.agregar_jugador(jugador)

    def test_agregar_jugador(self):
        self.assertEqual(self.repo.cantidad_jugadores(), 6)

    def test_obtener_jugador_actual_no_elimina(self):
        actual = self.repo.obtener_jugador_actual()
        self.assertEqual(actual, "J1")
        self.assertEqual(self.repo.cantidad_jugadores(), 6)

    def test_rotar_saque_mueve_jugador_al_final(self):
        jugador_que_saco = self.repo.rotar_saque()
        self.assertEqual(jugador_que_saco, "J1")
        self.assertEqual(self.repo.obtener_jugador_actual(), "J2")
        self.assertEqual(self.repo.cantidad_jugadores(), 6)
        self.assertIn("J1", self.repo.obtener_orden_actual())

    def test_rotacion_completa_regresa_al_orden_inicial(self):
        orden_inicial = self.repo.obtener_orden_actual()
        for _ in range(6):
            self.repo.rotar_saque()
        self.assertEqual(self.repo.obtener_orden_actual(), orden_inicial)

    def test_retirar_jugador_actual(self):
        jugador_retirado = self.repo.retirar_jugador_actual()
        self.assertEqual(jugador_retirado, "J1")
        self.assertEqual(self.repo.cantidad_jugadores(), 5)

    def test_repositorio_vacio_al_crearse(self):
        repo_vacio = RotacionSaquesRepository()
        self.assertTrue(repo_vacio.esta_vacia())
        self.assertEqual(repo_vacio.cantidad_jugadores(), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
