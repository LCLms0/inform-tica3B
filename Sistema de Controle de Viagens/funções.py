# import tabulate

# def registrar_viagem(listaViagens,lista2,lista3):
#     nome = input("Digite o Nome do Motorista:  ")
#     destino = input(("Digite o Destino:  "))
#     distancia = float(input("Digite a Distância pecorrida: "))
#     gasto_combustivel = float(input("Digite o Valor Gasto com Combustivél:  "))
#     consumo = gasto_combustivel / distancia

#     gastos = {
#         "gasto_combustivel" : gasto_combustivel
#     }

#     consumos = {
#         "consumo" : consumo
#     }

#     dic = {"motorista": nome, "destino":
#     destino, "distancia": distancia , 
#     "gasto_combustivel": gasto_combustivel , 
#     "consumo" : consumo }

#     listaViagens.append(dic)
#     lista2.append(gastos)
#     lista3.append(consumos)

# def exibir_viagens(listaViagens):
#     print(tabulate.tabulate(listaViagens, headers='keys'))

# def buscar_motorista(listaViagens):
#     pergunta = input("Digite o Nome do motorista:  ")
#     for i in listaViagens:
#         if i["motorista"] == pergunta:
#             print("Motorista Encontrado!")
#             print(i)
#         else:
#             print("O Motorista : {pergunta} não está Cadastrado!")
#             return

# def viagem_mais_cara(lista2):
#     for i in lista2:
#        return  max(lista2)

# def media_consumo(lista3):
#     for i in lista3:
#         return sum(lista3) / i

from tabulate import tabulate

def registrar_viagem(lista):
    print("\n--- Registrar Viagem ---")
    motorista = input("Nome do motorista: ")
    destino = input("Destino: ")

    try:
        distancia = float(input("Distância percorrida (km): "))
        gasto = float(input("Gasto com combustível (R$): "))
    except ValueError:
        print("Valores inválidos! Use apenas números.")
        return

    consumo = gasto / distancia
    viagem = {
        "motorista": motorista,
        "destino": destino,
        "distancia": distancia,
        "gasto": gasto,
        "consumo": round(consumo, 2)
    }
    lista.append(viagem)
    print("Viagem registrada com sucesso!")


def exibir_viagens(lista):
    print("\n--- Todas as Viagens ---")
    if not lista:
        print("Nenhuma viagem registrada.")
        return

    tabela = [
        [v["motorista"], v["destino"], v["distancia"], v["gasto"], v["consumo"]]
        for v in lista
    ]
    print(tabulate(tabela, headers=["Motorista", "Destino", "Distância", "Gasto", "Consumo"], tablefmt="grid"))


def buscar_motorista(lista):
    nome = input("Nome do motorista: ")
    viagens = [v for v in lista if v["motorista"].lower() == nome.lower()]

    if not viagens:
        print("Nenhuma viagem encontrada.")
        return

    tabela = [
        [v["motorista"], v["destino"], v["distancia"], v["gasto"], v["consumo"]]
        for v in viagens
    ]
    print(tabulate(tabela, headers=["Motorista", "Destino", "Distância", "Gasto", "Consumo"], tablefmt="grid"))


def viagem_mais_cara(lista):
    if not lista:
        print("Nenhuma viagem registrada.")
        return

    cara = max(lista, key=lambda v: v["gasto"])
    print("\n--- Viagem Mais Cara ---")
    print(f"Motorista: {cara['motorista']}")
    print(f"Destino: {cara['destino']}")
    print(f"Gasto: R$ {cara['gasto']:.2f}")


def media_consumo(lista):
    if not lista:
        print("Nenhuma viagem registrada.")
        return

    media = sum(v["consumo"] for v in lista) / len(lista)
    print(f"Média geral de consumo: R$ {media:.2f}/km")



