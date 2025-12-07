from cardapio import *
from pedidos import *
from relatorios import *

def main():
    cardapio = carregar_cardapio()
    pedidos = []
    id_p = 1


while True:

    print("------MENU------")
    print("[1] - Exibir cardápio")
    print("[2] - Fazer um novo pedido")
    print("[3] - Listar pedidos ")
    print("[4] - Buscar pedido por ID ")
    print("[5] - Relatório financeiro ")
    print("[6] - Sair")

    op = input("Opção: ")

    if op == "1":
        exibir_cardapio(cardapio)
    
    elif op == "2":
        pedido = novo_pedido(cardapio)
        pedido["id"] = id_p
        calcular_total(pedido, cardapio)
        pedidos.append(pedido)
        exibir_pedido(pedido, cardapio)
        id_p += 1


