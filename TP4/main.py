n = int(input("donner une valeur"))
s =0
j=0
for i in range(n+1): # (0,1,2,3 .... n)
    s = s+i
    print(s)

print(s)

s =0
while j <= n:
    s = s + j
    print(s)
    j=j+1

print(s)