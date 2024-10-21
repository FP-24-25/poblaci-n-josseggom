from poblacion import *

ruta_fichero = "C:\\Users\\joans\\Documents\\FP\\poblaci-n-josseggom\\data\\population.csv"

def test_lee_poblaciones(ruta_fichero):
    contenido = lee_poblaciones(ruta_fichero)
    return contenido

"""
def test_lee_poblaciones(datos: list[RegistroPoblacion]):
    contenido = lee_poblaciones(ruta_fichero)
    print("\n".join(str))
    return datos
"""

def test_calcula_paises(registros):
    listaPaises = calcula_paises(registros)
    print(len(listaPaises))
    print(listaPaises)

def test_filtra_por_pais(registros, codigo_o_censo):
    listaFiltradas = filtra_por_pais(registros, codigo_o_censo)
    print(listaFiltradas)

registros = test_lee_poblaciones(ruta_fichero)
#test_calcula_paises(registros)
registrosFiltrados = test_filtra_por_pais(registros, 2038637)

