# QUESTÃO 1

# peso = float(input("Digite seu Peso corporal (em quilos):  "))
# altura= float(input("Digite sua altura (em metros):  "))
# imc = peso /    ( altura * altura ) 
# if imc < 18.5 :
#     print(f"Seu Índice de Massa Corporal é {imc} você está : Abaixo do peso")
# if imc >= 18.5   <=  24.9 :
#     print(f"Seu Índice de Massa Corporal é {imc} você está : Peso normal")
# if imc  >=25   <= 29.9 :
#     print(f"Seu Índice de Massa Corporal é {imc} você está : sobrepeso")
# if imc > 30  :
#     print(f"Seu Índice de Massa Corporal é {imc} você está : Obesidade")
# print("Fim do Programa")

# QUESTÃO 2

# n= int(input("Digite um número inteiro para eu lhe informar os números pares e impar até esse número:  "))
# for i in range(1,n + 1) :
#     if i % 2 == 0 :
#         print(f"{i} é par")
#     else :
#         print(f" {i} é impar")
    
# QUESTÃO 3

# n = int(input("Digite um número inteiro que vou lhe informar a tabuada desde número:  "))    
# print(f"Tabuada do {n}:")
# for i in range(1, 11):
#         print(f"{n} x {i} = {n * i}")

# QUESTÃO 4

n = float(input("Digite um número e lhe direi se ele é primo ou não:  "))
for i in range(2, int((n))):
    if n / i == 0 :    
        print(f"{n} não é Primo")    
    else:
        print(f"{n} é Primo!")

    