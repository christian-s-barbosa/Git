---
titulo: GitHub Actions
tipo: conceito
nivel: intermediario
categoria: GitHub
tags: [github, actions, ci, cd, workflow, automacao, yaml]
resumo: "Conceitos e exemplos de GitHub Actions para CI/CD, gatilhos, secrets e boas práticas de workflows."
relacionados: ["Git em CI-CD", "GitHub Pages", "Releases"]
fonte: https://docs.github.com/pt/actions
---

# GitHub Actions

## O que é?

**GitHub Actions** é a plataforma de **CI/CD e automação** do GitHub. Com ela, você executa tarefas automaticamente em resposta a eventos do repositório (push, pull request, tag, agendamento, etc.).

## Conceitos

| Conceito | O que é |
| --- | --- |
| **Workflow** | Um processo automatizado (arquivo YAML) |
| **Event** | Gatilho que inicia o workflow |
| **Job** | Conjunto de passos executados em um runner |
| **Step** | Uma tarefa dentro do job |
| **Runner** | Máquina que executa o job |
| **Action** | Bloco reutilizável (ex.: `actions/checkout`) |

## Onde ficam

Os workflows ficam em:

```
.github/workflows/*.yml
```

## Exemplo de workflow

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Instalar dependências
        run: npm ci

      - name: Rodar testes
        run: npm test
```

## Gatilhos comuns

```yaml
on:
  push:
    branches: [main]
  pull_request:
  release:
    types: [published]
  schedule:
    - cron: '0 3 * * *'   # todo dia às 03:00
  workflow_dispatch:       # manual
```

## Secrets

Valores sensíveis ficam em **Settings → Secrets and variables → Actions** e são usados assim:

```yaml
- run: echo "Token: ${{ secrets.MEU_TOKEN }}"
```

- Nunca coloque segredos no YAML.
- O `GITHUB_TOKEN` é fornecido automaticamente.

## Usos comuns

- Rodar **testes** e **lint**.
- Fazer **build** e publicar artefatos.
- Fazer **deploy**.
- Criar **releases** automáticas.
- Publicar no **GitHub Pages**.
- Rodar tarefas agendadas.

## Erros comuns

- **Colocar segredos no YAML** em vez de usar secrets.
- **Não fixar versões de actions** (`@v4`) e sofrer mudanças.
- **Esquecer `fetch-depth: 0`** quando precisa de tags/histórico.
- **Workflows muito longos** sem cache.
- **Permissões amplas demais** no `GITHUB_TOKEN`.

## Casos de uso

| Situação | Gatilho |
| --- | --- |
| Testar a cada push | `push` |
| Validar pull requests | `pull_request` |
| Publicar release | `release` / tag |
| Deploy contínuo | `push` na main |
| Tarefa diária | `schedule` |
| Execução manual | `workflow_dispatch` |
