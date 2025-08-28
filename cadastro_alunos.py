mensagem = "Bem-vindo ao sistema de cadastro de alunos!"
print(mensagem)

alunos = []
dnv = True

while dnv:
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    # aceita vírgula ou ponto
    nota = float(input("Digite a nota do aluno: ").replace(",", "."))

    while nota > 10 or nota < 0:
        print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")
        nota = float(input("Digite a nota do aluno: ").replace(",", "."))

    novo_aluno = {"nome": nome, "idade": idade, "nota": nota}
    alunos.append(novo_aluno)

    print("Aluno cadastrado com sucesso!")
    print(alunos)

    dnv = input("\nDeseja cadastrar outro aluno? (s/n): ").strip().lower() == 's'


# ===== Ver aprovados (com operações) =====
apv = input("\nDeseja ver os aprovados? (s/n): ").strip().lower()
while apv == 's':
    if not alunos:
        print("\nNenhum aluno cadastrado.")
        break

    # operações com os dados
    quant_alunos = len(alunos)
    soma_notas = sum(a["nota"] for a in alunos)
    media_notas = soma_notas / quant_alunos
    acima_de_7 = sum(1 for a in alunos if a["nota"] > 7)
    nomes_ordenados = sorted((a["nome"] for a in alunos), key=str.casefold)

    print("\n===== Operações com os dados =====")
    print(f"Quantidade de alunos: {quant_alunos}")
    print(f"Média das notas: {media_notas:.2f}")
    print(f"Alunos com nota > 7: {acima_de_7}")
    print(f"Nomes (A-Z): {', '.join(nomes_ordenados)}")

    # lista apenas aprovados
    print("\n===== Aprovados (nota >= 7) =====")
    aprovados = [a for a in alunos if a["nota"] >= 7]
    if aprovados:
        for a in aprovados:
            print(f"{a['nome']}\t{a['idade']} anos\tNota {a['nota']:.1f}")
    else:
        print("Nenhum aluno aprovado.")

    apv = input("\nDeseja ver os aprovados novamente? (s/n): ").strip().lower()


# ===== Situação dos alunos =====
situation = input("\nDeseja ver a situação (Aprovado/Recuperação/Reprovado)? (s/n): ").strip().lower()
while situation == 's':
    print("\n===== Situação dos alunos =====")
    for a in alunos:
        nota = a["nota"]
        if nota >= 7:
            situacao = "Aprovado"
        elif nota >= 5:
            situacao = "Recuperação"
        else:
            situacao = "Reprovado"

        print(f"Nome: {a['nome']:20} | Idade: {a['idade']:2d} | Nota: {nota:4.1f} | Situação: {situacao}")
    situation = input("\nDeseja ver a situação novamente? (s/n): ").strip().lower()


# ===== Salvar em CSV =====
csv_save = input("\nDeseja salvar os dados em um arquivo CSV? (s/n): ").strip().lower()
caminho_csv = "alunos.csv"
import csv, os

while csv_save == 's':
    with open(caminho_csv, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(["nome", "idade", "nota", "situacao"])
        for a in alunos:
            if a["nota"] >= 7:
                situacao = "Aprovado"
            elif a["nota"] >= 5:
                situacao = "Recuperação"
            else:
                situacao = "Reprovado"

            nota_str = f"{a['nota']:.2f}"
            writer.writerow([a["nome"], a["idade"], nota_str, situacao])

    print(f"\nDados salvos em: {caminho_csv}")
    csv_save = input("\nDeseja salvar os dados em um arquivo CSV novamente? (s/n): ").strip().lower()


# ===== Ver conteúdo do CSV =====
arq_show = input("\nDeseja ver o conteúdo do arquivo CSV? (s/n): ").strip().lower()
while arq_show == 's':
    if not os.path.exists(caminho_csv):
        print("O arquivo ainda não existe. Salve primeiro (opção anterior).")
    else:
        print("\n===== Conteúdo do arquivo =====")
        with open(caminho_csv, "r", encoding="utf-8-sig") as f:
            print(f.read(), end="\n")
    arq_show = input("\nDeseja ver o conteúdo do arquivo CSV novamente? (s/n): ").strip().lower()
