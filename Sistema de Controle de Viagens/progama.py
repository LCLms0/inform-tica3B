from funções import *

print("1 - Registrar nova viagem") 
print("2 - Exibir todas as viagens")
print("3 - Buscar viagens por motorista") 
print("4 - Exibir viagem mais cara") 
print("5 - Mostrar média geral de consumo") 
print("0 - Sair")

def menu():

    listaViagens = []


    while True:
        comando = int(input("Digite o comando:  "))
        if comando == 1:
            registrar_viagem(listaViagens)
        elif comando == 2:
            exibir_viagens(listaViagens)
        elif comando == 3:
            buscar_motorista(listaViagens)
        elif comando == 4:
            exibir_viagens(listaViagens)
        elif comando == 5:
            media_consumo(listaViagens)
        elif comando == 0:
            break

menu()
    