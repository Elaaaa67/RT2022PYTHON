
x = input("Veuillez entrer la note du module 1 et le coefficient correspondant :")
y = x.split(" ")
n = int(y[0])
c = int(y[1])
m = n * c


x1 = input("Veuillez entrer la note du module 2 et le coefficient correspondant :")
y1 = x1.split(" ")
n1 = int(y1[0])
c1 = int(y1[1])
m1= n1 * c1


x2 = input("Veuillez entrer la note du module 3 et le coefficient correspondant :")
y2 = x2.split(" ")
n2 = int(y2[0])
c2 = int(y2[1])
m2 = n2 * c2


x3 = input("Veuillez entrer la note du module 4 et le coefficient correspondant :")
y3 = x3.split(" ")
n3 =int(y3[0])
c3 = int(y3[1])
m3 = n3 * c3


x4 = input("Veuillez entrer la note du module 5 et le coefficient correspondant :")
y4 = x4.split(" ")
n4 = int(y4[0])
c4 = int(y4[1])
m4 = n4 * c4

print(f"Voici la note 1 {n} et le coefficient {c}")
print(f"Voici la note 2 {n1} et le coefficient {c1}")

print(f"Voici la note 3 {n2} et le coefficient {c2}")
print(f"Voici la note 4 {n3} et le coefficient {c3}")
print(f"Voici la note 5 {n4} et le coefficient {c4}")


mn = m+m1+m2+m3+m4
mc = c+c1+c2+c3+c4

tt = mn / mc
print("la moyenne est de ",tt)



if n < 8 or n1 < 8 or n2 < 8 or n3 < 8 or n4 < 8:
    print("non admis")
    exit()

if tt >10:
    print("Vous etes admis")
else:
    print( "Non admis")



