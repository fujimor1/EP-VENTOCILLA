#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:05:37 2024

@author: chapitec-alessandro
"""

import Gestion

def opciones():
    print("*** DATOS PERSONAS ***")
    print("1. Listar personas")
    print("2. Agregar personas")
    print("3. Salir")
    
def listar_archivos():
    print("-- Mostrar contenido de un archivo -- ")
    nombre = input("Archivo de los nombres: ")
    apellido = input("Archivo de los apellidos: ")
    dni = input("Archivo de los dni: ")
    print(Gestion.leer_archivo(nombre) + " \n" + Gestion.leer_archivo(apellido) + "\n" + Gestion.leer_archivo(dni))  

def agregar():
    print("-- Agregar Datos a un Archivo --")
    nombres = input("Archivo de los nombre: ")
    contenido_nombres = input("Contenido: ")
    print("")
    Apellido = input("Archivo de los apellidos: ")
    contenido_Apellido = input("Contenido: ")
    print("")
    DNI = input("Archivo de los dni: ")
    contenido_DNI = input("Contenido: ")
    
    Gestion.agregar_contenido_archivo(nombres, contenido_nombres)
    Gestion.agregar_contenido_archivo(Apellido, contenido_Apellido)
    Gestion.agregar_contenido_archivo(DNI, contenido_DNI)
    
def salir():
    print("Gracias por su visita....")
 
def error():
    print("Opción incorrecta")
    
opcion = 1
while opcion!=3:
    opciones()
    opcion = int(input("opcion: "))
    if opcion == 1:
        listar_archivos()
    elif opcion == 2:
        agregar()
    elif opcion == 3:
        salir()
    else:
        error()