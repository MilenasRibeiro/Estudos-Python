a = int(input("Digite a nota do primeiro bimestre: " ))
b = int(input("Digite a nota do segundo bimestre: "))
c = int(input("Digite a nota do terceiro bimestre: "))
d = int(input("Digite a nota do quarto bimestre: "))

media = (a + b + c + d)/4
if a <= 100 and b <= 100 and c <= 100 and d <= 100:
    print("A média de notas é:", media)
else: 
    print("Foi digitado alguma nota errada", )