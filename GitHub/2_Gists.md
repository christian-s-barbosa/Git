---
titulo: Gists
tipo: conceito
nivel: intermediario
categoria: GitHub
tags: [github, gist, trecho, snippet, compartilhar, gh-cli]
resumo: "O que são Gists, diferença entre público e secret, como criar e gerenciar e quando usar."
relacionados: ["Releases", "GitHub Pages", "Code review"]
fonte: https://docs.github.com/pt/get-started/writing-on-github/editing-and-sharing-content-with-gists
---

# Gists

## O que é?

Um **Gist** é uma forma simples de **compartilhar trechos de código** ou arquivos no GitHub. Cada gist é, na verdade, um **repositório Git** pequeno, que pode ser clonado e versionado.

## Gist x repositório

| Característica | Gist | Repositório |
| --- | --- | --- |
| Objetivo | Trechos/arquivos soltos | Projeto completo |
| Estrutura | Um ou poucos arquivos | Estrutura completa |
| Comentários | Sim | Issues/PRs |
| Fork | Sim | Sim |
| Clonável | Sim | Sim |

## Tipos

- **Público**: aparece em buscas e no seu perfil.
- **Secret (privado)**: não aparece em buscas, mas é acessível por link (não é totalmente privado).

## Criar

**Pela web**: acesse `https://gist.github.com`, escreva o conteúdo e escolha público ou secret.

**Pela CLI:**

```bash
# cria um gist a partir de um arquivo
gh gist create arquivo.txt

# com descrição
gh gist create arquivo.txt --desc "Exemplo de uso"

# público
gh gist create arquivo.txt --public

# a partir de vários arquivos
gh gist create a.js b.js
```

## Gerenciar

```bash
gh gist list              # lista seus gists
gh gist view <id>         # mostra um gist
gh gist edit <id>         # edita
gh gist delete <id>       # remove
gh gist clone <id>        # clona como repositório
```

## Erros comuns

- **Usar gist secret para segredos reais**: ele não é privado de verdade.
- **Guardar projeto inteiro em gist** em vez de repositório.
- **Perder o link** de um gist secret (ele não é indexado).
- **Confundir secret com privado**.

## Casos de uso

| Situação | Uso |
| --- | --- |
| Compartilhar um trecho de código | Gist público |
| Guardar um snippet rápido | Gist secret |
| Exemplo em uma issue/resposta | Gist |
| Versionar um arquivo solto | Gist (é um repo Git) |
| Compartilhar configuração | Gist |
