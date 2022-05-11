import sqlite3

# from tkinter import ttk
from tkinter.messagebox import *

# import tkinter as tk
import re
from tkinter import DISABLED, END, NORMAL  # StringVar, IntVar

"""var_nombre = StringVar()
var_apellido = StringVar()
var_dni = IntVar()
var_nacimiento = IntVar()
var_categoria = StringVar()
"""


def crear_base():
    con = sqlite3.connect("mi_base.db")
    return con


def crear_tabla(con):
    cursor = con.cursor()
    sql = """CREATE TABLE socios
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             nombre varchar(20) NOT NULL,
             apellido varchar(20) NOT NULL,
             dni integer NOT NULL,
             fecha integer NOT NULL,
             categoria varchar(20) NOT NULL)
    """
    cursor.execute(sql)
    con.commit()


try:
    con = crear_base()
    crear_tabla(con)
except:
    pass


def seleccionado(tree):
    valor = tree.selection()
    item = tree.item(valor)
    mi_idd = item["text"]
    return mi_idd, valor


def insertar(
    entry_nombre,
    entry_apellido,
    entry_dni,
    entry_nacimiento,
    entry_categoria,
    nombre,
    apellido,
    dni,
    fecha,
    categoria,
    tree,
):
    cadena1 = nombre
    cadena2 = apellido
    patron = "^[A-Za-záéíóú]*$"
    if re.match(patron, cadena1):
        if re.match(patron, cadena2):
            con = crear_base()
            cursor = con.cursor()
            # mi_id = int(mi_id)
            data = (nombre, apellido, dni, fecha, categoria)
            sql = "INSERT INTO socios(nombre, apellido,  dni, fecha, categoria) VALUES (?, ?, ?, ?, ?);"
            cursor.execute(sql, data)
            con.commit()
            actualizar_treeview(tree)
            limpiar_campos(
                entry_nombre,
                entry_apellido,
                entry_dni,
                entry_nacimiento,
                entry_categoria,
            )
        else:
            f_error("Campos ingresados en 'Apellido' incorrectos")
    else:
        f_error("Campos ingresados en 'Nombre' incorrectos")


"""
def f_seleccionar(tree):
    # bt_guardar["state"] = DISABLED
    limpiar_campos()

    if tree.selection():
        valor = tree.selection()
        item = tree.item(valor)
        mi_id = item["text"]
        campos = item["values"]
        mi_id = int(mi_id)
        completar_campos(campos)
        # bt_modificar["state"] = NORMAL
        # bt_borrar["state"] = NORMAL
        return mi_id
    else:
        f_error("No hay ningún ítem seleccionado")


def f_borrar(tree):
    # bt_borrar["state"] = DISABLED
    # bt_modificar["state"] = DISABLED
    if tree.selection():

        mi_id, valor = seleccionado()
        con = crear_base()
        cursor = con.cursor()
        data = (mi_id,)
        sql = "DELETE FROM socios WHERE id = ?;"
        cursor.execute(sql, data)
        con.commit()
        tree.delete(valor)
        limpiar_campos()
        # bt_guardar["state"] = NORMAL

    else:
        f_error("No hay ningún ítem seleccionado")
"""


def actualizar_bd(nombre, apellido, dni, fecha, categoria, tree):

    con = crear_base()
    cursor = con.cursor()
    valor = tree.selection()
    item = tree.item(valor)
    mi_id = item["text"]
    mi_id = int(mi_id)
    data = (nombre, apellido, dni, fecha, categoria, mi_id)
    sql = "UPDATE socios SET nombre=?, apellido=?,  dni=?, fecha=?, categoria=? WHERE id= ?;"
    cursor.execute(sql, data)
    con.commit()
    actualizar_treeview(tree)


def f_borrar(
    entry_nombre,
    entry_apellido,
    entry_dni,
    entry_nacimiento,
    entry_categoria,
    bt_borrar,
    bt_modificar,
    bt_guardar,
    tree,
):
    bt_borrar["state"] = DISABLED
    bt_modificar["state"] = DISABLED
    if tree.selection():

        mi_id, valor = seleccionado(tree)
        con = crear_base()
        cursor = con.cursor()
        data = (mi_id,)
        sql = "DELETE FROM socios WHERE id = ?;"
        cursor.execute(sql, data)
        con.commit()
        tree.delete(valor)
        limpiar_campos(
            entry_nombre,
            entry_apellido,
            entry_dni,
            entry_nacimiento,
            entry_categoria,
        )
        bt_guardar["state"] = NORMAL

    else:
        f_error("No hay ningún ítem seleccionado")


def actualizar_treeview(mitreview):
    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)

    sql = "SELECT * FROM socios ORDER BY id DESC"
    con = crear_base()
    cursor = con.cursor()
    datos = cursor.execute(sql)

    resultado = datos.fetchall()
    for fila in resultado:
        mitreview.insert(
            "", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5])
        )


def f_error(un_string):
    showerror("ERROR", un_string)


def f_guardar(
    entry_nombre,
    entry_apellido,
    entry_dni,
    entry_nacimiento,
    entry_categoria,
    nombre,
    apellido,
    dni,
    nacimiento,
    categoria,
    tree,
):
    insertar(
        entry_nombre,
        entry_apellido,
        entry_dni,
        entry_nacimiento,
        entry_categoria,
        nombre.get(),
        apellido.get(),
        dni.get(),
        nacimiento.get(),
        categoria.get(),  # PERMITE GUARDAR AUNQUE EL CAMPO CATEGORIA ESTE VACIO. PORQUE????
        tree,
    )


def limpiar_campos(
    nombre, apellido, dni, nacimiento, categoria
):  # Vacia los campos de ingreso de datos

    nombre.delete(0, END)
    apellido.delete(0, END)
    dni.delete(0, END)
    nacimiento.delete(0, END)
    categoria.delete(0, END)

    nombre.insert(0, "")
    apellido.insert(0, "")
    dni.insert(0, "")
    nacimiento.insert(0, "")
    categoria.insert(0, "")


def f_modificar(
    entry_nombre,
    entry_apellido,
    entry_dni,
    entry_nacimiento,
    entry_categoria,
    nombre,
    apellido,
    dni,
    nacimiento,
    categoria,
    tree,
    bt_guardar,
    bt_modificar,
    bt_borrar,
):
    bt_modificar["state"] = DISABLED
    bt_borrar["state"] = DISABLED
    bt_guardar["state"] = NORMAL
    actualizar_bd(
        nombre.get(),
        apellido.get(),
        dni.get(),
        nacimiento.get(),
        categoria.get(),
        tree,
    )
    limpiar_campos(
        entry_nombre,
        entry_apellido,
        entry_dni,
        entry_nacimiento,
        entry_categoria,
    )
