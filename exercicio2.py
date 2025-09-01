# QUESTÃO 1 

# somafinal= 0
# for i in range (1 , 4 ) :
#     numero=float(input('Digite sua nota:  ') )  
#     somafinal += (numero)
# media= (somafinal)  / 3
# print(f"Sua média é : {media}  ")
# if media  < 7 :
#     print("você está reprovado !")
# else :
#     print('você foi aprovado !')

# QUESTÃO 2

# contador=0
# vogal = [ 'a' , 'A' , 'E' , 'e' , 'i' , 'I', 'O' , 'o' , 'u' , 'U']
# n=input("Digite uma palavra:  ")
# for v in vogal:
#     if v in n :
#         print(f'{v}')
#         contador += 1 
#         continue

# QUESTÃO 3 

# número= float(input("digite um número e lhe direi se ele é par ou impar: "))
# if  número % 2 :
#     print(f"{número} é impar ")
# else : 
#     print(f" {número} é par")

# QUESTÃO 4

# numeros=[]
# for i in range(1,6) :
#     numeros.append(int(input(f"Digite o {i}° número: ")))
# if numeros:
#     mai=max(numeros)
#     men=min(numeros)
#     print(f"Maior valor é: {mai}")
#     print(f"Menor valor é: {men}")

# QUESTÃO 5

#total = 0               
#mais_de_100 = 0        
#while True:
#    preço = float(input("Digite o valor do produto (0 para encerrar): "))
#    if preço == 0:
#        break 
#    total += preço    

  #  if preço > 100:
   #     mais_de_100 += 1
#print("Total da compra: R$", total)
#print("Produtos acima de R$100:", mais_de_100)


# QUESTÃO 6

# n = float(input("Digite um número: "))
# fatorial = 1
# i = 1
# while i <= n:
#    fatorial *= i
#    i += 1
# print(f"O fatorial de {n} é {fatorial}")
