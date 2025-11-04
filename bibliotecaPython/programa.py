from funcões import adicionar_livro, emprestar_livro, devolver_livro, exibir_livros

def menu():
    print("=" * 40)
    print("📚  SISTEMA DE BIBLIOTECA  📚".center(40))
    print("=" * 40)
    print("1 - Adicionar livro")
    print("2 - Exibir todos os livros")
    print("3 - Emprestar livro")
    print("4 - Devolver livro")
    print("0 - Sair")
    print("=" * 40)

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
            print("\n👋 Encerrando o programa... Até mais!\n")
            break
        else:
            print("\n⚠️ Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    main()

