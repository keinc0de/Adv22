from pprint import pprint


def lee(archivo):
    with open(archivo, "r") as txt:
        return [l.replace("\n", "") for l in txt.readlines()]

def datosLinea(linea):
    _ = []
    for i in range(0, len(linea), 4):
        _.append(linea[i:i+3].replace('[','').replace(']','').strip())
    return _

def leerOrdenCajas(archivo):
    lineas = lee(archivo)
    datos = [datosLinea(linea) for linea in lineas]
    res = []
    for x in range(len(datos[0])):
        _ = []
        for lista in datos:
            _.append(lista[x])
        res.append([letra for letra in _[::-1] if letra!=""])
    return res

def leerMovimientos(archivo):
    _ = []
    for linea in lee(archivo):
        li = linea.split()
        _.append({li[0]:int(li[1]), f'{li[2]}_':int(li[3]), li[4]:int(li[5])})
    return _

def mueve(d, move=1, from_=0, to=0):
    for x in range(move):
        d[to-1].insert(len(d[to-1]), d[from_-1].pop())

def cajasArriba(orden_cajas, movimientos):
    cajas = leerOrdenCajas(orden_cajas)
    moves = leerMovimientos(movimientos)
    for mv in moves:
        mueve(cajas, **mv)
    res = ""
    for col in cajas:
        res += col[-1]
    return res
    # pprint(cajas)

print("MOVIENDO CAJAS: con grua modelo 9000")
# PARTE 1
print(f'cajas de arriba(ejemplo): {cajasArriba("dia5/cajas_e.txt", "dia5/me.txt")}')
print(f'cajas de arriba(datos): {cajasArriba("dia5/cajas.txt", "dia5/moves.txt")}')

def mueveDos(d ,move=1, from_=0, to=0):
    d[to-1].extend(d[from_-1][-move::])
    for x in range(move):
        d[from_-1].pop()

def cajasArriba9001(orden_cajas, movimientos):
    cajas = leerOrdenCajas(orden_cajas)
    moves = leerMovimientos(movimientos)
    for mv in moves:
        mueveDos(cajas, **mv)
    res = ""
    for col in cajas:
        res += col[-1]
    return res
    # pprint(cajas)

# PARTE 2
print("MOVIENDO CAJAS: con grua modelo 9001")
print(f'cajas de arriba(ejemplo): {cajasArriba9001("dia5/cajas_e.txt", "dia5/me.txt")}')
print(f'cajas de arriba(datos): {cajasArriba9001("dia5/cajas.txt", "dia5/moves.txt")}')
