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
    for i in listaViagens:
        if i["motorista"] == pergunta:
            print("Motorista Encontrado!")
            print(i)
        else:
            print("O Motorista : {pergunta} não está Cadastrado!")
            return


def max(lista) :
    

def viagem_mais_cara(listaViagens):
    for i in listaViagens:
        o "gasto_combustivel" maior , tem que printar



def media_consumo(listaViagens):
    print("Ainda não finalizado")
    return


