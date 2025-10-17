#1

# lista=[]
# for i in range(1,6):
#     nome=input(f"Digite o nome {i}: ")
#     lista.append(nome)
# print(f"{lista}")

# nao_comecam_com_a = 0
# for nome in lista:
#     if not nome.lower().startswith('a'):
#         nao_comecam_com_a += 1
#     print(nao_comecam_com_a)

#2

# notas=[]
# for n in range(1,5):
#     nota=float(input(f"Digite sua nota {n}: "))
#     notas.append(nota)

# def calcular_media(notas):
#     media=sum(notas) / 4
#     if media >= 7:
#         print("Está aprovado!")
#     else:
#         print("Está reprovado!")

# calcular_media(notas)

#3

# numeros = []
# for i in range(10):
#     numero = int(input(f"Digite o {i+1}º número inteiro: "))
#     numeros.append(numero)

# soma_pares = 0
# soma_impares = 0
# for numero in numeros:
#     if numero % 2 == 0:
#         soma_pares += numero
#     else:
#         soma_impares += numero

# print(f"A soma dos números pares é: {soma_pares}")
# print(f"A soma dos números ímpares é: {soma_impares}")

#4

# convidados=[]
# for c in range(1,6):
#     con=input(f"Digite um nome {c}: ")
#     convidados.append(con)

# per=input("Qual nome deseja verificar na lista?: ")
# if per in convidados:
#     print("Convidado confirmado!")
# else:
#     print("Convidado não encontrado!")

#5

# nomes=[]
# for i in range(1,8):
#     n=input(f"Digite o {i}° nome: ")
#     nomes.append(n)

# def filtrar_nomes(nomes):
#     nomes_filtrados = [nome for nome in nomes if len(nome) > 5]
#     print(f"{nomes_filtrados}")

# filtrar_nomes(nomes)

#6

# numeros=[]
# for a in range(1,7):
#     num=int(input(f"Digite o número {a}: "))
#     numeros.append(num)

# n=int(input("Digite um número para saber se está na lista: "))
# if n in numeros:
#     print(f"{n} está na lista!")
# else:
#     print(f"{n} não está na lista!")

# posição=numeros.index(n)
# print(f"O número {n} está na {posição} posição!")

#7

# n=int(input("Digite um número: "))
# def par_impar(n):
#     if n % 2 == 0:
#         return f"Esse número é par!"
#     else :
#         return f"Esse número é impar!"
# print(par_impar(n))

#8

# def contador(n):
#     n=10
#     while n <=10:
#         print(f"{n}")
#         n -= 1
#         if n<0:
#             break
#     print("Explosão!")
# contador(n=0)
