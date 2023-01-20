i = 0
x = 0
y = 0
z = 0
while i < 10:
    x = int(input("Entrez une autre valeur:"))
    while not (0<= x <= 20):
        x = int(input("réessayer une autre valeur : "))
    i = i+1
    if x<10:
        x =x+1

else :
    if x>=15:
        y=y+1
    else:
        z=z+1

print(f"Il y a {x} Valeur strictement inferrieur à 10\n Il y a {y} supérieur ou égale à 10 et inférieur strictement à 15 \n Il y a {z} Le nombre de valeurs supérieur ou égale à 15" )