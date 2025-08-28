import csv, os

# ===== Classe Aluno =====
class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

    def situacao(self):
        if self.nota >= 7:
            return "Aprovado"
        elif self.nota >= 5:
            return "Recuperação"
        return "Reprovado"

    def exibir_info(self):
        print(f"Nome: {self.nome:20} | Idade: {self.idade:2d} | Nota: {self.nota:4.1f} | Situação: {self.situacao()}")


mensagem = "Bem-vindo ao sistema de cadastro de alunos!"
print(mensagem)

alunos = []  # lista de objetos Aluno

# ===== Cadastro =====
dnv = True
while dnv:
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    nota = float(input("Digite a nota do aluno: ").replace(",", "."))

    while nota > 10 or nota < 0:
        print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")
        nota = float(input("Digite a nota do aluno: ").replace(",", "."))

    aluno = Aluno(nome, idade, nota)
    alunos.append(aluno)

    print("Aluno cadastrado com sucesso!")
    dnv = input("\nDeseja cadastrar outro aluno? (s/n): ").strip().lower() == 's'


# ===== Operações com os dados =====
if alunos:
    quant_alunos = len(alunos)
    soma_notas = sum(a.nota for a in alunos)
    media_notas = soma_notas / quant_alunos
    acima_de_7 = sum(1 for a in alunos if a.nota > 7)
    nomes_ordenados = sorted((a.nome for a in alunos), key=str.casefold)

    print("\n===== Operações com os dados =====")
    print(f"Quantidade de alunos: {quant_alunos}")
    print(f"Média das notas: {media_notas:.2f}")
    print(f"Alunos com nota > 7: {acima_de_7}")
    print(f"Nomes (A-Z): {', '.join(nomes_ordenados)}")
else:
    print("\nNenhum aluno cadastrado.")
    exit(0)


# ===== Situação dos alunos =====
print("\n===== Situação dos alunos =====")
for a in alunos:
    a.exibir_info()


# ===== Salvar em CSV =====
caminho_csv = "alunos.csv"
with open(caminho_csv, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["nome", "idade", "nota", "situacao"])
    for a in alunos:
        writer.writerow([a.nome, a.idade, f"{a.nota:.2f}", a.situacao()])

print(f"\n Dados salvos em: {caminho_csv}")
