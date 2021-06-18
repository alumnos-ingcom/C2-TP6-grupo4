################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio Etiquetas HTML
# UNRN Andina - Introducción a la Ingenieria en Computación
################
# Reemplazar por las funciones del ejercicio
def hace_etiqueta(contenido, etiqueta):
    '''
    Retorna el contenido envuelto en una etiqueta como está indicado en el segundo argumento.
    La funcion llamada con contenido="Hola" y etiqueta="h1" retornará
    <h1>Hola</h1>
    '''
    etiqueta_apertura="<"+etiqueta+">"
    etiqueta_cierre="</"+etiqueta+">"
    return etiqueta_apertura+contenido+etiqueta_cierre    
def hace_comenta(contenido):
    '''
    Retorna el contenido envuelto en las marcas de comentario HTML
    <!--  -->
    (separen las marcas del contenido con un espacio)
    '''
    etiqueta_apertura="<!--"
    etiqueta_cierre="-->"
    return etiqueta_apertura+contenido+etiqueta_cierre
def principal():
    nombre_archivo=input("Ingrese un nombre para su archivo html: ")
    h1 = hace_etiqueta('Hola HTML', 'h1')
    h2 = hace_etiqueta('Este es otro título', 'h2')
    titulo_tabla = hace_etiqueta('Título para la tabla', 'h3')
    parrafo = hace_etiqueta('Esto es un párrafo', 'p')
    negrita= hace_etiqueta('texto en negrita','strong')
    cursiva= hace_etiqueta(' texto en cursiva ','i')
    tachado= hace_etiqueta(' texto tachado','s')
    otro_parrafo = hace_etiqueta('Esto es otro párrafo '+negrita+cursiva+tachado, 'p')
    titulo1=hace_etiqueta('Título 1','th')
    titulo2=hace_etiqueta('Título 2','th')
    titulo3=hace_etiqueta('Título 3','th')
    titulos =hace_etiqueta(titulo1+titulo2+titulo3,'tr')
    columna1=hace_etiqueta('fila 1 Columna 1','td')
    columna2=hace_etiqueta('fila 1 Columna 2','td')
    columna3=hace_etiqueta('fila 1 Columna 3','td')
    fila1 =hace_etiqueta(columna1+columna2+columna3,'tr')
    columna1=hace_etiqueta('fila 2 Columna 1','td')
    columna2=hace_etiqueta('fila 2 Columna 2','td')
    columna3=hace_etiqueta('fila 2 Columna 3','td')
    fila2 =hace_etiqueta(columna1+columna2+columna3,'tr')
    tabla = hace_etiqueta(titulos+fila1+fila2,'table')
    body = hace_etiqueta(h1+h2+parrafo+otro_parrafo+titulo_tabla+tabla,'body')
    titulo_de_la_pagina=hace_etiqueta('Título de la página','title')
    html = hace_etiqueta(titulo_de_la_pagina+body,'html')
    print(html)
    nombre_archivo = nombre_archivo+".html"
    try:
        archivo= open(nombre_archivo,'w')
        archivo.write(html)
        archivo.close()
        print(f"El archivo {nombre_archivo} se ha creado satisfactoriamente")
    except:
        print(f"No se ha podido crear el archivo {nombre_archivo}")
if __name__ == "__main__":
    principal()

