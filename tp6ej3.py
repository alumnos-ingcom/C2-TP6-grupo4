################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio Copiadora
# UNRN Andina - Introducción a la Ingenieria en Computación
################
# Reemplazar por las funciones del ejercicio
def copiar_archivo(nombre_archivo_entrada,nombre_archivo_salida):
    try:
        archivo_entrada= open(nombre_archivo_entrada, 'r',encoding="UTF-8")
        archivo_salida = open(nombre_archivo_salida,'a')
        archivo_salida.write(archivo_entrada.read())
        archivo_entrada.close()
        archivo_salida.close()
        return True
    except FileNotFoundError as e:
        return False
    
def principal():
    nombre_archivo_entrada=input("Ingrese el nombre del archivo de entrada:")
    nombre_archivo_salida=input("Ingrese el nombre del archivo de salida:")
    if copiar_archivo(nombre_archivo_entrada,nombre_archivo_salida):
        print(f"El contenido del archivo '{nombre_archivo_entrada}' se ha copiado al archivo '{nombre_archivo_salida}'")
    else:
        print(f"No se ha podido copiar el archivo '{nombre_archivo_entrada}' ha '{nombre_archivo_salida}'")
if __name__ == "__main__":
    principal()

