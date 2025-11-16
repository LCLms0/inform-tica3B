import tabulate

def carregar_cardapio():
    print("------Canto do Palhano------")

    print("Salgados")
    salgados = [ 
    {"id": 1, "nome": "Coxinha", "preco": (f"R$ 5,00)") },
    {"id": 2, "nome": "Pastel (carne/queijo/frango)", "preco": (f"R$ 7,00)") },
    {"id": 3, "nome": "Enroladinho de Salsicha", "preco": (f"R$ 4,00)") },
    {"id": 4, "nome": "Empada (frango/palmito)", "preco": (f"R$ 6,00)") }, 
    ]

    print("Lanches / Sanduíches")
    lanches = [
    {"id": 5, "nome": "X-Salada", "preco": (f"R$ 14,00)") },
    {"id": 6, "nome": "X-Bacon", "preco": (f"R$ 18,00)") },
    {"id": 7, "nome": "Empada (frango/palmito)", "preco": (f"R$ 6,00)") },
    {"id": 8, "nome": "Empada (frango/palmito)", "preco": (f"R$ 6,00)") },
    ]

    print("Bebidas e Refrigerantes")
    bebidas = [
    {"id": 9, "nome": "Sucos", "preco": (f"R$ 5,00)") },
    {"id": 10, "nome": "Coca-cola", "preco": (f"R$ 10,00)") },
    {"id": 11, "nome": "Pepsi", "preco": (f"R$ 9,00)") },
    ]

def exibir_cardapio(cardapio):
    return(carregar_cardapio)
print(tabulate.tabulate(carregar_cardapio, headers='keys'))





