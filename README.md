# calcular_media_aluno

Um sistema completo em Python para calcular e classificar o desempenho de alunos.

## 📋 Descrição

Este projeto calcula a média aritmética de notas de alunos, classifica seu desempenho e gera um relatório agrupado por situação (Aprovado, Recuperação, Reprovado).

**Funcionalidades:**
- ✅ Validação de entrada para nomes (apenas letras e espaços)
- ✅ Coleta de 3 notas por aluno com validação (0 a 10)
- ✅ Cálculo automático da média
- ✅ Classificação automática:
  - **Aprovado**: média ≥ 7.0
  - **Recuperação**: média entre 5.0 e 6.9
  - **Reprovado**: média < 5.0
- ✅ Relatório final agrupado por situação

## 🚀 Como usar

Execute o script:

```bash
python desafio_01.py
```

Siga as instruções:
1. Digite a quantidade de alunos
2. Para cada aluno, informe o nome e suas 3 notas
3. Visualize o relatório final com todos os alunos agrupados por situação

## 📝 Arquivo principal

- **desafio_01.py** - Script principal com todas as funções de coleta, validação, cálculo e relatório
