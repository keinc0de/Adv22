import txt

lie = txt.listaDeListas("dia2_ejemplo.txt", "\n")
lid = txt.listaDeListas("dia2_datos.txt", "\n")
print(lie)
# AX PIEDRA
# BY PAPEL
# CZ TIJERAS

def obtenPuntaje(lista):
	puntaje_total = 0
	for elem in lista:
		puntaje = 0
		if "X" in elem:
			puntaje+=1
		elif "Y" in elem:
			puntaje+=2
		elif "Z" in elem:
			puntaje+=3
		
		if elem in ["C X", "A Y", "B Z"]:
			puntaje+=6
		elif elem in ["A X", "B Y", "C Z"]:
			puntaje+=3
		#print(puntaje)
		puntaje_total += puntaje
	return puntaje_total
		
#print(f"TOTAL(e1): {obtenPuntaje(lie)}")
#print(f"TOTAL(P1): {obtenPuntaje(lid)}")

def obtenPuntajeDos(lista):
	puntaje_total = 0
	for elem in lista:
		puntaje = 0
		if "X" in elem:
			puntaje+=1
		elif "Y" in elem:
			puntaje+=2
		elif "Z" in elem:
			puntaje+=3
		print("p", puntaje)
		if elem in ["B Z", "C X"]:
			puntaje+=6
		elif elem in ["A X", "B Y", "C Z", "A Y", "B Y", "C Y"]:
			puntaje+=3
		print(puntaje)
		puntaje_total += puntaje
	return puntaje_total

print(f"TOTAL(e1): {obtenPuntajeDos(lie)}")
#print(f"TOTAL(P2): {obtenPuntajeDos(lid)}")