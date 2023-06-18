import tkinter as tk

ventana = tk.Tk()
ventana.title("lista de tareas")

lista_tarea = ["tarea1", "tarea2", "tarea3", "tarea4", "tarea5"]

for tarea in lista_tarea:
    tk.Checkbutton(
        ventana, text=tarea, font=("Arial", 18)).pack(pady=10, padx=60)


ventana.mainloop()
