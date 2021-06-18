################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio Anagrama II
# UNRN Andina - Introducción a la Ingenieria en Computación
################
# Reemplazar por las funciones del ejercicio
from tp6ej1 import es_anagrama
def principal():
    archivo = open('anagramas.txt','r',encoding="UTF-8")
    for linea in archivo:
        textos=linea[:-1]
        texto = textos.split("–")
        if len(texto)==2:
            texto_uno = texto[0].strip()
            texto_dos = texto[1].strip()
            if es_anagrama(texto_uno,texto_dos):
                print(f"La palabra \"{texto_uno}\" y \"{texto_dos}\" son anagramas")
            else:
                print(f"La palabra \"{texto_uno}\" y \"{texto_dos}\" no son anagramas")
    archivo.close()
if __name__ == "__main__":
    principal()

