# QUESTÃO 1

# nome=input("digite seu nome:  ")
# def saudação(nome):
#         return f"Olá, {nome}! Seja bem-vindo ao curso de lógica de programação."
# print(saudação(nome))

# QUESTÃO 2

# n=int(input("Digite um número: "))
# def par_impar(n):
#     if n % 2 == 0:
#         return f"Esse número é par!"
#     else :
#         return f"Esse número é impar!"
# print(par_impar(n))

# QUESTÃO 3

# def com(a,b):
#     a=float(input("digite um numero:"))
#     b=float(input("digite outro numero:"))
#     if a>b:
#         return print(f"{a} é maior que {b}")
#     if a<b:
#         return print(f"{b} é maior que {a}")
#     else:
#         return print(f"{a} e {b} são iguais")
# com(a=0,b=0)   
    
# QUESTÃO 4

# def tabuada(n) :
#     n = int(input("digite um número e ,eu lhe direi sua tabuada:  "))
#     for i in range(1, 11):
#         print(f"{n} x {i} = {n * i}")
# tabuada(n=0)

# QUESTÃO 5

# def contador(n):
#     n=10
#     while n <=10:
#         print(f"{n}")
#         n -= 1
#         if n<0:
#             break
#     print("Explosão!")
# contador(n=0)

# QUESTÃO 6

# def con(n):
#     soma_notas=0
#     n=int(input("digite a quantidade de notas: "))
#     for i in range(n):
#         notas=float(input("digite a nota: "))
#         soma_notas += notas
#     print(soma_notas/n)
# con(n=0) 

# QUESTÃO 7

# def fatorial(n):
#     n = float(input("Digite um número: "))
#     fatorial = 1
#     i = 1
#     while i <= n:
#         fatorial *= i
#         i += 1
#     print(f"O fatorial de {n} é {fatorial}")
# fatorial(n=0)
    
# QUESTÃO 8

# def vogal(n):
#     contador=0
#     vogal = [ 'a' , 'A' , 'E' , 'e' , 'i' , 'I', 'O' , 'o' , 'u' , 'U']
#     n=input("Digite uma palavra:  ")
#     for v in vogal:
#         if v in n :
#            contador += 1  
#     print(f"{n} tem {contador} vogais!")
# vogal(n=0)

# QUESTÃO 9


# QUESTÃO 10

# eh_par = 0
# n = int(input("digite um número e lhe direi a soma de todos os pares até ele:  "))
# for i in range(n + 1):
#     if i % 2 == 0:
#         eh_par += i
# print(f"a soma dos números é: {eh_par}")    

# QUESTÃO 11 


# def adição(a,b):
#     a=float(input("Digite o valor do primeiro número da soma: "))
#     b=float(input("Digite o valor do segundo número da soma: "))
#     soma = (a+b)
#     return print(f"a soma é {soma}")

# def subtração(a,b):
#     a=float(input("Digite o valor do primeiro número da subtração: "))
#     b=float(input("Digite o valor do segundo número da subtração: "))
#     sub = (a-b)
#     return print(f"a subtração é {sub}")

# def multiplicação(a,b):
#     a=float(input("Digite o valor do primeiro número da multiplicação: "))
#     b=float(input("Digite o valor do segundo número da multiplicação: "))
#     multi = (a*b)
#     return print(f"a multiplicação é {multi}")

# def divisão(a,b):
#     a=float(input("Digite o valor do primeiro número da divisão: "))
#     b=float(input("Digite o valor do segundo número da divisão: "))
#     div = (a/b)
#     return print(f"a divisão é {div}")

# print("Bem vindo a calculadora!")
# operação= input("Digite a operação desejada entre [+] [-] [*] [/]: ")
# if operação == "+" :
#     adição(a=0,b=0)
# if operação == "-" :
#     subtração(a=0,b=0)
# if operação == "*" :
#     multiplicação(a=0,b=0)
# if operação == "/" :
#     divisão(a=0,b=0)

