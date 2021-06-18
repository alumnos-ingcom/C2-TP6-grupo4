################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio Anagrama
# UNRN Andina - Introducción a la Ingenieria en Computación
################
# Reemplazar por las funciones del ejercicio
import collections
def quitar_espacios(lista_texto):
    i=0
    lista_aux=lista_texto
    for letra in lista_texto:
        if letra==" ":
            del lista_aux[i]
        i=i+1  
    return lista_aux
def pasar_a_minuscula(lista_texto):
    i=0
    lista_aux=lista_texto
    for letra in lista_texto:
        lista_aux[i]= letra.lower()
        i=i+1  
    return lista_aux

def es_anagrama(texto_uno,texto_dos):
    lista_texto_uno= list(texto_uno)
    lista_texto_dos= list(texto_dos)
    lista_texto_uno= pasar_a_minuscula(lista_texto_uno)
    lista_texto_dos= pasar_a_minuscula(lista_texto_dos)
    lista_texto_uno= quitar_espacios(lista_texto_uno)
    lista_texto_dos= quitar_espacios(lista_texto_dos)
    return collections.Counter(lista_texto_uno)==collections.Counter(lista_texto_dos)
def principal():
    texto_uno = input("Ingrese una cadena de texto:")
    texto_dos = input("Ingese otra cadena de texto:")
    if es_anagrama(texto_uno,texto_dos):
        print(f"La palabra \"{texto_uno}\" y \"{texto_dos}\" son anagramas")
    else:
        print(f"La palabra \"{texto_uno}\" y \"{texto_dos}\" no son anagramas")

if __name__ == "__main__":
    principal()

