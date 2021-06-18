################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio Descodificador
# UNRN Andina - Introducción a la Ingenieria en Computación
################
# Reemplazar por las funciones del ejercicio
def descifrado_del_cesar(texto,cantidad=1):
    """
    Esta funcion cifra descifra la funcion cifrado_del_cesar haciendo que recorra cada caracter de la variable texto
    el número de cantidad hacia de izquierda de su ubicacion
    volviendo a empezar cuando termina el caracter z-aZ-A9-0
    ejemplo b lo cifra en a y a lo cifra en z si la cantidad es 1 
    ejemplo e lo cifra en a y d lo cifra en z si la cantidad es 4
    ejemplo 1 lo cifra en 0 y 0 lo cifra en 9 si la cantidad es 1
    ejemplo 4 lo cifra en 0 y 3 lo cifra en 9 si la cantidad es 4
    """
    caracteres="";
    ascii_inicio_minuscula=97
    ascii_fin_minuscula=122
    ascii_inicio_mayuscula=65
    ascii_fin_mayuscula=90
    ascii_inicio_numero=48
    ascii_fin_numero=57
    caracter_codificado=0
    for c in texto:
        cod_ascii = ord(c)
        if (cod_ascii>=ascii_inicio_minuscula and cod_ascii<=ascii_fin_minuscula):#az
            caracter_codificado=cod_ascii-cantidad
            if caracter_codificado<ascii_inicio_minuscula:
                caracter_codificado = buscar_caracter_descifrado(caracter_codificado,ascii_inicio_minuscula,ascii_fin_minuscula)           
        elif (cod_ascii>=ascii_inicio_mayuscula and cod_ascii<=ascii_fin_mayuscula):#AZ
            caracter_codificado=cod_ascii-cantidad
            if caracter_codificado<ascii_inicio_mayuscula:
                caracter_codificado = buscar_caracter_descifrado(caracter_codificado,ascii_inicio_mayuscula,ascii_fin_mayuscula)           
        elif (cod_ascii>=ascii_inicio_numero and cod_ascii<=ascii_fin_numero):#numeros
            caracter_codificado = cod_ascii-cantidad
            if caracter_codificado<=ascii_inicio_numero:
                caracter_codificado = buscar_caracter_descifrado(caracter_codificado,ascii_inicio_numero,ascii_fin_numero)
        caracteres = caracteres+ chr(caracter_codificado)
    return caracteres
def buscar_caracter_descifrado(caracter_codificado,inicio_numero_ascii,fin_numero_ascii):
    """
    Esta funcion busca un caracter_codificado dentro de un intervalo [inicio_numero_ascii,fin_numero_ascii] y
    para buscarlo suma diferencia_min_may al numero a buscar hasta que esté dentro del intervalo y lo devuelve
    """
    diferencia_min_may=fin_numero_ascii-inicio_numero_ascii+1
    while  not caracter_codificado>=inicio_numero_ascii or not caracter_codificado<=fin_numero_ascii:
        caracter_codificado=caracter_codificado+diferencia_min_may 
    return caracter_codificado

def copiar_archivo_decodificado(nombre_archivo_entrada,rotacion):
    try:
        archivo_entrada= open(nombre_archivo_entrada, 'r')
        archivo_salida = open(nombre_archivo_entrada+".decode",'w')
        contenido_archivo_decodificado= descifrado_del_cesar(archivo_entrada.read(),rotacion)
        archivo_salida.write(contenido_archivo_decodificado)
        archivo_entrada.close()
        archivo_salida.close()
        return True
    except FileNotFoundError as e:
        return False
    
def principal():
    solicitar_archivo=True
    while solicitar_archivo:
        nombre_archivo=input("Ingrese el nombre del archivo a descodificar (.cesar):") 
        tamanio_texto= len(nombre_archivo)
        if nombre_archivo[-6:tamanio_texto+1]==".cesar":
            solicitar_archivo=False
    solicitar_rotacion=True
    while solicitar_rotacion:
        try:
            rotacion=int(input("Ingrese un número entero mayor a 0 para la rotacion de descodificación:"))
            if rotacion>0:
                solicitar_rotacion=False
        except:
            continue
    if copiar_archivo_decodificado(nombre_archivo,rotacion):
        print(f"El archivo '{nombre_archivo}' se ha descodificado como '{nombre_archivo}.decode'")
    else:
        print(f"No se ha podido descodificar el archivo '{nombre_archivo}'")
if __name__ == "__main__":
    principal()

