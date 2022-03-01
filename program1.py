import random

#print("Rechnen!")

#print("Ich multipliziere 2 Zahlen!")

#zahl1 = int(input("Faktor = "))
#zahl2 = int(input("Faktor = "))
#zahl3 = int(input("Faktor = "))
#zahl4 = int(input("Faktor = "))
#zahl5 = int(input("Faktor = "))
#zahl6 = int(input("Faktor = "))


#ergebnis = zahl6 * (zahl1 * zahl2 + zahl3 * zahl4 - zahl5)

#print("Produkt = {}".format(ergebnis))


#print("Gewonnen hat {}".format("Thorvid"))

alter = 9         # Variable Typ: ganzzahlig
name = "Philipp"  # Variable Typ: Zeichenkette

smile = """
  *****  
 *     *
*  * *  *
*       *
*   *   *
* *   * *
 * *** *
  *****
"""

#print(smile)

#print("Hallo {}, Dein Alter ist {}, ganz schön alt, wa?".format(name, alter))

x = 14
y = 15

a = x*y

versuchzahl = 20

print("{} Versuche: Rate eine Zahl".format(versuchzahl))

zahl = random.randrange(100)

for i in range(versuchzahl):
	z = int(input("Versuch {}: Zahl = ".format(i+1)))
	
	if z < zahl:
		print("zu klein")
	if z > zahl:
		print("zu groß")
	if z == zahl:
		print("Richtig, gewonnen!")
		exit()

