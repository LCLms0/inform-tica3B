def soma():
    resultado = 0
    a = float(input("Digite o primeiro valor:  "))
    b = float(input("Digite o segundo valor:  "))
    print (a + b)

def subtracao():
    resultado = 0
    a = float(input("Digite o primeiro valor:  "))
    b = float(input("Digite o segundo valor:  "))
    print (a - b)

def multiplicacao():
    resultado = 0
    a = float(input("Digite o primeiro valor:  "))
    b = float(input("Digite o segundo valor:  "))
    print (a * b)

def divisao():
    resultado = 0
    a = float(input("Digite o primeiro valor:  "))
    b = float(input("Digite o segundo valor:  "))
    if b == 0:
        print("não é possivel dividir um número por zero.")
        b = float(input("Digite o segundo valor (novamente):  "))
    print (a / b)
