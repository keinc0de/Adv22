def lee(archivo):
    with open(archivo) as txt:
        return txt.read()

def marca(texto, n=4):
    for x in range(0, len(texto)):
        _ = texto[x:x+n]
        if len(set(_))==n:
            return {"caracteres":_, "i":x+n}

def marcador(archivo):
    print(f"pos marcador(4): {marca(lee(archivo))}")
    print(f"pos marcador(14): {marca(lee(archivo), 14)}")

marcador("dia6/datos.txt")

# a1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
# a2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
# a3 = "nppdvjthqldpwncqszvftbrmjlhg"
# a4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
# a5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
# print(marca(a1))
# print(marca(a2))
# print(marca(a3))
# print(marca(a4))
# print(marca(a5))