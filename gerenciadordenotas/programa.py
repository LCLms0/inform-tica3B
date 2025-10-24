print("MENU")
print("1 - cadastrar aluno")
print("2 - exibir relatorio")
print("0 - sair")
listaAlunos = []

while True:
    comando = int(input("Digite o comando:  "))
    if comando == 1:
        aluno = input("Digite o nome do aluno:  ")
        nota1= float(input("Nota 1"))
        nota2= float(input("Nota 1"))
        nota3= float(input("Nota 1"))
        dicionario = {aluno:[nota1,nota2,nota3]}
        listaAlunos.append(dicionario)
    if comando == 2:
        print(listaAlunos)
        
    if comando == 0:
        break
