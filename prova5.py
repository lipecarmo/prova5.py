
num_alunos = int(input("Digite o número de alunos: "))

soma_geral = 0 


for i in range(num_alunos):
    nome = input(f"\nDigite o nome do aluno {i + 1}: ")

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    

    media = (nota1 + nota2 + nota3) / 3
    soma_geral += media

    if media >= 7.0:
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"

    print(f"\nNome: {nome}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média: {media:.2f}")
    print(f"Resultado: {resultado}")

media_geral = soma_geral / num_alunos
print(f"\nMédia geral da turma: {media_geral:.2f}")
