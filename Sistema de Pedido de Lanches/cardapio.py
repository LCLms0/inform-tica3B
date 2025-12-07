def carregar_cardapio():
    return [
        {"id": 1, "nome": "Hambúrguer", "preco": 12.5},
        {"id": 2, "nome": "Batata Frita", "preco": 7.0},
        {"id": 3, "nome": "Refrigerante", "preco": 5.0}
    ]

def exibir_cardapio(cardapio):
    print("\n--- CARDÁPIO ---")
    for item in cardapio:
        print(item["id"], "-", item["nome"], "- R$", item["preco"])

def buscar_item(cardapio, id_item):
    for item in cardapio:
        if item["id"] == id_item:
            return item
    return None


