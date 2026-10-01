# Sistema de Rotación de Saques - Voleibol

**Lenguaje utilizado:** Python 3

Proyecto que inició en la Semana 7 (*Patrones de Diseño, Testing Unitario y
Tipos de Datos Abstractos Lineales*) y que se amplió para el examen con
**persistencia de datos** e **interfaz gráfica**.

## Descripción breve

Aplicación que administra el orden de saque de un equipo de voleibol. El
jugador que saca pasa al final de la fila de rotación y espera su próximo
turno. Este comportamiento corresponde a una **Cola (Queue)** con principio
FIFO, implementada manualmente con una lista enlazada.

## Objetivo del proyecto

Modelar la rotación de saques de voleibol aplicando una estructura de datos
lineal propia (Cola), el patrón de diseño Repository, pruebas unitarias,
persistencia de datos en archivo y una interfaz gráfica de usuario.

## Principales funcionalidades

- **Rotación de saques:** el jugador del frente saca y pasa al final de la fila.
- **Agregar jugadores** al final de la fila de rotación.
- **Retirar al jugador actual** (por ejemplo, por sustitución).
- **Persistencia de datos:** el orden de rotación se guarda automáticamente en
  el archivo `jugadores.json` después de cada cambio y se recupera al abrir de
  nuevo la aplicación.
- **Interfaz gráfica (Tkinter):** ventana que muestra quién saca ahora, el
  orden completo de la fila y botones para agregar, rotar y retirar jugadores.
- **Pruebas unitarias** de la cola, del repositorio y de la persistencia.

## Estructura del proyecto

```
├── cola.py          # Cola implementada con lista enlazada (Nodo y Cola)
├── repository.py    # Patrón Repository + persistencia en JSON
├── gui.py           # Interfaz gráfica con Tkinter
├── main.py          # Punto de entrada de la aplicación
├── test_cola.py     # Pruebas unitarias (unittest)
└── README.md
```

## Estructura de datos: Cola

| Método          | Descripción                                         |
|-----------------|------------------------------------------------------|
| `encolar(x)`    | Agrega un elemento al final de la cola                |
| `desencolar()`  | Elimina y retorna el elemento al frente de la cola     |
| `ver_frente()`  | Consulta el elemento al frente sin eliminarlo          |
| `esta_vacia()`  | Verifica si la cola no tiene elementos                 |
| `tamano()`      | Retorna la cantidad de elementos almacenados           |
| `a_lista()`     | Retorna los elementos de frente a final como lista     |

## Patrón Repository y persistencia

`RotacionSaquesRepository` encapsula la Cola y expone operaciones propias del
dominio (agregar jugador, rotar saque, retirar jugador, etc.). Además es la
única clase que lee y escribe el archivo `jugadores.json`, por lo que ni la
interfaz gráfica ni la Cola conocen cómo se guardan los datos.

## Requisitos

- Python 3.8 o superior
- Tkinter (viene incluido con Python en Windows y macOS; en Linux puede
  instalarse con `sudo apt install python3-tk`)
- No requiere dependencias externas

## Cómo ejecutar el proyecto

Interfaz gráfica:

```bash
python main.py
```

En la primera ejecución se crea `jugadores.json` con un equipo de seis
jugadores. Los cambios posteriores se conservan al cerrar y abrir de nuevo.

Simulación por consola (sin persistencia):

```bash
python main.py --consola
```

## Cómo ejecutar las pruebas unitarias

```bash
python -m unittest test_cola.py -v
```

Se incluyen 19 pruebas que cubren la cola (orden FIFO, excepciones con cola
vacía), el repositorio (rotación, retiro) y la persistencia (guardar,
recuperar, archivo inexistente o dañado).

## Autor

Miguel Angel Escobar Andrade
