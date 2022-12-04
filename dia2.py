import txt


def piedraPapelTijeras(tu_elegiste, yo_elegi):
    if tu_elegiste==yo_elegi:
        res = "empate"
    else:
        if tu_elegiste=="piedra" and yo_elegi=="papel":
            res = "gane"
        elif tu_elegiste=="piedra" and yo_elegi=="tijeras":
            res = "perdi"
        elif tu_elegiste=="papel" and yo_elegi=="piedra":
            res = "perdi"
        elif tu_elegiste=="papel" and yo_elegi=="tijeras":
            res = "gane"
        elif tu_elegiste=="tijeras" and yo_elegi=="piedra":
            res = "gane"
        elif tu_elegiste=="tijeras" and yo_elegi=="papel":
            res = "perdi"
    return {"resultado":res, "tu":tu_elegiste, "yo":yo_elegi}

def miPuntaje(forma1, forma2):
    res = piedraPapelTijeras(forma1, forma2)
    por_partida, por_forma = 0, 0
    if res.get('resultado')=='gane':
        por_partida += 6
    elif res.get('resultado')=='empate':
        por_partida += 3
    
    if res.get('yo')=='piedra':
        por_forma += 1
    elif res.get('yo')=='papel':
        por_forma += 2
    elif res.get('yo')=='tijeras':
        por_forma += 3
    puntaje = por_partida + por_forma
    # print(
    #     f"{res.get('resultado'):>6} {puntaje}: "\
    #     f"partida({por_partida}) + forma({por_forma}) "\
    #     f"{forma1:>7} vs {forma2:<7}"
    # )
    return puntaje

def traduceLetra(letra):
    if letra in "AX":
        forma = "piedra"
    elif letra in "BY":
        forma = "papel"
    elif letra in "CZ":
        forma = "tijeras"
    return forma

def puntajeUsandoGuia(guia):
    puntaje = 0
    for codigo in guia:
        oponente =  traduceLetra(codigo[0])
        yo = traduceLetra(codigo[1])
        puntaje += miPuntaje(oponente, yo)
    return puntaje

def jugada(forma, accion):
    res = ""
    if accion=="ganar":
        if forma=="piedra":
            res = "papel"
        elif forma=="tijeras":
            res = "piedra"
        elif forma=="papel":
            res = "tijeras"
    elif accion=="perder":
        if forma=="piedra":
            res = "tijeras"
        elif forma=="tijeras":
            res = "papel"
        elif forma=="papel":
            res = "piedra"
    elif accion=="empate":
        res = forma
    return res

def traduceLetras(letra1, letra2):
    oponente = traduceLetra(letra1)
    if letra2=="X":
        forma2 = jugada(oponente, accion="perder")
    elif letra2=="Y":
        forma2 = jugada(oponente, accion="empate")
    elif letra2=="Z":
        forma2 = jugada(oponente, accion="ganar")
    return oponente, forma2

def puntajeUsandoGuiaModo2(guia):
    puntaje = 0
    for codigo in guia:
        oponente, yo = traduceLetras(codigo[0], codigo[1])
        puntaje += miPuntaje(oponente, yo)
    return puntaje

# DATOS EJEMPLO
# _g = txt.listaDeListas(archivo="dia2_ejemplo.txt", sep="\n", sep2=" ")
# print(_g)
# print(f"PUNTAJE TOTAL (ejemplo): {puntajeUsandoGuia(_g)}")

# DATOS
data1 = txt.listaDeListas("dia2_datos.txt", sep="\n", sep2=" ")
# print(data1)
# PARTE 1
print(f"PUNTAJE TOTAL(P1): {puntajeUsandoGuia(data1)}")

# DATOS EJEMPLO PARTE 2
# print(f"PUNTAJE TOTAL (ejemplo2): {puntajeUsandoGuiaModo2(_g)}")
# PARTE 2
print(f"PUNTAJE TOTAL(P2): {puntajeUsandoGuiaModo2(data1)}")
