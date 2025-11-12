import tabulate

def registrar_viagem(listaViagens):
    nome = input("Digite o Nome do Motorista:  ")
    destino = input(("Digite o Destino:  "))
    distancia = float(input("Digite a Distância pecorrida: "))
    gasto_combustivel = float(input("Digite o Valor Gasto com Combustivél:  "))
    consumo = gasto_combustivel / distancia

    dic = {"motorista": nome, "destino":
    destino, "distancia": distancia , 
    "Gasto de Combustivél": gasto_combustivel , 
    "consumo" : consumo }

    listaViagens.append(dic)

def exibir_viagens(listaViagens):
    if not listaViagens:
        print("Nenhuma viagem registrada.")
        return
    print(tabulate.tabulate(listaViagens, headers='keys'))

def buscar_motorista(listaViagens):
    pergunta = input("Digite o Nome do motorista:  ")
    for i in listaViagens:
        if i["motorista"] == pergunta:
            print("Motorista Encontrado!")
            print(i)
        else:
            print(f"O Motorista : {pergunta} não está Cadastrado!")
            return

def viagem_mais_cara(listaViagens):
    maiores = []
    maior   = max([viagem["Gasto de Combustivél"] for viagem in listaViagens])
    if maior tiver mais doq 1:
        maiores.append(maior)
    

def media_consumo(listaViagens):
    for i in listaViagens:
        return sum(i["Gasto de Combustivél"]) / i


