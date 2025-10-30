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

dict =  { "titulo": [titulo], "autor": [autor], "status": "disponível"}

while True:
    comando = int(input("Digite o Comando:  "))
    if comando == 1:
        print(adicionar_livro)  
    if comando == 2:
        print(exibir_livros)   
    if comando == 3:
        print(emprestar_livro) 
    if comando == 4:
        print(devolver_livro) 
    if comando == 0:
        break
