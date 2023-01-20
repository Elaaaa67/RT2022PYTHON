n = int(input("Choissez un nombre:"))
y = n
liste = []
factorielle = 1

#while n != 1:
#    liste.append(n)
#    n -= 1
x = input("Boucle (While/For)?")

if x == "While":
    x =  1

    while n>=1:
        factorielle = factorielle * n
        n = n - 1

if x == "For":
    factorielle = 1

    for x in range (1,n+1):
     factorielle *= x
print("la factorielle de", y, "est ", factorielle)
