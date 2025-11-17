from funcoes import *

def menu():
    
    print("------Canto do Palhano------")

    print("------Menu------")

    print("[1] - Ver cardápio")
    print("[2] - Adicionar item ao pedido")
    print("[3] - Ver pedido")
    print("[4] - Remover item")
    print("[0] - Finalizar")

    cardapio = []
    pedidos = []


    while True:

        try:
            comando = int(input("Digite o comando:  "))

        except ValueError:
            print("Comando inválido! Tente novamente!")
            continue  # volta pro início do while
        
        match comando:
            case  1 :
                carregar_cardapio(cardapio)
            case 2 :
                adicionar_pedido(cardapio, pedidos)
            case 3 :
                exibir_pedido(pedidos)
            case 4 : 
                remover_item(pedidos)
            case 0 :
                break
            case _ :
                print("Comando Invalido! Tente Novamente!")
                return


menu()




