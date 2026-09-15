---
titulo: Revisões e ranges
tipo: conceito
nivel: intermediario
categoria: Git
tags: [git, revisao, range, head, describe, rev-parse, referencias]
resumo: "Formas de referenciar commits (HEAD~n, HEAD^n), ranges (.. e ...), git describe e git rev-parse."
relacionados: ["Inspeção do histórico", "Refspecs", "Git em CI-CD"]
fonte: https://git-scm.com/docs/gitrevisions
---

# Revisões e ranges

## O que é?

Uma **revisão** é a forma de **referenciar um commit** no Git. Você não precisa usar sempre o hash completo: existem atalhos e expressões que apontam para commits e intervalos.

## Referências comuns

| Referência | Significado |
| --- | --- |
| `<hash>` | Um commit específico (ex.: `3f2a1b9`) |
| `HEAD` | Commit atual |
| `HEAD~1` | Um commit antes do HEAD (pai) |
| `HEAD~3` | Três commits antes |
| `HEAD^` | Primeiro pai (igual a `HEAD~1`) |
| `HEAD^2` | Segundo pai (em commits de merge) |
| `main` / `feature` | Ponteiro para o topo da branch |
| `v1.0.0` | Uma tag |
| `origin/main` | Branch remota |

```bash
git show HEAD~2
git diff HEAD~1 HEAD
git checkout HEAD^
```

> `~n` sobe **n** gerações; `^n` escolhe o **n-ésimo pai**.

## Ranges (intervalos)

| Expressão | Significado |
| --- | --- |
| `A..B` | Commits que estão em **B** e não em **A** |
| `A...B` | Diferença **simétrica** (commits exclusivos de cada lado) |
| `^A B` | O mesmo que `A..B` |

```bash
# commits da feature que não estão na main
git log main..feature

# diferença entre as branches
git diff main...feature
```

## git describe

Descreve um commit com base na **tag mais próxima**:

```bash
git describe
# v1.2.0-5-g3f2a1b9
```

- `v1.2.0`: tag mais próxima.
- `5`: número de commits desde a tag.
- `g3f2a1b9`: hash abreviado.

Útil para gerar versões em builds.

```bash
git describe --tags          # considera qualquer tag
git describe --tags --always # usa o hash se não houver tag
```

## git rev-parse

**Resolve** uma referência e mostra o hash correspondente:

```bash
git rev-parse HEAD
git rev-parse --short HEAD
git rev-parse --abbrev-ref HEAD    # nome da branch atual
```

## Erros comuns

- **Confundir `~` e `^`** em commits de merge.
- **Trocar `..` por `...`**: `..` mostra commits de um lado; `...` compara os dois lados.
- **Usar `HEAD~2` esperando pular merge commits**: a contagem segue os pais.
- **Esquecer que `git describe` precisa de tags** para funcionar bem.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Ver os últimos commits | `git log HEAD~5..HEAD` |
| Commits que faltam na main | `git log main..feature` |
| Comparar branches | `git diff main...feature` |
| Gerar versão de build | `git describe --tags` |
| Descobrir o hash atual | `git rev-parse HEAD` |
| Saber a branch atual | `git rev-parse --abbrev-ref HEAD` |
