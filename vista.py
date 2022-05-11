import os
from tkinter import *
from modelo import f_error
from modelo import f_guardar
from modelo import f_modificar
from modelo import f_borrar

# from modelo import seleccionado
# from modelo import crear_base
from modelo import limpiar_campos

# from modelo import insertar
from modelo import actualizar_treeview

# from modelo import actualizar_bd

from tkinter import DISABLED, Button
from tkinter import Label
from tkinter import Entry
from tkinter import ttk
from tkinter import StringVar, IntVar
import tkinter as tk
from PIL import ImageTk, Image


"""
var_nombre, var_apellido, var_dni, var_nacimiento, var_categoria 

entry_nombre, entry_apellido, entry_dni, entry_nacimiento, entry_categoria
    
    
    var_nombre = StringVar()
    var_apellido = StringVar()
    var_dni = IntVar()
    var_nacimiento = IntVar()
    var_categoria = StringVar()
"""


## ESTO DE ABAJO NO SE DONDE METERLO


##############################################################################
def vista_principal(master):
    master.title("Planilla del Club")
    # master.geometry("800x700")
    BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
    ruta = os.path.join(BASE_DIR, "logo.jpg")

    var_nombre = StringVar()
    var_apellido = StringVar()
    var_dni = IntVar()
    var_nacimiento = IntVar()
    var_categoria = StringVar()

    def completar_campos(
        campos,
    ):  # Completa los campos de ingreso de datos me lo llevo al modelo a ver que onda

        entry_nombre.insert(0, campos[0])
        entry_apellido.insert(0, campos[1])
        entry_dni.insert(0, campos[2])
        entry_nacimiento.insert(0, campos[3])
        entry_categoria.insert(0, campos[4])

    def f_seleccionar(tree):
        bt_guardar["state"] = DISABLED
        limpiar_campos(
            entry_nombre, entry_apellido, entry_dni, entry_nacimiento, entry_categoria
        )

        if tree.selection():
            valor = tree.selection()
            item = tree.item(valor)
            mi_id = item["text"]
            campos = item["values"]
            mi_id = int(mi_id)
            completar_campos(campos)
            bt_modificar["state"] = NORMAL
            bt_borrar["state"] = NORMAL
            return mi_id
        else:
            f_error("No hay ningún ítem seleccionado")

    espacio = Label(master)
    espacio.grid(row=0, columnspan=4)
    nombre_del_club = Label(master, text="CLUB UNIVERSITARIO")
    nombre_del_club.grid(columnspan=4, row=1, column=0)

    nombre_del_club2 = Label(master, text="DE RUGBY")
    nombre_del_club2.grid(columnspan=4, row=2, column=0)
    espacio = Label(master)
    espacio.grid(row=4, columnspan=4)

    logo = Image.open(ruta)
    resize_logo = logo.resize((100, 100))
    logo2 = ImageTk.PhotoImage(resize_logo)
    mi_logo = ttk.Label(master, image=logo2)
    mi_logo.grid(row=0, column=6, rowspan=4, pady=10)

    nombre = Label(master, text="Nombre")
    nombre.grid(row=7, column=0, sticky="w", padx=10)

    apellido = Label(master, text="Apellido", anchor="n")
    apellido.grid(row=7, column=2, sticky="w", padx=10)

    dni = Label(master, text="DNI", anchor="n")
    dni.grid(row=8, column=0, sticky="w", padx=10)

    nacimiento = Label(master, text="Fecha de nacimiento", anchor="n")
    nacimiento.grid(row=8, column=2, sticky="w", padx=10)

    categoria = Label(master, text="Categoria", anchor="n")
    categoria.grid(row=9, column=0, sticky="w", padx=10)
    w_ancho = 25

    entry_nombre = Entry(master, textvariable=var_nombre, width=w_ancho)
    entry_nombre.grid(row=7, column=1)

    entry_apellido = Entry(master, textvariable=var_apellido, width=w_ancho)
    entry_apellido.grid(row=7, column=3)

    entry_dni = Entry(master, textvariable=var_dni, width=w_ancho)
    entry_dni.grid(row=8, column=1)

    entry_nacimiento = Entry(master, textvariable=var_nacimiento, width=w_ancho)
    entry_nacimiento.grid(row=8, column=3)

    entry_categoria = Entry(master, textvariable=var_categoria, width=w_ancho)
    entry_categoria.grid(row=9, column=1)

    espacio = Label(master)
    espacio.grid(row=10, columnspan=4)
    limpiar_campos(
        entry_nombre, entry_apellido, entry_dni, entry_nacimiento, entry_categoria
    )

    tree = ttk.Treeview(master)

    tree["columns"] = ("Nombre", "Apellido", "DNI", "Fecha de Nacimiento", "Categoria")

    tree.column("#0", width=50, minwidth=20, anchor="w")
    tree.column("Nombre", width=200, minwidth=20, anchor="w")
    tree.column("Apellido", width=200, minwidth=20, anchor="w")
    tree.column("DNI", width=100, minwidth=20, anchor="w")
    tree.column("Fecha de Nacimiento", width=150, minwidth=20, anchor="w")
    tree.column("Categoria", width=80, minwidth=20, anchor="w")

    tree.heading("#0", text="ID")
    tree.heading("Nombre", text="NOMBRE")
    tree.heading("Apellido", text="APELLIDO")
    tree.heading("DNI", text="DNI")
    tree.heading("Fecha de Nacimiento", text="FECHA DE NACIMIENTO")
    tree.heading("Categoria", text="CATEGORIA")

    tree.grid(column=0, row=11, columnspan=8, padx=10)

    actualizar_treeview(tree)

    bt_guardar = Button(
        master,
        text="Guardar",
        command=lambda: f_guardar(
            entry_nombre,
            entry_apellido,
            entry_dni,
            entry_nacimiento,
            entry_categoria,
            var_nombre,
            var_apellido,
            var_dni,
            var_nacimiento,
            var_categoria,
            tree,
        ),
        bg="#DCDCDC",
        width=20,
    )
    bt_guardar.grid(row=10, column=-0, pady=5, padx=5, columnspan=1)

    bt_modificar = Button(
        master,
        text="Modificar",
        command=lambda: f_modificar(
            entry_nombre,
            entry_apellido,
            entry_dni,
            entry_nacimiento,
            entry_categoria,
            var_nombre,
            var_apellido,
            var_dni,
            var_nacimiento,
            var_categoria,
            tree,
            bt_guardar,
            bt_modificar,
            bt_borrar,
        ),
        bg="#DCDCDC",
        width=20,
        state=DISABLED,
    )
    bt_modificar.grid(row=10, column=1, pady=5, padx=5, columnspan=1)

    bt_seleccionar = Button(
        master,
        text="Seleccionar",
        command=lambda: f_seleccionar(tree),
        bg="#DCDCDC",
        width=20,
    )
    bt_seleccionar.grid(row=10, column=3, pady=5, padx=5, columnspan=2)

    bt_borrar = Button(
        master,
        text="Borrar",
        command=lambda: f_borrar(
            entry_nombre,
            entry_apellido,
            entry_dni,
            entry_nacimiento,
            entry_categoria,
            bt_borrar,
            bt_modificar,
            bt_guardar,
            tree,
        ),
        bg="#DCDCDC",
        width=20,
        state=DISABLED,
    )
    bt_borrar.grid(row=10, column=5, pady=5, padx=5, columnspan=2)

    bt_salir = Button(master, text="Salir", command=master.quit, bg="#DCDCDC", width=15)
    bt_salir.grid(row=15, column=6, sticky="SE", padx=10, pady=10)


#####################################################################
