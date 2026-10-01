class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Cola:
    

    def __init__(self):
        self._frente = None
        self._final = None
        self._cantidad = 0

    def encolar(self, elemento):
        """Agrega un elemento al final de la cola."""
        nuevo_nodo = Nodo(elemento)
        if self.esta_vacia():
            self._frente = nuevo_nodo
            self._final = nuevo_nodo
        else:
            self._final.siguiente = nuevo_nodo
            self._final = nuevo_nodo
        self._cantidad += 1

    def desencolar(self):
        """Elimina y retorna el elemento que está al frente de la cola"""
        if self.esta_vacia():
            raise IndexError("No se puede desencolar: la cola está vacía.")
        nodo_frente = self._frente
        self._frente = self._frente.siguiente
        if self._frente is None:
            self._final = None
        self._cantidad -= 1
        return nodo_frente.dato

    def ver_frente(self):
        """Consulta (sin eliminar) el elemento que está al frente de la cola."""
        if self.esta_vacia():
            raise IndexError("La cola está vacía, no hay elemento al frente.")
        return self._frente.dato

    def esta_vacia(self):
        """Retorna True si la cola no tiene elementos almacenados."""
        return self._cantidad == 0

    def tamano(self):
        """Retorna la cantidad de elementos almacenados en la cola."""
        return self._cantidad

    def a_lista(self):
        """Retorna los elementos de la cola, de frente a final, como lista."""
        elementos = []
        actual = self._frente
        while actual is not None:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

    def __len__(self):
        return self._cantidad

    def __str__(self):
        elementos = []
        actual = self._frente
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " -> ".join(elementos) if elementos else "Cola vacía"
