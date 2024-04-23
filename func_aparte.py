def filtro(lista,num):
    lista_nueva= list(filter(lambda x: len(x)>num,lista))
    return lista_nueva

# operaciones.py

contador_impares = lambda lista: len([x for x in lista if x % 2 != 0])
