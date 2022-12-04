import txt

def elfoConMasCalorias(lista):
    sumas = []
    for elem in lista:
        sumas.append(sum(elem))
    mayorv = max(sumas)
    indice = sumas.index(mayorv)
    print(f"elfo({indice+1}): {mayorv} = {lista[indice]}")
    return indice+1

def tresConMasCalorias(lista):
    suma_total = 0
    li_mod = lista
    for x in range(3):
        mayor = elfoConMasCalorias(li_mod)
        indice = mayor-1
        total_calorias = sum(li_mod.pop(indice))
        suma_total += total_calorias
    return suma_total

# DATOS
dt_ejemplo = txt.listaSepPor("dia1_ejemplo.txt", sep="\n"*2, sep2="\n")
datos = txt.listaSepPor("dia1_datos.txt", sep="\n"*2, sep2="\n")
# DATOS PARTE 1
elfoConMasCalorias(dt_ejemplo)
elfoConMasCalorias(datos)

# DATOS PARTE 2
print(f"TOTAL CALORIAS(3 elfos): {tresConMasCalorias(dt_ejemplo)}")
print(f"TOTAL CALORIAS(3 elfos): {tresConMasCalorias(datos)}")