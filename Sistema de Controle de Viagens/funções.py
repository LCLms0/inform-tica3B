import tabulate

def registrar_viagem(listaViagens):
    nome = input("Digite o Nome do Motorista:  ")
    destino = input(("Digite o Destino:  "))
    distancia = float(input("Digite a Distância pecorrida: "))
    gasto_combustivel = float(input("Digite o Valor Gasto com Combustivél:  "))
    consumo = gasto_combustivel / distancia

    dic = {"motorista": nome, "destino":
    destino, "distancia": distancia , 
    "gasto_combustivel": gasto_combustivel , 
    "consumo" : consumo }

    listaViagens.append(dic)

def exibir_viagens(listaViagens):
    print(tabulate.tabulate(listaViagens, headers='keys'))

def buscar_motorista(listaViagens):
    pergunta = input("Digite o Nome do motorista:  ")
    if pergunta in listaViagens:
        print("nada")



def viagem_mais_cara(listaViagens):
    print("Ainda não finalizado")
    return

def media_consumo(listaViagens):
    print("Ainda não finalizado")
    return


