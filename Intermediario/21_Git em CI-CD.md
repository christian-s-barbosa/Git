---
titulo: Git em CI-CD
tipo: conceito
nivel: intermediario
categoria: Git
tags: [git, ci, cd, pipeline, actions, automacao, checkout]
resumo: "Como o Git é usado em pipelines de CI/CD: gatilhos, checkout eficiente, autenticação, versionamento e boas práticas."
relacionados: ["GitHub Actions", "Fluxos de trabalho", "Revisões e ranges"]
fonte: https://git-scm.com/docs
---

# Git em CI/CD

## O que é?

**CI/CD** (Integração Contínua / Entrega Contínua) são pipelines automatizados que **testam, constroem e implantam** o código. O Git é o **gatilho**: cada `push`, `pull request` ou `tag` pode iniciar uma execução.

## Como o Git é usado

- **Gatilhos**: push, pull request, tag, agendamento.
- **Checkout**: o pipeline clona o repositório.
- **Referência**: usa branch, commit ou tag para versionar o artefato.
- **Publicação**: tags costumam marcar releases.

## Checkout eficiente

```bash
# clone raso: mais rápido no CI
git clone --depth 1 <url>

# histórico limitado (para git describe/versionamento)
git clone --depth 50 <url>

# apenas a branch necessária
git clone --single-branch --branch main <url>
```

No GitHub Actions, o `fetch-depth` controla isso:

```yaml
- uses: actions/checkout@v4
  with:
    fetch-depth: 0   # histórico completo (para tags/describe)
```

## Exemplo de workflow

```yaml
name: CI
on:
  push:
    branches: [main]
  pull_request:
  release:
    types: [published]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm test
```

## Autenticação no CI

| Forma | Uso |
| --- | --- |
| Token (PAT) | HTTPS, escopos limitados |
| `GITHUB_TOKEN` | Acesso ao próprio repositório |
| Deploy key (SSH) | Acesso a outro repositório |

- Guarde credenciais em **secrets**, nunca no código.
- Prefira tokens de escopo mínimo.

## Versionamento a partir do Git

```bash
git describe --tags          # v1.2.0-5-g3f2a1b9
git rev-parse --short HEAD   # hash curto
```

- Usado para nomear artefatos e builds.
- Tags marcam releases; `git describe` gera versões.

## Boas práticas

- Clone **raso** quando o histórico completo não é necessário.
- Use **cache** de dependências.
- **Nunca** faça `push --force` em branch monitorada pelo CI.
- Rode o pipeline em **pull requests** também.
- Proteja a branch principal (revisão obrigatória).
- Use **tags** para releases.

## Erros comuns

- **Clonar com `--depth 1` e precisar de tags** (`git describe` falha).
- **Colocar token no repositório** em vez de usar secrets.
- **Deploy a partir de branch desatualizada**.
- **Não proteger a branch principal** e permitir push direto.

## Casos de uso

| Situação | Prática |
| --- | --- |
| Rodar testes a cada push | gatilho `push` + `npm test` |
| Validar pull requests | gatilho `pull_request` |
| Publicar release | gatilho em `tag` |
| Gerar versão do build | `git describe --tags` |
| Clonar rápido no CI | `clone --depth 1` |
