def lista_lineas(archivo):
    with open(archivo, "r") as txt:
        return [linea.replace("\n", "") for linea in txt.readlines()]

def lee(archivo):
    with open(archivo, "r") as txt:
        return txt.read()

def listaSepPor(archivo, sep, sep2=None):
    res = []
    _ = lee(archivo).split(sep)
    if sep2 is None:
        res = _
    else:
        for texto in _:
            res.append([int(x) for x in texto.split(sep2) if x.isdigit()])
    return res

def listaDeListas(archivo, sep, sep2=None):
    res = []
    _ = lee(archivo).split(sep)
    if sep2 is None:
        res = _
    else:
        for texto in _:
            res.append([x for x in texto.split(sep2)])
    return res

if __name__=="__main__":
    file = "datos_d1a.txt"
    li = listaSepPor(file, "\n"*2, "\n")
    print(li)