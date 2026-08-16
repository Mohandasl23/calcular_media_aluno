# Calcular Média Aluno

Um sistema em Python para calcular e classificar o desempenho académico de alunos com base em suas notas.

## Descrição

Este projeto implementa um sistema de gestão de notas que coleta dados de múltiplos alunos, calcula suas médias aritmética, classifica seu desempenho e gera um relatório consolidado agrupado por situação académica.

## Funcionalidades

- Validação de entrada para nomes (apenas letras e espaços)
- Coleta de 3 notas por aluno com validação de intervalo (0 a 10)
- Cálculo automático da média aritmética
- Classificação automática por situação:
  - **Aprovado**: média ≥ 7.0
  - **Recuperação**: média entre 5.0 e 6.9
  - **Reprovado**: média < 5.0
- Relatório consolidado agrupado por situação académica

## Requisitos

- Python 3.6 ou superior

## Como usar

Execute o script a partir do terminal:

```bash
python desafio_01.py
```

### Fluxo de uso

1. Digite a quantidade de alunos a processar
2. Para cada aluno, forneça:
   - Nome (apenas letras e espaços)
   - Três notas (valores entre 0 e 10)
3. O sistema exibirá um relatório final com todos os alunos agrupados por situação

### Exemplo de execução

```
Digite a quantidade de alunos: 3
Digite o nome do aluno: João Silva
Digite a 1ª nota: 8.5
Digite a 2ª nota: 7.0
Digite a 3ª nota: 8.5
Digite o nome do aluno: Maria Santos
Digite a 1ª nota: 5.5
Digite a 2ª nota: 4.5
Digite a 3ª nota: 5.0
Digite o nome do aluno: Pedro Costa
Digite a 1ª nota: 6.0
Digite a 2ª nota: 5.5
Digite a 3ª nota: 6.5

Relatório Final:

Aprovado: 1
  João Silva: 8.00

Recuperação: 2
  Maria Santos: 5.00
  Pedro Costa: 6.00
```

## Estrutura do projeto

- **desafio_01.py** - Script principal contendo todas as funções do sistema

## Licença

Este projeto é fornecido como está para fins educacionais.
