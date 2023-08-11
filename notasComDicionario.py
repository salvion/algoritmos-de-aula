notas = {}
conceito = ""

quantidade = int(input("Quantos alunos? "))

for i in range(quantidade):
    nome = input(f"Nome do aluno {i+1}: ")
    nota = float(input(f"Nota do aluno {i+1}: "))
    notas[nome] = nota

for nome, nota in notas.items():
    if nota < 7.0:
        conceito = "F"
    if nota >= 7.0:
        conceito = "C"
    if nota >= 8.0:
        conceito = "B"
    if nota >= 9.0:
        conceito = "A"

    print(f"Aluno {nome}, com conceito {conceito} e nota {nota}")