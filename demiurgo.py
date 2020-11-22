#El demiurgo nos sirve para gestionar archvos
#modos de apertura:
# r: solo lectura 
# w: escritura(crea el archivo si no existe)
# a: (append). va el final del archivo y agrega(crea el archivo si no existe)
# r+: lectura y escritura (si el archivo no existe saca un error)
# w+ lecrura y escritura (si el archivo no existe lo crea)
# a+: lectura y escritura (crea el archivo si no existe) y los datos se agregan al final


archivo=open("numeros.txt","r")
linea=archivo.readline() #lee una linea
print(linea)
linea=archivo.readline() #lee la siguiente linea
print(linea)

#cuando son muchos datos
# while linea != "":
#     linea=archivo.readline() #lee la siguiente linea
#     print(linea)

while linea != "":
    linea=archivo.readline() #lee la siguiente linea
    linea=int(linea)
    print(linea+1)

# siempre que se abre un archivo asegurarse de cerrarlo
archivo.close()
