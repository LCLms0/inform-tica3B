from funções import *

def menu():
    print("---------------------------------")
    print("[1] -> Registrar nova viagem") 
    print("---------------------------------")
    print("[2] -> Exibir todas as viagens")
    print("---------------------------------")
    print("[3] -> Buscar viagens por motorista") 
    print("---------------------------------")
    print("[4] -> Exibir viagem mais cara") 
    print("---------------------------------")
    print("[5] -> Mostrar média geral de consumo") 
    print("---------------------------------")
    print("[0] -> Sair")
    print("---------------------------------")

    listaViagens = []
    lista2 = []
    lista3 = []

    while True:

        try:
            comando = int(input("Digite o comando:  "))

        except ValueError:
            print("Comando inválido! Tente novamente!")
            continue  # volta pro início do while
        
        match comando:
            case  1 :
                registrar_viagem(listaViagens,lista2,lista3)
            case 2 :
                exibir_viagens(listaViagens)
            case 3 :
                buscar_motorista(listaViagens)
            case 4 : 
                viagem_mais_cara(lista2)
            case 5 :
                media_consumo(lista3)
            case 0 :
                break
            case _ :
                print("Comando Invalido! Tente Novamente!")
                return
            
menu()
