def novo_pedido(cardapio):
    pedido = {"id": None, "itens": [], "total": 0}

    while True:
        id_item = int(input("ID do item (0 para sair): "))
        if id_item == 0:
            break

        item = next((i for i in cardapio if i["id"] == id_item), None)
        if not item:
            print("Item não existe.")
            continue

        qtd = int(input("Quantidade: "))
        pedido["itens"].append({"id": id_item, "quantidade": qtd})

    return pedido


def calcular_total(pedido, cardapio):
    total = 0
    qtd_total = 0

    for item_p in pedido["itens"]:
        item = next((i for i in cardapio if i["id"] == item_p["id"]), None)
        total += item["preco"] * item_p["quantidade"]
        qtd_total += item_p["quantidade"]

    if total > 50:
        total *= 0.9

    pedido["total"] = total
    pedido["brinde"] = qtd_total > 5


def exibir_pedido(pedido, cardapio):
    print("\n--- PEDIDO ---")
    for item_p in pedido["itens"]:
        item = next((i for i in cardapio if i["id"] == item_p["id"]), None)
        print(item["nome"], "x", item_p["quantidade"])
    print("Total:", pedido["total"])
    if pedido.get("brinde"):
        print("Brinde incluso!")

    


    