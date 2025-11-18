import tabulate

def carregar_cardapio(cardapio):
    print("------Canto do Palhano------")
    salgados = [ 
    {"id": 1, "nome": "Coxinha", "preco":  (5.00)  },
    {"id": 2, "nome": "Pastel (carne/queijo/frango)", "preco": (7.00) },
    {"id": 3, "nome": "Enroladinho de Salsicha", "preco": (4.00) },
    {"id": 4, "nome": "Empada (frango/palmito)", "preco": (6.00)}, 
    ]
    lanches = [
    {"id": 5, "nome": "X-Salada", "preco": (14.00) },
    {"id": 6, "nome": "X-Bacon", "preco": (18.00) },
    {"id": 7, "nome": "Empada (frango/palmito)", "preco": (6.00) },
    {"id": 8, "nome": "Empada (frango/palmito)", "preco": (6.00) },
    ]
    bebidas = [
    {"id": 9, "nome": "Sucos", "preco": (5.00) },
    {"id": 10, "nome": "Coca-cola", "preco": (10.00) },
    {"id": 11, "nome": "Pepsi", "preco": (9.00) },
    ]
    cardapio.append(salgados)
    cardapio.append(lanches)
    cardapio.append(bebidas)
    print(cardapio)


def exibir_cardapio(cardapio):
    print(tabulate.tabulate(cardapio, headers='keys'))

def adicionar_pedido(cardapio, pedidos):
    id = int(input("Digite o ID do pedido:  "))
    qtd = int(input(f"Digite a quantidade de {id}:  "))
    for i in cardapio:
        if i["id"] == id:
            total = i * qtd
    pedindo =   {
    "item": "Hambúrguer",
    "qtd": qtd,
    "total": total,
    "ID" : id
    }
    pedidos.append(pedindo)


def exibir_pedido(pedidos):
    print(pedidos)
    print(sum([soma["total"] for soma in pedidos]))



def remover_item(pedidos):
    id = int(input("Digite o id do item que será removido:  "))


    for i in pedidos:
        if i["ID"] == id :
            pedidos.remove(i)
    

