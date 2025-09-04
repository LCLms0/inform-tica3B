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

# n = int(input("Digite um número e lhe direi se ele é primo ou não:  "))
# eh_primo = True
# for i in range(2,n):
#     if n % i == 0:
#         eh_primo = False 
# if eh_primo:
#     print(f'{n} é primo') 
# else:
#     print(f"{n} não é primo")        

# QUESTÃO 5

# alunosquepassaram=0
# alunosquenãopassaram=0
# somanotas=0
# alunos=int(input("digite a quantidade de alunos: "))
# for i in range(0,alunos) :
#     nota=float(input("digite a nota do aluno: "))
#     somanotas += nota
#     if nota <= 6 :
#         alunosquepassaram += 1
#     if nota > 6 :
#         alunosquenãopassaram +=1
# media= somanotas/alunos
# print(f" media da turma foi: {media}")
# print(f"a quantidade que passou foi {alunosquepassaram}")
# print(f"a quantidade que não passou foi {alunosquenãopassaram}")

# QUESTÃO 6

# import random
# print("BEM VINDO AO JOGO DE ADIVINHAÇÕES!") 
# print("REGRAS: 1 - TENTE ADIVINHAR O NÚMERO SECRETO")
# n_aleatorio = 0 
# pontuação = 0
# for n in range(1 , 20):
#     n_aleatorio=int(random.Random())
#     n_usuario= int(input("Tente adivinhar o número:  "))
#     if n_usuario < n_aleatorio :
#         print("quase lá...tente novamente mas com um número menor.")
#         continue
#     if n_usuario > n_aleatorio :
#         print("quase lá...tente novamente mas com um número maior.")
#         continue
#     if n_usuario == n_aleatorio :
#         print("você acertou!!! Ganhou + 100 de pontuação ! (digite 0 para parar)")
#         pontuação += 100
#         continue
#     if n_aleatorio == 0 :
#         break
# import time
# print(f"Sua Pontuação Final foi...")
# time.sleep(3)
# print(f"{pontuação}!!!") 
