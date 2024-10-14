#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 16:04:49 2024

@author: chapitec-alessandro
"""

def agregar_contenido_archivo(nombre, contenido):
    archivo = open(nombre, "at")
    archivo.write("\n" + contenido)
    archivo.close()

def leer_archivo(nombre):
    archivo = open(nombre, "rt", encoding='utf8')
    contenido = archivo.read()
    archivo.close()
    return contenido