import tabulate

def registrar_viagem(listaViagens):
    nome = input("Digite o Nome do Motorista:  ").strip().lower()
    destino = input(("Digite o Destino:  ")).strip().lower()
    distancia = float(input("Digite a Distância pecorrida: "))
    gasto_combustivel = float(input("Digite o Valor Gasto com Combustivél:  "))
    consumo = gasto_combustivel / distancia

    dic = {
        "motorista"           : nome,
        "destino"             : destino,
        "distancia"           : distancia, 
        "Gasto de Combustivél": gasto_combustivel, 
        "consumo"             : consumo }

    listaViagens.append(dic)

def exibir_viagens(listaViagens):
    if not listaViagens:
        print("Nenhuma viagem registrada.")
        return
    print(tabulate.tabulate(listaViagens, headers='keys'))

def buscar_motorista(listaViagens):
    pergunta = input("Digite o Nome do motorista:  ").strip().lower()
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
    for viagem in listaViagens:
        if viagem["Gasto de Combustivél"] == maior:
            maiores.append(viagem)
    exibir_viagens(maiores)
  

    

def media_consumo(listaViagens):
    print("A média geral de consumo: ")
    print(sum([viagem["consumo"] for viagem in listaViagens]) / len(listaViagens))
