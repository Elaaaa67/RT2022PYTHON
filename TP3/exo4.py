def factorial_while(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
        print(f'{i-1}! = {result}')
    return result

def factorial_for(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        print(f'{i}! = {result}')
    return result

n = int(input("Entrez un nombre entier: "))
loop_type = input("Choisissez le type de boucle à utiliser (while/for): ")

if loop_type == "while":
    print(factorial_while(n))
else:
    print(factorial_for(n))