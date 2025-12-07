def listar_pedidos(pedidos, cardapio):
    print("\n--- PEDIDOS ---")
    for p in pedidos:
        print("Pedido", p["id"], "- Total:", p["total"])

def buscar_pedido_por_id(pedidos, id_pedido):
    for p in pedidos:
        if p["id"] == id_pedido:
            return p
    return None

def relatorio_financeiro(pedidos):
    if not pedidos:
        return {"total_vendido": 0, "mais_caro": None, "total_itens": 0}

    total_vendido = sum(p["total"] for p in pedidos)
    mais_caro = max(pedidos, key=lambda p: p["total"])["id"]
    total_itens = sum(i["quantidade"] for p in pedidos for i in p["itens"])

    return {
        "total_vendido": total_vendido,
        "mais_caro": mais_caro,
        "total_itens": total_itens
    }
