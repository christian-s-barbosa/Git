---
titulo: git rebase
tipo: comando
nivel: intermediario
categoria: Git
tags: [git, rebase, historico, reescrita, merge, interativo]
resumo: "Como o rebase reaplica commits sobre outra base, rebase interativo, tratamento de conflitos e a regra de ouro."
relacionados: ["Variantes de rebase (--onto e --root)", "Merge avançado", "git cherry-pick"]
fonte: https://git-scm.com/docs/git-rebase
---

# git rebase

## O que é?

O `git rebase` **reaplica** os commits de uma branch sobre outra base. Em vez de mesclar (merge), ele "desencaixa" seus commits e os recoloca um a um em cima do commit mais recente de outra branch.

O resultado é um **histórico linear**, como se o trabalho tivesse começado a partir do ponto mais atual.

## Como funciona?

Considere:

```
A --- B --- C   (main)
       \
        D --- E   (feature)
```

Após `git rebase main` estando na `feature`:

```
A --- B --- C           (main)
             \
              D' --- E' (feature)
```

- Os commits `D` e `E` são **recriados** como `D'` e `E'` (novos hashes).
- A `feature` passa a partir de `C`.

## Para que serve?

- Manter um **histórico linear** e mais limpo.
- **Atualizar** uma branch com as novidades da principal antes de abrir um pull request.
- **Organizar commits** locais (rebase interativo).

## Comandos básicos

```bash
# reaplica a branch atual sobre a main
git switch feature
git rebase main

# reaplica sobre o remoto atualizado
git fetch origin
git rebase origin/main
```

## Rebase interativo

Permite **editar** os commits antes de reaplicá-los:

```bash
git rebase -i HEAD~3
```

Abre um editor com os últimos 3 commits. Ações possíveis:

| Ação | Efeito |
| --- | --- |
| `pick` | Mantém o commit como está |
| `reword` | Altera a mensagem do commit |
| `edit` | Pausa para alterar o conteúdo do commit |
| `squash` | Junta o commit ao anterior (mantendo as mensagens) |
| `fixup` | Junta ao anterior (descartando a mensagem) |
| `drop` | Remove o commit |

## Conflitos durante o rebase

Ao reaplicar um commit, podem surgir conflitos:

```bash
# resolve os arquivos, marca e continua
git add arquivo.txt
git rebase --continue

# pula o commit que está causando o conflito
git rebase --skip

# cancela o rebase e volta ao estado anterior
git rebase --abort
```

## Rebase x Merge

| Característica | git rebase | git merge |
| --- | --- | --- |
| Histórico | Linear | Com ramificações |
| Cria commit de merge | Não | Sim (três vias) |
| Reescreve commits | Sim | Não |
| Seguro em histórico público | Não | Sim |

## Regra de ouro

> **Nunca faça rebase em commits que já foram enviados (push) para uma branch compartilhada.**

Como o rebase **cria novos commits** (novos hashes), quem já baixou os antigos terá um histórico divergente. Use rebase apenas em **commits locais** ainda não publicados.

## Quando usar?

- Antes de abrir um **pull request**, para deixar a branch atualizada e linear.
- Para **limpar/organizar** commits locais (squash, reword).
- Para incorporar as novidades da `main` em uma branch **pessoal**.

## Erros comuns

- **Fazer rebase em commits já publicados** (com `push`): reescreve o histórico e causa divergência para quem já baixou. Rebase só em commits locais.
- **Confundir rebase com merge**: o rebase cria commits novos (novos hashes); o merge preserva os originais.
- **Perder a noção de onde estava** durante um rebase interativo. Use `git rebase --abort` para voltar ao estado anterior.
- **Resolver conflitos e esquecer o `git add`** antes de `git rebase --continue`.
- **Squash excessivo**, juntando commits de assuntos diferentes e dificultando o histórico.
- **Fazer rebase da branch principal** em vez de rebase da sua branch **sobre** ela.

## Casos de uso

| Cenário | Comando |
| --- | --- |
| Atualizar sua feature com a main antes do PR | `git switch feature` + `git rebase main` |
| Juntar vários commits pequenos em um só | `git rebase -i HEAD~3` (squash) |
| Corrigir a mensagem do último commit | `git commit --amend` ou `rebase -i` (reword) |
| Reordenar ou remover commits locais | `git rebase -i HEAD~n` |
| Deixar a branch linear para revisão | `git rebase origin/main` |
