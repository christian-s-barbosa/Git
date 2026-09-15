---
titulo: git worktree
tipo: comando
nivel: intermediario
categoria: Git
tags: [git, worktree, diretorio, branches, paralelo]
resumo: "Como trabalhar em várias branches ao mesmo tempo com múltiplos diretórios de trabalho usando git worktree."
relacionados: ["git stash", "Branches (Ramificações)", "sparse-checkout"]
fonte: https://git-scm.com/docs/git-worktree
---

# git worktree

## O que é?

O `git worktree` permite ter **vários diretórios de trabalho** ligados ao **mesmo repositório**. Assim, você pode trabalhar em **branches diferentes ao mesmo tempo**, em pastas separadas, sem precisar ficar trocando de branch.

## Para que serve?

- Trabalhar em uma **correção urgente** sem interromper o trabalho atual.
- **Comparar** duas branches lado a lado.
- Rodar **builds/testes** de uma branch enquanto edita outra.
- Evitar `git stash` e trocas constantes de contexto.

## Como funciona?

Cada worktree é uma pasta com seus próprios arquivos, mas todos compartilham o **mesmo histórico** (o `.git` principal).

```
projeto/            <- worktree principal (branch main)
projeto-hotfix/     <- worktree extra (branch hotfix)
```

- Uma branch só pode estar **ativa em um worktree por vez**.

## Comandos

```bash
# cria um novo worktree para uma branch existente
git worktree add ../projeto-hotfix hotfix

# cria um worktree com uma nova branch
git worktree add -b nova-feature ../projeto-feature

# lista os worktrees
git worktree list

# remove um worktree
git worktree remove ../projeto-hotfix

# limpa referências de worktrees removidos manualmente
git worktree prune
```

## Exemplo prático

```bash
# você está na main trabalhando
cd projeto

# surge um bug urgente em produção
git worktree add -b hotfix ../projeto-hotfix origin/main

# trabalhe na correção na outra pasta
cd ../projeto-hotfix
git commit -am "Corrige bug urgente"
git push origin hotfix

# depois de resolver, remova o worktree
cd ../projeto
git worktree remove ../projeto-hotfix
```

## Comandos

| Comando | Descrição |
| --- | --- |
| `git worktree add <pasta> <branch>` | Cria um worktree para uma branch |
| `git worktree add -b <branch> <pasta>` | Cria worktree com nova branch |
| `git worktree list` | Lista os worktrees |
| `git worktree remove <pasta>` | Remove um worktree |
| `git worktree prune` | Limpa referências inválidas |

## Cuidados

- Não é possível ter a **mesma branch** em dois worktrees ativos.
- Remova worktrees com `git worktree remove` (não apague a pasta na mão, para evitar sujeira).
- É um recurso **local**: worktrees não são enviados ao remoto.

## Erros comuns

- **Tentar usar a mesma branch em dois worktrees**: não é permitido.
- **Apagar a pasta do worktree manualmente**, deixando referências sujas (use `git worktree remove`).
- **Confundir worktree com clone**: worktrees compartilham o mesmo repositório.
- **Esquecer de limpar** worktrees antigos (use `git worktree prune`).
- **Rodar comandos no worktree errado**, alterando o que não queria.

## Casos de uso

| Cenário | Comando |
| --- | --- |
| Corrigir um bug urgente sem interromper o trabalho | `git worktree add -b hotfix ../hotfix` |
| Comparar duas branches lado a lado | dois worktrees |
| Rodar testes em outra branch | worktree da branch de teste |
| Revisar um PR sem sair da branch atual | worktree da branch do PR |
