x =int(input("Entrez un nombre entier: "))

if x >0 :
    msg="Le nombre est positif"

    if x%2==0:
        msg+=" et pair"
    else:
        msg += " et impair"

elif x <0:
    msg= "Le nombre est négatif"

    if x%2==0:
        msg+=" et pair"
    else:
       msg+=" et impair"

else:
     msg="Le zéro est positif et pair"

print(f"{msg}")
