#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 15:09:18 2024

@author: chapitec-alessandro
"""


#Nombre de usuario
usuario = open("login.txt", "rt", encoding='utf8')
datos_usuario = usuario.read()  
usuario.close()

#Contrasenia
clave = open("clave.txt", "rt", encoding='utf8')
datos_clave = clave.read()
clave.close()


def mostrar_opciones():
    print("\nDatos Persona")
    print("1. Listar persona")
    print("2. Agregar persona")
    print("3. Salir")

username = input("Digite el usuario: ")
password = input("Digite la contrasenia: ")

if datos_usuario == username and datos_clave == password:
    print("Usuario válido")
    mostrar_opciones()
else:
    print("Usuario no válido")
    print("\n")

    username = input("Digite el usuario nuevamente: ")
    password = input("Digite la contrasenia nuevamente: ")

    if datos_usuario == username and datos_clave == password:
        print("Usuario válido")
        mostrar_opciones()
    else:
        print("Excediste los límites permitidos")



    

