from funcoes import *
from tabulate import tabulate

print("Bem vindo ao gerenciador de notas python!")
print("Comandos: ")
print("-----------------------")
print("[1] -> cadastrar aluno ")
print("-----------------------")
print("[2] -> exibir relatorio ")
print("-----------------------")
print("[0] -> sair")
print("-----------------------")


Listaalunos = []
while True:    
    listanotas = []
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
        dict = {
            "Aluno": aluno,
            "Notas": {
                "nota 1":nota1,
                "nota 2":nota2,
                "nota 3":nota3,
            }, 
            "Média": media,
            "Situação": situação
        }
        Listaalunos.append(dict)
    if comando == 2:
        print(tabulate(Listaalunos, headers='keys'))
    if comando == 0:
        break
