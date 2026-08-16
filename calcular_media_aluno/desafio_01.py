# Solicita e valida o nome do aluno.
# Aceita apenas letras e espaços, evitando entradas vazias ou inválidas.
def obter_nome():
    while True:

        nome = input("Digite o nome do aluno: ")
        if nome.strip() and all(
            caractere.isalpha() or caractere.isspace() for caractere in nome
        ):
            return nome
        print("Nome inválido. Digite apenas letras e espaços.")


# Coleta as 3 notas do aluno e valida se cada valor está entre 0 e 10.
def obter_notas():
    notas = []
    for nota in range(1, 4):
        while True:
            try:
                valor_nota = float(input(f"Digite a {nota}ª nota: "))
                if 0 <= valor_nota <= 10:
                    notas.append(valor_nota)
                    break
                print("Nota inválida. Digite um valor entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
    return notas


# Calcula a média aritmética das notas informadas.
def obter_media(notas):
    return sum(notas) / len(notas)


# Classifica o aluno conforme a média final:
# 7 ou mais = Aprovado, 5 ou mais = Recuperação, menor que 5 = Reprovado.
def classificar_aluno(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    return "Reprovado"


# Exibe o relatório final, mostrando a quantidade e os nomes de cada grupo.
def imprimir_relatorio(alunos_agrupados):
    print("\nRelatório Final:\n")
    for situacao, alunos in alunos_agrupados.items():
        print(f"{situacao}: {len(alunos)}")
        for aluno in alunos:
            print(f"  {aluno['nome']}: {aluno['media']:.2f}")
        print()  # Adiciona uma linha em branco entre os grupos


# Controla o fluxo principal do sistema: coleta a quantidade de alunos,
# solicita os dados, calcula a média, classifica e agrupa os resultados.
def executar_sistema():

    # Dicionário que guarda os alunos por situação.
    alunos_agrupados = {"Aprovado": [], "Recuperação": [], "Reprovado": []}

    while True:
        try:
            quantidade_alunos = int(input("Digite a quantidade de alunos: "))
            if quantidade_alunos > 0:
                break
            print("Digite um número maior que 0.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    for _ in range(quantidade_alunos):
        nome = obter_nome()
        notas = obter_notas()
        media = obter_media(notas)
        situacao = classificar_aluno(media)

        aluno = {"nome": nome, "media": media}

        alunos_agrupados[situacao].append(aluno)

    imprimir_relatorio(alunos_agrupados)


if __name__ == "__main__":
    executar_sistema()
