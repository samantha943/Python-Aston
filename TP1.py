TP Sabrina

'''Exo1
#!/usr/bin/python3

text= "Je dois faire des sauvegardes régulières de mes fichiers."
print(text*500)

'''

''' EXO2
#!/usr/bin/python3
print(list(range(1, 1000, 2)))
'''

''' Exo3
#!/usr/bin/python3

nb = 13
print(" 1 *", nb, "=", 1 * nb)
print(" 2 *", nb, "=", 2 * nb)
print(" 3 *", nb, "=", 3 * nb)
print(" 4 *", nb, "=", 4 * nb)
print(" 5 *", nb, "=", 5 * nb)
print(" 6 *", nb, "=", 6 * nb)
print(" 7 *", nb, "=", 7 * nb)
print(" 8 *", nb, "=", 8 * nb)
print(" 9 *", nb, "=", 9 * nb)
print("10 *", nb, "=", 10 * nb)
'''

''' Exo4
#!/usr/bin/python3

txt = input(" Entrez ce que vous désirez : ")

print(len(txt))
'''

'''Exo5
#!/usr/bin/python3

txt = int(input( " Entrez un nombre : "))
if txt%2 == 0:
    print("pair")
else:
    print("impair")
'''

'''Exo6
#!/usr/bin/python3


txt = int(input( " Entrez un nombre : "))

if txt > 20:
    print(" Trop Grand !!! ")


elif txt < 10:
        print(" Trop Petit !!! ")

else:
   print (" OK ")

'''

''' Exo 7

#!/usr/bin/python3

txt = int(input( " Entrez un nombre : "))

i = 0
while i < 11:
    print(" La suite est :  ", txt + i )
    i = i + 1



'''

''' Exo8
#!/usr/bin/python3

txt = int(input( " Entrez un nombre : "))

nb = txt
print(" 1 *", nb, "=", 1 * nb)
print(" 2 *", nb, "=", 2 * nb)
print(" 3 *", nb, "=", 3 * nb)
print(" 4 *", nb, "=", 4 * nb)
print(" 5 *", nb, "=", 5 * nb)
print(" 6 *", nb, "=", 6 * nb)
print(" 7 *", nb, "=", 7 * nb)
print(" 8 *", nb, "=", 8 * nb)
print(" 9 *", nb, "=", 9 * nb)
print("10 *", nb, "=", 10 * nb)

'''

'''Exo9

#!/usr/bin/python3

txt = int(input( " Entrez un nombre : "))

somme = 0

for i in range(1, txt + 1):
    somme = somme + i
print(("La somme des"), txt, ("premier entiers naturels est égale à"), somme)

'''

''' Exo10

#!/usr/bin/python3

txt = int(input( " Entrez Votre Age : "))


if txt == 6 or txt == 7:
    print(" Vous êtes Poussins!!! ")

elif txt == 8 or txt == 9:
        print(" Vous êtes Pupille !!! ")

elif txt == 10 or txt == 11:
        print(" Vous êtes Minimes !!! ")

elif txt >= 12:
        print(" Vous êtes Cadet!!! ")

else:
    print("Vous ne correspondez a aucune categories")

'''

''' Exo11

#!/usr/bin/python3

txt = int(input("Combien d'article Avez-vous pris ?"))
prix = float(input("quel est son prix ?"))
prixHT = txt*prix
TVA = prixHT * 1.20
print("Votre nombres d'articles est :", txt)
print("Prix HT :", prixHT)
print("Prix TTC :", TVA)

'''
