# Desafio 01 — Sistema de Classificação de Alunos

Este projeto implementa um script em Python para registrar alunos, ler suas três notas, calcular a média final e classificar cada aluno conforme o desempenho.

## Objetivo

O sistema avalia a média de cada aluno usando a seguinte regra:

- Aprovado: média >= 7.0
- Recuperação: 5.0 <= média < 7.0
- Reprovado: média < 5.0

## Estrutura do projeto

- `desafio_01.py` — arquivo principal contendo a lógica da aplicação.
- `README.md` — documentação do projeto.

## Requisitos

- Python 3.8 ou superior
- Biblioteca padrão do Python

## Como executar

1. Abra o terminal na pasta do projeto.
2. Execute o comando:

```bash
python desafio_01.py
```

3. Informe os dados solicitados pelo programa.

## Funcionalidades

O programa oferece as seguintes funcionalidades:

- validação do nome do aluno
- validação das notas dentro do intervalo de 0 a 10
- cálculo da média aritmética
- classificação por situação
- organização dos alunos em grupos
- impressão do relatório final

## Organização do código

A lógica foi dividida em funções para facilitar manutenção e leitura:

- `obter_nome()`: valida e retorna o nome do aluno.
- `obter_notas()`: coleta e valida as três notas.
- `obter_media(notas)`: calcula a média final.
- `classificar_aluno(media)`: retorna a situação do aluno.
- `imprimir_alunos(titulo, alunos)`: exibe os alunos de um grupo específico.
- `calcular_media_aluno()`: executa o fluxo principal do programa.

## Fluxo principal

```python
if __name__ == "__main__":
    calcular_media_aluno()
```

Esse bloco garante que o programa seja executado somente quando o arquivo for rodado diretamente.

## Exemplo de uso

```text
Digite a quantidade de alunos: 2
Digite o nome do aluno: Ana
Digite a 1ª nota: 8
Digite a 2ª nota: 7
Digite a 3ª nota: 9

Digite o nome do aluno: Pedro
Digite a 1ª nota: 5
Digite a 2ª nota: 4
Digite a 3ª nota: 6

Alunos aprovados: 1
Ana: 8.00

Alunos em recuperação: 1
Pedro: 5.00

Alunos reprovados: 0
```

## Validações implementadas

- A quantidade de alunos deve ser maior que zero.
- O nome deve conter apenas letras e espaços.
- Cada nota deve estar entre 0 e 10.
- Entradas inválidas provocam nova solicitação de dados.

## Autor

- Mohandas Leandro
