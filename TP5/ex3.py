neyney= input("Entrez une letre:")
neyney = neyney.lower()
neyney_lol = ""


for c in neyney:
    if neyney.isalpha():
        neyney_lol += c

if neyney_lol == neyney_lol[::-1]:
    print("C'est un Palindromes")
else:
    print(" ce n'est pas un Palindromes")

