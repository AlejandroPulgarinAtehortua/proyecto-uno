archivo=open("numeros.txt","r")
archivo2=open("resultado.txt", "w")

def funcion(x):
    return 2*x+1


lineas=archivo.readlines()
for lineas in lineas:
    x=int(lineas)
    y=funcion(x)
    print(y)
    y=str(y)
    archivo2.write(y)
    archivo2.write("\n")
    
# siempre que se abre un archivo asegurarse de cerrarlo
archivo.close()
archivo.close()