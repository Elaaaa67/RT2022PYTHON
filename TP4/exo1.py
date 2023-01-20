x = float(input("Vous cherchez la table de multiplication de quel nombre ?:"))
i=0
l1 =[]
for i in range(0,10,1):
    l1.append([x,i,x*i])

for i in l1:
    print(f"{i[0]} * {i[1]} = {i[2]}")

print("L1")