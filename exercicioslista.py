#1

# lista=[]
# listaA=[]
# a=["a" , "A"]
# for i in range(1,6):
#     nome=input(f"Digite o nome: ")
#     lista.append(nome)
# for i in lista:
#         if i in a:
#             listaA.append(i)
# print(f"todos os nomes digitados:{lista}")
# print(f"todos os nomes que contém as letras Aa:{listaA}")

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

#4

# pares=[]
# for p in range(1,11):
#     par=int(input(f"Digite o número {p}: "))
#     pares.append(par)

# def filtrar_pares(pares):
#     for i in pares:
#         if i % 2 == 0:
#             print(f"Os pares são: {i}")

# filtrar_pares(pares)

#5

# numer=[]
# for r in range(1,9):
#     nu=int(input(f"Digite o número {r}: "))
#     numer.append(nu)

# maior=max(numer)
# menor=min(numer)
# soma=sum(numer)
# media=sum(numer) / r

# print(F"Maior número é: {maior}")
# print(F"Menor número é: {menor}")
# print(F"Soma dos números é: {soma}")
# print(F"Média dos números é: {media}")


#6

# numer=[]
# for r in range(1,11):
#     nu=int(input(f"Digite o número {r}: "))
#     numer.append(nu)
# v=int(input("Digite um número para remover da lista: "))

# def remover_elemento(numer, v):
#       nova_lista = [elemento for elemento in numer if elemento != v]
#       print(f"{nova_lista}")

# remover_elemento(numer, v)

#7

# convidados=[]
# for c in range(1,6):
#     con=input(f"Digite um nome {c}: ")
#     convidados.append(con)

# per=input("Qual nome deseja verificar na lista?: ")
# if per in convidados:
#     print("Convidado confirmado!")
# else:
#     print("Convidado não encontrado!")

#8

# soma = 0
# l=[]
# l2=[]
# for i in range(1,7):
#     n= float(input("Digite o número: "))
#     l.append(n)
# for i in l:
#     soma += i
#     if i >= 6:
#         l2.append(i)
# print(f"as notas são: {l}")
# print(f"a média foi {soma / i}")
# print(f"as notas acima de 6 ou igual a seis são: {l2}")

#9

# carrinho=[]
# for i in range(1,6):
#     produto=input(f"Adicione um produto {i}: ")
#     carrinho.append(produto)
# print(f"{carrinho}")

# remover=input("Deseja remover qual produto? ")
# if remover in carrinho:
#     carrinho.remove(remover)
#     print(f"Lista autoalizada: {carrinho}")

#10

# nomes=[]
# for i in range(1,8):
#     n=input(f"Digite o {i}° nome: ")
#     nomes.append(n)

# def filtrar_nomes(nomes):
#     nomes_filtrados = [nome for nome in nomes if len(nome) > 5]
#     print(f"{nomes_filtrados}")

# filtrar_nomes(nomes)