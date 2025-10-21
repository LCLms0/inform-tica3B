alunos = []
notas  = []
quan = int(input("Digite a quantidade de alunos que deseja cadastrar:  "))
for e in range(quan):
    aluno = input(f"Digite o Nome do {e+1}° Aluno:  ")
    alunos.append(aluno)
    for i in range(4-1):
            nota = input(f"Digite a {i+1}° Nota:  ")
            notas.append(nota)

print(f"{alunos}")
print(f"{notas}")