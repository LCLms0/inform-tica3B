from main import *


def novo_pedido(cardapio):
    pedido={
        "ID": ,
        "Quantidade":,
        }
    itens=int(input("Digite o id do item para adicionar ao pedido: "))
    quant_itens=int(input("Digite a quantidade do item: "))
    if itens in cardapio["id"]:
        pedido["ID"] = itens
        print("Item adicionado com sucesso!")
    else:
        print("Id não encontrado!")
    pedido["Quantidade"] = quant_itens
    


    