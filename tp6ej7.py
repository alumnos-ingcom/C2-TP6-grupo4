################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio Etiquetas HTML parte 2 (opcional)
# UNRN Andina - Introducción a la Ingenieria en Computación
################
# Reemplazar por las funciones del ejercicio
def hace_etiqueta_con_atributos(contenido, etiqueta,diccionario_atributos={}):
    '''
    Retorna el contenido envuelto en una etiqueta como está indicado en el segundo argumento y sus atributos.
    La funcion llamada con contenido="Hola" y etiqueta="h1" retornará
    <h1>Hola</h1> y contenido="Texto del enlace" y etiqueta="a" diccionario_atributos={"href" : "https://www.unrn.edu.ar"}
    <a href="https://www.unrn.edu.ar">Texto del enlace</a>
    '''
    atributos=''
    for atributo in diccionario_atributos:
        atributos= atributos+' '+atributo+"="+'"'+diccionario_atributos[atributo]+'"'
    etiqueta_apertura="<"+etiqueta+atributos+">"
    etiqueta_cierre="</"+etiqueta+">\n"
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
    h1 = hace_etiqueta_con_atributos('Hola HTML', 'i')
    h1 = hace_etiqueta_con_atributos(h1, 'u')
    h1= hace_etiqueta_con_atributos(h1, 'h1')
    h2 = hace_etiqueta_con_atributos('Este es otro título', 'h2')
    titulo_tabla = hace_etiqueta_con_atributos('Título para la tabla', 'h3')
    parrafo = hace_etiqueta_con_atributos('Esto es un párrafo', 'p')
    negrita= hace_etiqueta_con_atributos('texto en negrita','strong')
    cursiva= hace_etiqueta_con_atributos(' texto en cursiva ','i')
    tachado= hace_etiqueta_con_atributos(' texto tachado','s')
    diccionario_enlace = {"href" : "https://www.unrn.edu.ar","target":"_blank"}
    enlace = hace_etiqueta_con_atributos(' Texto del enlace ','a',diccionario_enlace)
    diccionario_imagen= {"src" : "https://www.unrn.edu.ar/images/favicon/apple-touch-icon-152x152.png"}
    imagen = hace_etiqueta_con_atributos(' Texto imagen ','img',diccionario_imagen)
    imagen_unrn = hace_etiqueta_con_atributos('','img',diccionario_imagen)
    imagen_con_enlace = hace_etiqueta_con_atributos(imagen_unrn,'a',diccionario_enlace)
    salto_de_linea=hace_etiqueta_con_atributos('','br')
    otro_parrafo = hace_etiqueta_con_atributos('Esto es otro párrafo '+negrita+cursiva+tachado+enlace+imagen+salto_de_linea+imagen_con_enlace, 'p')
    diccionario_stylos_th1= {"style" : "color:red"}
    diccionario_stylos_th2= {"style" : "color:blue"}
    diccionario_stylos_th3= {"style" : "color:orange"}
    titulo1=hace_etiqueta_con_atributos('Título 1','th',diccionario_stylos_th1)
    titulo2=hace_etiqueta_con_atributos('Título 2','th',diccionario_stylos_th2)
    titulo3=hace_etiqueta_con_atributos('Título 3','th',diccionario_stylos_th3)
    titulos =hace_etiqueta_con_atributos(titulo1+titulo2+titulo3,'tr')
    columna1=hace_etiqueta_con_atributos('fila 1 Columna 1','td')
    columna2=hace_etiqueta_con_atributos('fila 1 Columna 2','td')
    columna3=hace_etiqueta_con_atributos('fila 1 Columna 3','td')
    fila1 =hace_etiqueta_con_atributos(columna1+columna2+columna3,'tr')
    columna1=hace_etiqueta_con_atributos('fila 2 Columna 1','td')
    columna2=hace_etiqueta_con_atributos('fila 2 Columna 2','td')
    columna3=hace_etiqueta_con_atributos('fila 2 Columna 3','td')
    fila2 =hace_etiqueta_con_atributos(columna1+columna2+columna3,'tr')
    tabla = hace_etiqueta_con_atributos(titulos+fila1+fila2,'table')
    diccionario_estilos_div= {"style" : "width:800px;background:#ccc;margin:auto;padding:5px;"}
    contenido =hace_etiqueta_con_atributos(h1+h2+parrafo+otro_parrafo+titulo_tabla+tabla,'div',diccionario_estilos_div)
    body = hace_etiqueta_con_atributos(contenido,'body')
    titulo_de_la_pagina=hace_etiqueta_con_atributos('Título de la página','title')
    html = hace_etiqueta_con_atributos(titulo_de_la_pagina+body,'html')
    print(html)
    nombre_archivo = "pagina.html"
    try:
        archivo= open(nombre_archivo,'w')
        archivo.write(html)
        archivo.close()
        print(f"El archivo {nombre_archivo} se ha creado satisfactoriamente")
    except:
        print(f"No se ha podido crear el archivo {nombre_archivo}")
if __name__ == "__main__":
    principal()

