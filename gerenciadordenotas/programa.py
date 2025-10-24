from funcoes import *

print("MENU")
print("1 - cadastrar aluno")
print("2 - exibir relatorio")
print("0 - sair")

listaAlunos = []
listanotas = []
while True:
    comando = int(input("Digite o comando:  "))
    if comando == 1:
        aluno = input("Digite o nome do aluno:  ")
        nota1= float(input("Nota 1: "))
        nota2= float(input("Nota 2: " ))
        nota3= float(input("Nota 3: "))
        listanotas.append(nota1)
        listanotas.append(nota2)
        listanotas.append(nota3)
        media = calcular_media(listanotas)
        situação = verificar_situacao(media)
        dicionario = {aluno:[nota1,nota2,nota3,media,situação]}
        listaAlunos.append(dicionario)
    if comando == 2:
        print(listaAlunos)
        print(calcular_media(listanotas))
        print(verificar_situacao(media))
    if comando == 0:
        break
