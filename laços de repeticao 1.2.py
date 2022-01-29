a = int(input("Primeiro Bimestre: "))
while a > 100:
    a = int (input("Você digitou errado.Primeiro Bimestre: "))
    
b = int(input("Segundo Bimestre: "))
while b > 100:
    b = int (input("Você digitou errado.Segundo Bimestre: "))
    
c = int(input("Terceiro Bimestre: "))
while c > 100:
        c = int (input("Você digitou errado.Terceiro Bimestre: "))
        
d = int(input("Quarto Bimestre: ")) 
while d > 100:
            d = int (input("Você digitou errado.Quarto Bimestre: "))
media = (a + b + c + d)/ 4
print(" A média de notas é: ", media)