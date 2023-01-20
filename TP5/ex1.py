n1 = str(input("Entrez un premier nom:"))
p1 = str(input(f"Entrez le prénom de {n1}:"))
n2 = str(input("Entrez un deuxieme nom:"))
p2 = str(input(f"Entrez le prénom de {n2}:"))

if n1 > n2:
    print(str.capitalize(p1), str.upper(n1))
    print(str.capitalize(p2), str.upper(n2))

elif n1 < n2:
    print(str.capitalize(p2), str.upper(n2))
    print(str.capitalize(p1), str.upper(n1))



