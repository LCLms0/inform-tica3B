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
    print(f"Livro '{titulo}' adicionado com sucesso!")

def emprestar_livro(listaLivros):
    titulo = input("Digite o título do livro a ser emprestado: ").strip()
    for livro in listaLivros:
        if livro["titulo"].lower() == titulo.lower():
            if livro["status"] == "disponível":
                livro["status"] = "emprestado"
                print(f"O livro '{titulo}' foi emprestado!")
                return
            else:
                print(f"O livro '{titulo}' já está emprestado!")
                return
    print(f"Livro '{titulo}' não encontrado.")

def devolver_livro(listaLivros):
    titulo = input("Digite o título do livro a ser devolvido: ").strip()
    for livro in listaLivros:
        if livro["titulo"].lower() == titulo.lower():
            if livro["status"] == "emprestado":
                livro["status"] = "disponível"
                print(f"O livro '{titulo}' foi devolvido!")
                return
            else:
                print(f"O livro '{titulo}' já está disponível!")
                return
    print(f"Livro '{titulo}' não encontrado.")

def exibir_livros(listaLivros):
    if not listaLivros:
        print("Nenhum livro cadastrado.")
        return

    tabela = [[livro["titulo"], livro["autor"], livro["status"]] for livro in listaLivros]
    print(tabulate(tabela, headers=["Título", "Autor", "Status"], tablefmt="grid"))
    print()


