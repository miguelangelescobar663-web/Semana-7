# Sistema de Rotación de Saques - Voleibol

Proyecto desarrollado para la actividad de la **Semana 7: Patrones de Diseño,
Testing Unitario y Tipos de Datos Abstractos Lineales**.

## Descripción del problema

En el voleibol, el equipo que tiene el servicio debe rotar el orden de saque
entre sus jugadores. Cada vez que un jugador saca y el equipo mantiene el
servicio, ese jugador debe volver al final de la fila de rotación para
esperar su próximo turno. Este comportamiento corresponde exactamente al
funcionamiento de una **Cola (Queue)**: el primer jugador de la fila es el
primero en sacar (FIFO), y al terminar su turno regresa al final de la fila.

## Estructura de datos

Se implementó manualmente una **Cola** (`cola.py`) utilizando una lista
enlazada propia (sin usar `collections.deque` ni `queue.Queue` de la
biblioteca estándar de Python), con las siguientes operaciones:

| Método          | Descripción                                         |
|-----------------|------------------------------------------------------|
| `encolar(x)`    | Agrega un elemento al final de la cola                |
| `desencolar()`  | Elimina y retorna el elemento al frente de la cola     |
| `ver_frente()`  | Consulta el elemento al frente sin eliminarlo          |
| `esta_vacia()`  | Verifica si la cola no tiene elementos                 |
| `tamano()`      | Retorna la cantidad de elementos almacenados           |

## Patrón de diseño Repository

La clase `RotacionSaquesRepository` (`repository.py`) encapsula el acceso a
la Cola y expone operaciones propias del dominio del problema (agregar
jugador, rotar saque, retirar jugador, etc.), separando así la lógica de
acceso a datos de la lógica principal de la aplicación (`main.py`). La
aplicación nunca manipula la Cola directamente, siempre lo hace a través
del repositorio.

## Estructura del proyecto

```
volleyball_rotation/
├── cola.py          # Implementación manual de la Cola (lista enlazada)
├── repository.py    # Patrón Repository
├── main.py          # Aplicación de demostración
├── test_cola.py     # Pruebas unitarias (unittest)
└── README.md
```

## Requisitos

- Python 3.8 o superior
- No requiere dependencias externas

## Cómo ejecutar la aplicación

```bash
python main.py
```

Esto simula la formación de un equipo, 8 saques consecutivos con su
respectiva rotación, y la salida de un jugador por sustitución.

## Cómo ejecutar las pruebas unitarias

Con el módulo `unittest` de la biblioteca estándar:

```bash
python -m unittest test_cola.py -v
```

O, alternativamente, con `pytest` instalado:

```bash
pytest test_cola.py -v
```

Se incluyen 14 pruebas unitarias que cubren:
- Creación de una cola vacía
- Encolar y desencolar elementos (orden FIFO)
- Consulta del frente sin eliminar
- Manejo de excepciones al operar sobre una cola vacía
- Integración completa del Repository (agregar, rotar, retirar jugadores)
- Verificación de que una rotación completa regresa al orden inicial

## Autor

[Nombre del estudiante]
