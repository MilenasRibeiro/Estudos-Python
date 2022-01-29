lis = [2, 4, 6, 8]
lis_a = ["Gato", "Cachorro", "Elefante"]
print ("\nA lista numerica é: ", lis)
print ("\nA lista de animais é: ", lis_a)
print("\nO elemento na posição 2 é: ",lis_a [2])
    
for x in lis_a:
    print("\n", x)
soma = 0

for y in lis:
    print("Os valores são: ", y)
    soma += y
    print("A soma é: ", soma)
    
print(sum(lis))

lis_a.sort()
print(lis_a)