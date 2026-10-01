import os
import tkinter as tk

from repository import RotacionSaquesRepository

ARCHIVO_DATOS = "jugadores.json"


class AplicacionRotacion:
    """Interfaz gráfica (Tkinter) para el sistema de rotación de saques."""

    def __init__(self, ventana, repositorio):
        self.ventana = ventana
        self.repo = repositorio
        self.ventana.title("Rotación de Saques - Voleibol")
        self.ventana.geometry("420x480")
        self.ventana.resizable(False, False)

        self._crear_widgets()
        self.actualizar_vista()

    def _crear_widgets(self):
        tk.Label(self.ventana, text="Rotación de Saques - Voleibol",
                 font=("Arial", 15, "bold")).pack(pady=(12, 4))

        self.etiqueta_saca = tk.Label(self.ventana, text="",
                                      font=("Arial", 12), fg="#1a6b2f")
        self.etiqueta_saca.pack(pady=4)

        tk.Label(self.ventana, text="Orden de rotación (frente → final):",
                 font=("Arial", 10)).pack(anchor="w", padx=20)
        self.lista = tk.Listbox(self.ventana, height=9, font=("Arial", 11),
                                activestyle="none")
        self.lista.pack(fill="x", padx=20, pady=4)

        marco_entrada = tk.Frame(self.ventana)
        marco_entrada.pack(fill="x", padx=20, pady=8)
        self.entrada = tk.Entry(marco_entrada, font=("Arial", 11))
        self.entrada.pack(side="left", fill="x", expand=True)
        self.entrada.bind("<Return>", lambda evento: self.agregar_jugador())
        tk.Button(marco_entrada, text="Agregar jugador",
                  command=self.agregar_jugador).pack(side="left", padx=(8, 0))

        marco_botones = tk.Frame(self.ventana)
        marco_botones.pack(pady=6)
        tk.Button(marco_botones, text="Rotar saque", width=16,
                  command=self.rotar_saque).pack(side="left", padx=6)
        tk.Button(marco_botones, text="Retirar jugador actual", width=20,
                  command=self.retirar_jugador).pack(side="left", padx=6)

        self.etiqueta_estado = tk.Label(self.ventana, text="", fg="#555555",
                                        wraplength=380)
        self.etiqueta_estado.pack(pady=8)

    # ---------- Acciones de los botones ----------
    def agregar_jugador(self):
        nombre = self.entrada.get().strip()
        if not nombre:
            self._estado("Escribe el nombre del jugador.")
            return
        self.repo.agregar_jugador(nombre)
        self.entrada.delete(0, tk.END)
        self._estado(f"{nombre} se agregó al final de la fila.")
        self.actualizar_vista()

    def rotar_saque(self):
        if self.repo.esta_vacia():
            self._estado("No hay jugadores para rotar.")
            return
        jugador = self.repo.rotar_saque()
        self._estado(f"{jugador} sacó y pasó al final de la fila.")
        self.actualizar_vista()

    def retirar_jugador(self):
        if self.repo.esta_vacia():
            self._estado("No hay jugadores para retirar.")
            return
        jugador = self.repo.retirar_jugador_actual()
        self._estado(f"{jugador} salió de la rotación (sustitución).")
        self.actualizar_vista()

    # ---------- Vista ----------
    def actualizar_vista(self):
        jugadores = self.repo.obtener_lista_jugadores()
        self.lista.delete(0, tk.END)
        for posicion, jugador in enumerate(jugadores, start=1):
            self.lista.insert(tk.END, f"{posicion}. {jugador}")
        if jugadores:
            self.etiqueta_saca.config(text=f"Saca ahora: {jugadores[0]}")
        else:
            self.etiqueta_saca.config(text="La fila está vacía")

    def _estado(self, mensaje):
        self.etiqueta_estado.config(text=mensaje)


def iniciar_gui():
    primera_vez = not os.path.exists(ARCHIVO_DATOS)
    repositorio = RotacionSaquesRepository(ARCHIVO_DATOS)
    if primera_vez:
        # Primera ejecución: se precarga un equipo de seis jugadores.
        for numero in range(1, 7):
            repositorio.agregar_jugador(f"Jugador {numero}")
    ventana = tk.Tk()
    AplicacionRotacion(ventana, repositorio)
    ventana.mainloop()
