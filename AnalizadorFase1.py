#Analizador lexico - Inteligencia artificial - 2018
#import os
#from colorama import Fore
import sys

def menu():
    #os.system('cls')
    f_i = "proyecto analizador lexico sintactico.".capitalize()
    print(f_i.center(80,"="))
    print("\n\tSelecciona una opcion:")
    print("\t 1 - Listar tokens")
    print("\t 2 - Guardar token")
    print("\t 3 - Modificar token")
    print("\t 4 - Consultar token")
    print("\t 5 - Salir")

def imprimir(archivoNombre):
    try:
        with open(archivoNombre,'r') as sin_espacio:
            lineas = [linea.strip() for linea in sin_espacio] #elimina todos los espacios, tabulaciones, carácteres de nueva línea (\n) y retornos de carro (\r) tanto al principio como al final de la cadena.

        for linea in lineas:
            print(linea)
    except FileNotFoundError:
        print("El archivo no existe.")
    except AttributeError:
        print("Debes de ingresar un fichero.")

def imprimirCN(archivoNombre):
    with open(archivoNombre,'r') as sin_espacio:
        lineas = [linea.strip() for linea in sin_espacio]
    cont = 1
    for linea in lineas:
        print(str(cont)+ " " +linea)
        cont= cont+1

def mensajeCont():
    input("\n\t Pulsa ENTER para continuar")

def validar(palabra):
    with open("Tokens.txt") as tk:
        lista = [linea.strip() for linea in tk]
        for lineaC in lista:
            if palabra == lineaC:
                return True
    return False 

def modificar(ruta, fila, nuevo_dato):
    try:
        with open(ruta) as tk:
            lista = [linea.strip() for linea in tk]
            lista[fila-1] = nuevo_dato

        with open(ruta, mode='wt', encoding='utf-8') as st:
            st.write('\n'.join(lista))
        print("\tModificacion exitosa.!")
        print("\t Token: "+nuevo_dato+" agregado.")
    except:
        print("Error inesperado:", sys.exc_info()[0])
        raise


while True:
    menu()
    opcion = int(input("Digite la opcion: "))
    if opcion == 1: #Lista todos los tokens en el archivo txt
        imprimir("Tokens.txt")
        mensajeCont()
    elif opcion == 2: #Agrega un nuevo token al archivo txt
        Archiv = open("Tokens.txt","a+")
        palabra = input("Digite el nuevo token: ")
        if validar(palabra.upper()) == True:
            print("\tEl token ya existe.")
        else:
            Archiv.write('\n' + palabra.upper())
            Archiv.close()
            print("\tToken guardado.")
        mensajeCont()
    elif opcion == 3: #Modifica algun token en el archivo
        imprimirCN("Tokens.txt")
        fil = int(input("Digite el numero de la fila a cambiar: "))
        datoNuevo = input("Digite el token: ")
        modificar("Tokens.txt", fil, datoNuevo.upper())
        mensajeCont()
    elif opcion == 4: #Consulta un token en especifico
        '''listaTokens = open("Tokens.txt","r")
        contenido = listaTokens.read() #se guarda en la variable
        contenido = contenido.split("\n") ''' #se hace una lista en la que los elementos del archivo se separan por cada salto de linea
        palabraT = input("Digite el token a buscar: ")
        if validar(palabraT.upper()) == True:
            print("El token: "+palabraT.upper()+" ya existe.")
        else:
            print("El token: "+palabraT.upper()+" aun no ha sido agregado al archivo.")
            des = input("\t¿Desea agregar la palabra? - (s/n) ")
            if(des =="s"):
                Archiv = open("Tokens.txt","a+")
                Archiv.write('\n' + palabraT.upper())
                Archiv.close()
                print("\t\tToken guardado.")
            else:
                break
        mensajeCont()
    elif opcion == 5: #Fin del programa
        print("\t /// Fin del programa. ///\n\n")
        break
    else:
        print("")
        input("No has pulsado ninguna opcion valida ...\n Pulsa una tecla para continuar")
#Agrgar que al guardar valide la longitud de la palabra