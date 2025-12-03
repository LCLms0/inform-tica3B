import tabulate 
from main import *

def carregar_cardapio(cardapio) :
    return cardapio

def exibir_cardapio(cardapio):
    print(tabulate(cardapio, headers="keys", tablefmt="fancy_grid"))


def buscar_item(cardapio, id_item):
    id = int(input("Digite o id do pedido: "))
    for i in cardapio:
        for e in i:
            if e == id:
                id_itens.append(i)
    return id_itens

