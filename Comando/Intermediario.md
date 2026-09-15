---
titulo: Comandos Intermediários do Git
tipo: referencia
nivel: intermediario
categoria: Git
tags: [git, comandos, cli, cheatsheet, intermediario]
resumo: "Cheatsheet dos comandos intermediários do Git (rebase, cherry-pick, reflog, bisect, worktree, LFS etc.)."
relacionados: ["Comandos Básicos do Git", "Comandos Avançados do Git", "git rebase"]
fonte: https://git-scm.com/docs
---

# Comandos Intermediários do Git

## Rebase

| Comando | Descrição |
| --- | --- |
| `git rebase main` | Reaplica a branch atual sobre a `main` |
| `git rebase origin/main` | Reaplica sobre o remoto atualizado |
| `git rebase -i HEAD~3` | Rebase interativo dos últimos 3 commits |
| `git rebase --continue` | Continua após resolver um conflito |
| `git rebase --skip` | Pula o commit que causou o conflito |
| `git rebase --abort` | Cancela o rebase e volta ao estado anterior |

## Cherry-pick

| Comando | Descrição |
| --- | --- |
| `git cherry-pick <hash>` | Aplica um commit específico na branch atual |
| `git cherry-pick <h1> <h2>` | Aplica vários commits |
| `git cherry-pick <a>..<b>` | Aplica um intervalo de commits |
| `git cherry-pick -n <hash>` | Aplica sem criar o commit |
| `git cherry-pick --continue` | Continua após resolver conflito |
| `git cherry-pick --abort` | Cancela a operação |

## Reflog

| Comando | Descrição |
| --- | --- |
| `git reflog` | Mostra os movimentos do HEAD |
| `git reflog show <branch>` | Mostra o reflog de uma branch |
| `git reflog --date=iso` | Mostra o reflog com datas |
| `git reset --hard HEAD@{n}` | Volta para um estado anterior do reflog |
| `git branch recuperada <hash>` | Cria branch a partir de um commit recuperado |

## Inspeção do histórico

| Comando | Descrição |
| --- | --- |
| `git log --author="X"` | Commits de um autor |
| `git log --since` / `--until` | Filtra por data |
| `git log --grep="texto"` | Filtra pela mensagem |
| `git log -S"texto"` | Commits que alteraram as ocorrências do texto |
| `git log main..feature` | Commits da feature que não estão na main |
| `git log -- <arquivo>` | Histórico de um arquivo |
| `git blame <arquivo>` | Autoria linha a linha |
| `git blame -L 10,20 <arquivo>` | Autoria de um intervalo de linhas |
| `git diff main feature` | Diferença entre duas branches |
| `git show <hash>` | Detalhes de um commit |

## Reescrita e limpeza

| Comando | Descrição |
| --- | --- |
| `git commit --amend` | Corrige o último commit |
| `git reset --soft HEAD~1` | Desfaz o commit mantendo tudo preparado |
| `git reset --mixed HEAD~1` | Desfaz o commit e tira do stage |
| `git reset --hard HEAD~1` | Desfaz o commit e descarta as alterações |
| `git revert <hash>` | Cria um commit que desfaz outro |
| `git clean -n` | Mostra o que seria removido (não rastreado) |
| `git clean -fd` | Remove arquivos e pastas não rastreados |

## Submodules

| Comando | Descrição |
| --- | --- |
| `git submodule add <url> <pasta>` | Adiciona um submodule |
| `git clone --recurse-submodules <url>` | Clona já baixando os submodules |
| `git submodule update --init --recursive` | Inicializa e atualiza os submodules |
| `git submodule update --remote` | Atualiza para a versão mais recente do remoto |
| `git submodule status` | Lista o estado dos submodules |
| `git submodule deinit <pasta>` | Desativa um submodule |

## Hooks

| Comando | Descrição |
| --- | --- |
| `git config core.hooksPath .githooks` | Define uma pasta versionada de hooks |
| `chmod +x .git/hooks/pre-commit` | Torna um hook executável |
| `git commit --no-verify` | Pula os hooks de commit |

## Bisect

| Comando | Descrição |
| --- | --- |
| `git bisect start` | Inicia a busca binária |
| `git bisect good <hash>` | Marca um commit bom |
| `git bisect bad <hash>` | Marca um commit ruim |
| `git bisect run <script>` | Automatiza a busca |
| `git bisect log` | Mostra o histórico da sessão |
| `git bisect reset` | Encerra e volta ao estado original |

## Worktree

| Comando | Descrição |
| --- | --- |
| `git worktree add <pasta> <branch>` | Cria um worktree para uma branch |
| `git worktree add -b <branch> <pasta>` | Cria worktree com uma nova branch |
| `git worktree list` | Lista os worktrees |
| `git worktree remove <pasta>` | Remove um worktree |
| `git worktree prune` | Limpa referências inválidas |

## Git LFS

| Comando | Descrição |
| --- | --- |
| `git lfs install` | Ativa o LFS na máquina |
| `git lfs track "*.psd"` | Passa a rastrear um tipo de arquivo |
| `git lfs untrack "*.psd"` | Para de rastrear |
| `git lfs ls-files` | Lista os arquivos gerenciados pelo LFS |
| `git lfs pull` | Baixa os arquivos do LFS |
| `git lfs fetch` | Busca os arquivos sem aplicar |
| `git lfs migrate import --include="*.psd"` | Migra arquivos do histórico para o LFS |

## Erros comuns

- **Fazer rebase em commits já publicados**: reescreve o histórico compartilhado.
- **Usar `git reset --hard` sem certeza** e perder alterações.
- **Esquecer `git submodule update --init --recursive`** após clonar.
- **Achar que `git push` envia tags** (use `--tags`).
- **Deixar o repositório em estado de bisect** sem `git bisect reset`.
- **Usar a mesma branch em dois worktrees** (não é permitido).

## Casos de uso

| Situação | Comandos |
| --- | --- |
| Atualizar a feature antes do PR | `git rebase main` |
| Juntar commits locais | `git rebase -i HEAD~n` (squash) |
| Recuperar commits perdidos | `git reflog` + `git reset --hard <hash>` |
| Trazer um hotfix para outra branch | `git cherry-pick <hash>` |
| Achar o commit que causou um bug | `git bisect start` + `good`/`bad` |
| Corrigir um bug sem sair da branch atual | `git worktree add -b hotfix ../hotfix` |
| Versionar arquivos grandes | `git lfs track "*.psd"` |
