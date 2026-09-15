---
titulo: git am e format-patch
tipo: comando
nivel: avancado
categoria: Git
tags: [git, format-patch, am, apply, patch, email, contribuicao]
resumo: "O fluxo de patches por e-mail: gerar patches com format-patch e aplicá-los com am, além do git apply."
relacionados: ["git request-pull", "git cherry-pick", "git range-diff"]
fonte: https://git-scm.com/docs/git-format-patch
---

# git am e format-patch

## O que é?

Esses comandos implementam o fluxo de **patches por e-mail**, muito usado em projetos como o **kernel do Linux**. O `format-patch` **gera** arquivos de patch a partir de commits; o `am` **aplica** esses patches preservando autor e mensagem.

- **`git format-patch`**: transforma commits em arquivos `.patch`.
- **`git am`**: aplica patches (de e-mail) como commits.
- **`git apply`**: aplica um diff sem criar commit.

## Gerar patches

```bash
# gera patch do último commit
git format-patch -1

# gera os últimos 3 commits
git format-patch -3

# gera patches de um intervalo
git format-patch main..feature

# gera um arquivo único
git format-patch main..feature --stdout > mudancas.patch
```

Gera arquivos como `0001-Adiciona-login.patch`.

## Aplicar patches

```bash
# aplica todos os patches da pasta
git am *.patch

# aplica um patch específico
git am 0001-Adiciona-login.patch

# em caso de conflito, use 3-way
git am -3 0001-Adiciona-login.patch

# continua após resolver
git am --continue

# cancela
git am --abort

# pula o patch problemático
git am --skip
```

- O `am` preserva **autor**, **data** e **mensagem** do commit original.

## git apply

Aplica um diff **sem** criar commit (útil para testar):

```bash
git apply mudancas.patch
git apply --check mudancas.patch   # só verifica se aplica
```

## am x apply

| Característica | git am | git apply |
| --- | --- | --- |
| Fonte | Patch com metadados (e-mail) | Diff simples |
| Cria commit | Sim | Não |
| Preserva autor/mensagem | Sim | Não |
| Uso típico | Contribuição por e-mail | Testar/aplicar diff |

## Erros comuns

- **Usar `git apply` achando que cria commit**: ele só altera os arquivos.
- **Aplicar patch fora de ordem**, gerando conflitos.
- **Não usar `-3`** e travar em conflitos simples.
- **Esquecer `git am --abort`** ao desistir.
- **Patches gerados sobre uma base diferente** e que não aplicam.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Enviar commits por e-mail | `git format-patch -3` |
| Aplicar patches recebidos | `git am *.patch` |
| Testar um diff sem commitar | `git apply mudancas.patch` |
| Contribuir com o kernel Linux | fluxo `format-patch` + e-mail |
