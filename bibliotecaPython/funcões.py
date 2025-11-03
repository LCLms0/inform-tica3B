
def adicionar_livro(lista):
        titulo = input("Digite o Titúlo Deste Livro:  ")
        autor = input("Digte o Titúlo Deste Livro:  ")
        livro = {
             "titulo" : titulo , "autor" : autor , "status" : "Disponivél"
        }
        lista.append(livro)

def emprestar_livro(lista):    
    Status = ("emprestado")
    Status.append(lista)

def  devolver_livro(lista):
    Status = ("Disponivél")
    Status.append(lista)

def exibir_livros(lista):
    print(lista)
    

