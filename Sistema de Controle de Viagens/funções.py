import tabulate

def registrar_viagem(listaViagens,lista2,lista3):
    nome = input("Digite o Nome do Motorista:  ")
    destino = input(("Digite o Destino:  "))
    distancia = float(input("Digite a Distância pecorrida: "))
    gasto_combustivel = float(input("Digite o Valor Gasto com Combustivél:  "))
    consumo = gasto_combustivel / distancia

    gastos = {
        "gasto_combustivel" : gasto_combustivel
    }

    consumos = {
        "consumo" : consumo
    }

    dic = {"motorista": nome, "destino":
    destino, "distancia": distancia , 
    "gasto_combustivel": gasto_combustivel , 
    "consumo" : consumo }

    listaViagens.append(dic)
    lista2.append(gastos)
    lista3.append(consumos)

def exibir_viagens(listaViagens):
    print(tabulate.tabulate(listaViagens, headers='keys'))

def buscar_motorista(listaViagens):
    pergunta = input("Digite o Nome do motorista:  ")
    for i in listaViagens:
        if i["motorista"] == pergunta:
            print("Motorista Encontrado!")
            print(i)
        else:
            print("O Motorista : {pergunta} não está Cadastrado!")
            return

def viagem_mais_cara(lista2):
    for i in lista2:
       return  max(lista2)

def media_consumo(lista3):
    for i in lista3:
        return sum(lista3) / i


