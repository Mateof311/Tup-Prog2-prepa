from func_aparte import*
"""
Escribe un programa que pida al usuario ingresar su edad y luego imprima un mensaje
indicando si es mayor de edad o no
"""
def mayor_edad():
    edad = int(input("Ingrese su edad:"))
    if(edad<18):
        print("Usted es menor de edad")
    else:
        print("Felicidades, ya es mayor de edad")

#mayor_edad()
"""
Escribe un programa que itere sobre un diccionario e 
imprima solo las claves que sean strings.
"""
def claves_str(diccionario):
    for clave in diccionario.keys():
        if type(clave) is str:
            print(clave)

dic={"perro":"guau",38:66,"4444":45,45:"77777"}
#claves_str(dic)
"""
Escribe una función que devuelve una copia de una lista en orden invertido.
"""
def lista_inv(lista):
    nueva_lista=[]
    for i in range(len(lista)-1,-1,-1):
        nueva_lista.append(lista[i])

    return nueva_lista

#print(lista_inv([1,2,3,4,5,4,"perro"]))

"""
Escribe una función que filtre las palabras de una lista que comiencen con una letra
específica utilizando una expresión lambda
"""
def primera_vocal(lista,letra):
    nueva_lista=list(filter(lambda x: x.startswith(letra), lista))
    return nueva_lista

listaej=["perro","gato","patio","auto"]
#print(primera_vocal(listaej,"p"))

"""
En un módulo separado, escribe una función que filtre los elementos de una lista de
string qué su longitud sea mayor a x (pasado cómo parámetro) utilizando una expresión
lambda.
"""
listafilter=["perrrrro","ss","fdfdfdfd","ddddd","ksksksksksk"]
#print(filtro(listafilter,5))
"""
En un módulo separado, crear una función lambda que cuente la cantidad de números
pares de una lista.
"""
lista_num=[1,2,3,4,5,6,7]
print(contador_impares(lista_num))
