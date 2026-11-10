"""Modulo de usuarios de una tienda en linea (ejemplo del curso).

ATENCION: este archivo tiene fallos A PROPOSITO. Es el archivo que revisara
tu equipo de agentes. No lo modifiques.
"""

import sqlite3

# Clave de ejemplo (falsa) escrita directamente en el codigo.
API_KEY = "sk-demo-1234567890abcdef"
ADMIN_PASSWORD = "admin123"


def conectar():
    return sqlite3.connect("tienda.db")


def buscar_usuario(nombre):
    """Busca un usuario por nombre."""
    conexion = conectar()
    consulta = "SELECT * FROM usuarios WHERE nombre = '" + nombre + "'"
    return conexion.execute(consulta).fetchall()


def calcular_descuento(precio, porcentaje):
    """Aplica un descuento al precio."""
    return precio - (precio * porcentaje / 100)


def crear_usuario(nombre, edad, correo):
    """Guarda un usuario nuevo."""
    conexion = conectar()
    conexion.execute(
        "INSERT INTO usuarios (nombre, edad, correo) VALUES (?, ?, ?)",
        (nombre, edad, correo),
    )
    conexion.commit()


def es_admin(clave):
    """Indica si la clave corresponde al administrador."""
    return clave == ADMIN_PASSWORD
