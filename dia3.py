from pprint import pprint

orden = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def lee(archivo):
    with open(archivo, "r") as txt:
        return [linea.replace("\n", "") for linea in txt.readlines()]

lie = lee("dia3_ejemplo.txt")
lid = lee("dia3_datos.txt")
# pprint(lid)
# pprint(lie)
def sumaPorCompartimento(lista):
    suma = 0
    for productos in lista:
        mitad = len(productos)//2
        compartimento1 = productos[:mitad]
        compartimento2 = productos[mitad:]
        rep = ""
        for articulo in compartimento1:
            if articulo in compartimento2:
                rep += articulo
                break
        i = orden.index(rep)+1
        # print(i, rep)
        suma += i
    return suma
# DATOS EJEMPLO
print("SUMA PRIORIDADES")
print(f"por compartimento(ejemplo1): {sumaPorCompartimento(lie)}")
print(f"por compartimento(datos): {sumaPorCompartimento(lid)}")

def sumaPorGrupoInsignia(lista):
    suma = 0
    for x in range(0, len(lista), 3):
        rep = ""
        for articulo in lista[x]:
            if articulo in lista[x+1] and articulo in lista[x+2]:
                rep += articulo
                break
        i = orden.index(rep)+1
        # print(i, rep)
        suma+=i
    return suma

print(f"por grupo Insignia(ejemplo): {sumaPorGrupoInsignia(lie)}")
print(f"por grupo Insignia(datos): {sumaPorGrupoInsignia(lid)}")

def sumaPC(li):
    # res = [a for p in li for a in p[:(len(p)//2)] if a in p[(len(p)//2):]]
    # suma = sum([orden.index(a)+1 for a in set(res)])
    suma = 0
    for p in li:
        mitad = len(p)//2
        _ = ""
        for a in p[:mitad]:
            if a in p[mitad:]:
                _+=a
                break
        i = orden.index(_)+1
        suma+=i
    return suma
# print(f"compartimento(ejemplo): {sumaPC(lie)}")
# print(f"compartimento(datos): {sumaPC(lid)}")