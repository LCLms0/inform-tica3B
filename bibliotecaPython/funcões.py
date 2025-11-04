from tabulate import tabulate

def adicionar_livro(listaLivros):
    titulo = input("Digite o título do livro: ").strip()
    autor = input("Digite o autor do livro: ").strip()
    livro = {
        "titulo": titulo,
        "autor": autor,
        "status": "disponível"
    }
    listaLivros.append(livro)
    print(f"\n✅ Livro '{titulo}' adicionado com sucesso!\n")

def emprestar_livro(listaLivros):
    titulo = input("Digite o título do livro a ser emprestado: ").strip()
    for livro in listaLivros:
        if livro["titulo"].lower() == titulo.lower():
            if livro["status"] == "disponível":
                livro["status"] = "emprestado"
                print(f"\n📕 O livro '{titulo}' foi emprestado!\n")
                return
            else:
                print(f"\n⚠️ O livro '{titulo}' já está emprestado!\n")
                return
    print(f"\n❌ Livro '{titulo}' não encontrado.\n")

def devolver_livro(listaLivros):
    titulo = input("Digite o título do livro a ser devolvido: ").strip()
    for livro in listaLivros:
        if livro["titulo"].lower() == titulo.lower():
            if livro["status"] == "emprestado":
                livro["status"] = "disponível"
                print(f"\n📗 O livro '{titulo}' foi devolvido!\n")
                return
            else:
                print(f"\n⚠️ O livro '{titulo}' já está disponível!\n")
                return
    print(f"\n❌ Livro '{titulo}' não encontrado.\n")

def exibir_livros(listaLivros):
    if not listaLivros:
        print("\n📚 Nenhum livro cadastrado.\n")
        return

    tabela = [[livro["titulo"], livro["autor"], livro["status"]] for livro in listaLivros]
    print(tabulate(tabela, headers=["Título", "Autor", "Status"], tablefmt="grid"))
    print()


