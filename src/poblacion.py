import csv 
from collections import namedtuple
from typing import NamedTuple

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero):
    with open(ruta_fichero, encoding='utf-8') as f:    
        lector = csv.reader(f)

        listaTuplas = list()
        for fila in lector:
            tupla = RegistroPoblacion(pais=fila[0],codigo=fila[1],año=int(fila[2]),censo=int(fila[3]))
            listaTuplas.append(tupla)

    return listaTuplas

"""
Indica que ruta fichero es un str y va a devolver una lista registro...
def lee_poblaciones(ruta_fichero: str) -> list[RegistroPoblacion]:

    res = []
    with open(ruta_fichero, encoding='utf-8') as f:    
        lector = csv.reader(f)

        for fila in lector:
            tupla = RegistroPoblacion(pais=fila[0],codigo=fila[1],año=int(fila[2]),censo=int(fila[3]))
            res.append(tupla)

    return listaTuplas
"""

def calcula_paises(poblaciones: list):
    res = []
    for i in poblaciones:
        if i.pais not in res:
            res.append(i.pais)

    return sorted(res)

"""
Hecho muy pronto pero se usará

def calcula_paises(poblaciones: list(RegistroPoblacion)) -> list[str]:
    res = set(p.pais for p in poblaciones) #es lo mismo que <dato> for iterador in contenedor
    return sorted(res)
"""

def filtra_por_pais(poblaciones, nombre_o_codigo):
    res = []

    for i in poblaciones:
        if nombre_o_codigo == i.censo or nombre_o_codigo == i.pais:
            res.append((i.año, i.censo))
    
    return res
    

def filtra_por_paises_y_anyo(poblaciones: list(RegistroPoblacion), anyo: int, paises: list) -> list:
    for i in paises:
        for e in poblaciones:
            if i in poblaciones.pais:
                if anyo < poblaciones.año:
                    

"""
Ejercicios Corregidos en clase

"""

