---
titulo: Refspecs
tipo: conceito
nivel: avancado
categoria: Git
tags: [git, refspec, fetch, push, remote, refs]
resumo: "Como funcionam os refspecs no fetch e push, incluindo forçar, deletar branches remotas e force-with-lease."
relacionados: ["Sincronização (remote, fetch, pull, push)", "Revisões e ranges", "Aliases e configurações"]
fonte: https://git-scm.com/docs/git-fetch
---

# Refspecs

## O que é?

Um **refspec** é a especificação de como uma **referência** (branch, tag) é mapeada entre o repositório **local** e o **remoto**. Ele aparece nos comandos `git fetch` e `git push` e também nas configurações do remoto.

## Formato

```
[+]<origem>:<destino>
```

- **origem**: ref no repositório de origem.
- **destino**: ref no repositório de destino.
- **`+`**: força a atualização (permite non-fast-forward).

## No fetch

```bash
# busca a branch main e grava em refs/remotes/origin/main
git fetch origin main:refs/remotes/origin/main

# o refspec padrão do origin costuma ser:
# +refs/heads/*:refs/remotes/origin/*
```

```bash
git fetch origin +refs/heads/*:refs/remotes/origin/*
```

## No push

```bash
# envia a branch local main para a branch remota main
git push origin main:main

# envia para uma branch remota com outro nome
git push origin local:remota

# envia a branch atual para a de mesmo nome
git push origin HEAD

# envia todas as branches locais
git push origin refs/heads/*:refs/heads/*
```

## Deletar uma branch remota

```bash
# o lado esquerdo vazio significa "deletar a ref remota"
git push origin :branch-antiga
# equivalente a:
git push origin --delete branch-antiga
```

## Forçar

```bash
# o + permite sobrescrever (cuidado!)
git push origin +main
git push --force-with-lease origin main   # mais seguro
```

- `--force`: sobrescreve o remoto.
- `--force-with-lease`: só sobrescreve se o remoto não tiver mudado desde seu último fetch (**mais seguro**).

## Ver e configurar

```bash
# mostra os refspecs configurados
git config --get remote.origin.fetch

# define um refspec personalizado
git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"
```

## Comandos

| Comando | Descrição |
| --- | --- |
| `git fetch origin main:refs/remotes/origin/main` | Fetch com refspec explícito |
| `git push origin main:main` | Push com refspec explícito |
| `git push origin :branch` | Deleta a branch remota |
| `git push origin +main` | Força o push |
| `git push --force-with-lease` | Força com segurança |
| `git config --get remote.origin.fetch` | Mostra o refspec do remote |

## Erros comuns

- **Usar `--force` em branch compartilhada**, apagando o trabalho de outros.
- **Confundir `--force` com `--force-with-lease`** (o segundo é mais seguro).
- **Esquecer o `+`** ao buscar refs que precisam ser sobrescritas.
- **Deletar branch remota sem querer** com `git push origin :branch`.
- **Não entender o refspec padrão** e achar que o `fetch` está incompleto.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Enviar branch local com outro nome | `git push origin local:remota` |
| Deletar branch remota | `git push origin :branch` |
| Sobrescrever com segurança | `git push --force-with-lease` |
| Buscar todas as branches | refspec `+refs/heads/*:refs/remotes/origin/*` |
