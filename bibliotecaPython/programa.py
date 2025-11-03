from funcões import *
print("Bem vindo a Blibioteca De Livros Python!")
print("Comandos: ")
print("-----------------------")
print("[1] -> Adicionar Livro ")
print("-----------------------")
print("[2] -> exibir Todos os Livros ")
print("-----------------------")
print("[3] -> Emprestar Livro")
print("-----------------------")
print("[4] -> Devolver Livro")
print("-----------------------")
print("[0] -> sair")
print("-----------------------")

lista = []

while True:
    comando = int(input("Digite o Comando:  "))
    if comando == 1:
        adicionar_livro()
    if comando == 2:
        exibir_livros()
    if comando == 3:
        emprestar_livro()
    if comando == 4:
        devolver_livro()
    if comando == 0:
        break
    else:
        print("Tente novamente")
