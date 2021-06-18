################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio Codificador
# UNRN Andina - Introducción a la Ingenieria en Computación
################
# Reemplazar por las funciones del ejercicio
def buscar_caracter_cifrado(caracter_codificado,inicio_numero_ascii,fin_numero_ascii):
    """
    Esta funcion busca un caracter_codificado dentro de un intervalo [inicio_numero_ascii,fin_numero_ascii] y
    para buscarlo resta diferencia_min_may al numero a buscar hasta que esté dentro del intervalo y lo devuelve
    """
    diferencia_min_may=fin_numero_ascii-inicio_numero_ascii+1
    while not caracter_codificado>=inicio_numero_ascii or not caracter_codificado<=fin_numero_ascii:
        caracter_codificado=caracter_codificado-diferencia_min_may
    return caracter_codificado
def cifrado_del_cesar(texto,cantidad=1):
    """
    Esta funcion cifra la variable texto corriendo cada caracter el número de cantidad hacia de derecha de su ubicacion
    volviendo a empezar cuando termina el caracter a-zA-Z0-9
    ejemplo a lo cifra en b y z lo cifra en a si la cantidad es 1 
    ejemplo a lo cifra en e y z lo cifra en d si la cantidad es 4
    ejemplo 0 lo cifra en 1 y 9 lo cifra en 1 si la cantidad es 1
    ejemplo 0 lo cifra en 4 y 9 lo cifra en 5 si la cantidad es 4
    """
    caracteres="";
    ascii_inicio_minuscula=97
    ascii_fin_minuscula=122
    ascii_inicio_mayuscula=65
    ascii_fin_mayuscula=90
    ascii_inicio_numero=48
    ascii_fin_numero=57
    for c in texto:
        cod_ascii = ord(c)
        if (cod_ascii>=ascii_inicio_minuscula and cod_ascii<=ascii_fin_minuscula):#az
            caracter_codificado=cod_ascii+cantidad
            if caracter_codificado>ascii_fin_minuscula:
                caracter_codificado = buscar_caracter_cifrado(caracter_codificado,ascii_inicio_minuscula,ascii_fin_minuscula)                 
        elif (cod_ascii>=ascii_inicio_mayuscula and cod_ascii<=ascii_fin_mayuscula):#AZ
            caracter_codificado=cod_ascii+cantidad
            if caracter_codificado>ascii_fin_mayuscula:
                caracter_codificado = buscar_caracter_cifrado(caracter_codificado,ascii_inicio_mayuscula,ascii_fin_mayuscula)                 
        elif (cod_ascii>=ascii_inicio_numero and cod_ascii<=ascii_fin_numero):#numeros
            caracter_codificado = cod_ascii+cantidad
            if caracter_codificado>ascii_fin_numero:
                caracter_codificado = buscar_caracter_cifrado(caracter_codificado,ascii_inicio_numero,ascii_fin_numero)           
        caracteres = caracteres+ chr(caracter_codificado)
    return caracteres
def copiar_archivo_codificado(nombre_archivo_entrada,rotacion):
    try:
        archivo_entrada= open(nombre_archivo_entrada, 'r')
        archivo_salida = open(nombre_archivo_entrada+".cesar",'w')
        contenido_archivo_codificado= cifrado_del_cesar(archivo_entrada.read())
        archivo_salida.write(contenido_archivo_codificado)
        archivo_entrada.close()
        archivo_salida.close()
        return True
    except FileNotFoundError as e:
        return False
    
def principal():
    nombre_archivo=input("Ingrese el nombre del archivo a codificar:")
    solicitar_rotacion=True
    while solicitar_rotacion:
        try:
            rotacion=int(input("Ingrese un número entero mayor a 0 para la rotacion de codificación:"))
            if rotacion>0:
                solicitar_rotacion=False
        except:
            continue
    if copiar_archivo_codificado(nombre_archivo,rotacion):
        print(f"El archivo '{nombre_archivo}' se ha codificado como '{nombre_archivo}.cesar'")
    else:
        print(f"No se ha podido codificar el archivo '{nombre_archivo}'")
if __name__ == "__main__":
    principal()

