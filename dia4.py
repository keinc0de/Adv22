from pprint import pprint
# --- Day 4: Camp Cleanup ---

def lee(archivo):
    with open(archivo, "r") as txt:
        lineas = [l.replace("\n", "") for l in txt.readlines()]
    res = []
    for linea in lineas:
        pareja = linea.split(",")
        _ = []
        for par in pareja:
            _.append([int(n) for n in par.split("-")])
            #_.append(par.split("-"))
        res.append(_)
    return res

def contiene(lista=[[2, 8], [3, 7]]):
    # ERROR [[62, 96], [98, 98]],
    par1, par2 = lista
    #a = ",".join([str(n) for n in range(par1[0], par1[1]+1)]).replace(",", "")
    #b = ",".join([str(n) for n in range(par2[0], par2[1]+1)]).replace(",", "")
    a = ",".join([str(n) for n in range(par1[0], par1[1]+1)])
    b = ",".join([str(n) for n in range(par2[0], par2[1]+1)])
    #print(f"a: {a}")
    #print(f"b: {b}")
    return True if a in b or b in a else False

def contenido(lista=[[2, 8], [3, 7]]):
    par1, par2 = lista
    if par2[0]>=par1[0] and par2[1]<=par1[1]: # 2 in 1
        return True
    elif par1[0]>=par2[0] and par1[1]<=par2[1]: # 1 in 2
        return True
    else:
        return False

def cuantosContiene(lista):
    similares = []
    for pareja in lista:
        if contenido(pareja):
        #if contiene(pareja):
            similares.append(pareja)
    #pprint(similares)
    return len(similares)

def interseccion(lista=[[2, 8], [3, 7]]):
    par1, par2 = lista
    a = range(par1[0], par1[1]+1)
    b = range(par2[0], par2[1]+1)
    bo = False
    for num in a:
        if num in b:
            #print(a, " ", num, "in :", b)
            bo = True
            break
    return bo
def cuantosInterseccion(lista):
    similares = []
    for pareja in lista:
        if interseccion(pareja):
            similares.append(pareja)
    #pprint(similares)
    return len(similares)


# DATOS
lie = lee("dia4_ejemplo.txt")
lid = lee("dia4_datos.txt")
print("CUANTOS:")
# PARTE 1
print(f"contenidos(ejemplo): {cuantosContiene(lie)}")
print(f"contenidos(datos): {cuantosContiene(lid)}")

# PARTE 2
print(f"con interseccion(ejemplo): {cuantosInterseccion(lie)}")
print(f"con interseccion(datos): {cuantosInterseccion(lid)}")

