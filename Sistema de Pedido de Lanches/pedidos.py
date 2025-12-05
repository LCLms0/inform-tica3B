from main import *


def novo_pedido(cardapio):
    pedido=[]
    quant_itens=int()
    itens=int(input("Digite o id do item para adicionar ao pedido: "))
    if itens in cardapio["id"]:
        pedido.append(itens)
        print("Item adicionado com sucesso!")
    


    