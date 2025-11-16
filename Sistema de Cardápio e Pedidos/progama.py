from funcoes import *

def menu():
    print("------Canto do Palhano------")

    print("------Menu------")

    print("[1] - Ver cardápio")
    print("[2] - Adicionar item ao pedido")
    print("[3] - Ver pedido")
    print("[4] - Remover item")
    print("[0] - Finalizar")

    while True:

        comando=int(input("Digite o comando: "))
        if comando == 1:
            exibir_cardapio()



menu()




