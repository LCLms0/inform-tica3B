from funcões import *

def menu():
    print("---------------------------------")
    print("SISTEMA DE BIBLIOTECA")
    print("---------------------------------")
    print("1 - Adicionar livro")
    print("---------------------------------")
    print("2 - Exibir todos os livros")
    print("---------------------------------")
    print("3 - Emprestar livro")
    print("---------------------------------")
    print("4 - Devolver livro")
    print("---------------------------------")
    print("0 - Sair")
    print("---------------------------------")

def main():
    listaLivros = []

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_livro(listaLivros)
        elif opcao == "2":
            exibir_livros(listaLivros)
        elif opcao == "3":
            emprestar_livro(listaLivros)
        elif opcao == "4":
            devolver_livro(listaLivros)
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tente novamente.")

main()

