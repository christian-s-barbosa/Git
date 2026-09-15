---
titulo: Comandos Avançados do Git
tipo: referencia
nivel: avancado
categoria: Git
tags: [git, comandos, cli, cheatsheet, avancado]
resumo: "Cheatsheet dos comandos avançados do Git (subtree, filter-repo, refspecs, sparse-checkout, bundle etc.)."
relacionados: ["Comandos Intermediários do Git", "Comandos Básicos do Git", "git subtree"]
fonte: https://git-scm.com/docs
---

# Comandos Avançados do Git

## Subtree

| Comando | Descrição |
| --- | --- |
| `git subtree add --prefix=<dir> <url> <branch> --squash` | Adiciona um subtree |
| `git subtree pull --prefix=<dir> <url> <branch>` | Atualiza o subtree |
| `git subtree push --prefix=<dir> <url> <branch>` | Envia mudanças do subtree |
| `git subtree split --prefix=<dir> -b <branch>` | Separa o subtree em uma branch |

## Patches (am / format-patch)

| Comando | Descrição |
| --- | --- |
| `git format-patch -1` | Gera patch do último commit |
| `git format-patch main..feature` | Gera patches de um intervalo |
| `git am *.patch` | Aplica patches como commits |
| `git am -3 <patch>` | Aplica com resolução 3-way |
| `git am --continue` / `--abort` / `--skip` | Continua / cancela / pula |
| `git apply <patch>` | Aplica um diff sem commitar |

## rerere

| Comando | Descrição |
| --- | --- |
| `git config --global rerere.enabled true` | Ativa o rerere |
| `git rerere status` | Mostra o estado |
| `git rerere diff` | Mostra o que foi aplicado |
| `git rerere forget <arquivo>` | Esquece uma resolução |

## sparse-checkout

| Comando | Descrição |
| --- | --- |
| `git sparse-checkout init --cone` | Inicializa no modo cone |
| `git sparse-checkout set <dirs>` | Define as pastas incluídas |
| `git sparse-checkout add <dir>` | Adiciona uma pasta |
| `git sparse-checkout list` | Lista as pastas incluídas |
| `git sparse-checkout disable` | Desativa |
| `git sparse-checkout reapply` | Reaplica as regras |

## Manutenção (maintenance)

| Comando | Descrição |
| --- | --- |
| `git maintenance start` | Inicia o agendamento automático |
| `git maintenance stop` | Para o agendamento |
| `git maintenance register` | Registra o repositório |
| `git maintenance run` | Roda as tarefas agora |
| `git maintenance run --task=commit-graph` | Roda uma tarefa específica |

## Refspecs

| Comando | Descrição |
| --- | --- |
| `git push origin local:remota` | Envia com outro nome |
| `git push origin :branch` | Deleta a branch remota |
| `git push --force-with-lease` | Força com segurança |
| `git fetch origin +refs/heads/*:refs/remotes/origin/*` | Refspec explícito |

## Reescrever histórico

| Comando | Descrição |
| --- | --- |
| `git filter-repo --path <x> --invert-paths` | Remove um caminho do histórico |
| `git filter-repo --replace-text <arquivo>` | Substitui textos (segredos) |
| `git filter-repo --path <dir>` | Mantém apenas um caminho |
| `git filter-repo --mailmap <arquivo>` | Renomeia autores |
| `git push --force --all` | Publica o histórico reescrito |

## Notes

| Comando | Descrição |
| --- | --- |
| `git notes add -m "msg" <hash>` | Adiciona uma nota |
| `git notes show <hash>` | Mostra a nota |
| `git notes remove <hash>` | Remove a nota |
| `git log --show-notes` | Mostra as notas no histórico |
| `git push origin refs/notes/commits` | Envia as notas |

## Bundle

| Comando | Descrição |
| --- | --- |
| `git bundle create repo.bundle --all` | Cria um bundle completo |
| `git bundle create x.bundle main~5..main` | Bundle de um intervalo |
| `git bundle verify repo.bundle` | Verifica o bundle |
| `git clone repo.bundle` | Clona a partir do bundle |
| `git fetch repo.bundle <ref>` | Busca refs do bundle |

## Internos

| Comando | Descrição |
| --- | --- |
| `git cat-file -t <hash>` | Tipo do objeto |
| `git cat-file -p <hash>` | Conteúdo do objeto |
| `git hash-object -w --stdin` | Cria um objeto |
| `git ls-tree -r HEAD` | Lista a tree recursivamente |
| `git count-objects -vH` | Tamanho dos objetos |
| `git verify-pack -v <idx>` | Estatísticas de um packfile |

## Limpeza (clean)

| Comando | Descrição |
| --- | --- |
| `git clean -n` | Mostra o que seria removido |
| `git clean -f` | Remove arquivos não rastreados |
| `git clean -fd` | Remove arquivos e pastas não rastreados |
| `git clean -fdx` | Remove também os ignorados |
| `git clean -fX` | Remove apenas os ignorados |
| `git clean -i` | Modo interativo |

## Variantes de rebase

| Comando | Descrição |
| --- | --- |
| `git rebase --onto <nova> <antiga> <branch>` | Move commits para outra base |
| `git rebase --onto main master topic` | Corrige commits na branch errada |
| `git rebase -i --root` | Reescreve todo o histórico |
| `git rebase -i HEAD~3` + `exec <cmd>` | Roda um comando por commit |

## Estatísticas e renomeações

| Comando | Descrição |
| --- | --- |
| `git shortlog` | Commits agrupados por autor |
| `git shortlog -sn` | Contagem por autor, ordenada |
| `git shortlog -sne` | Inclui e-mail |
| `git log --follow -- <arquivo>` | Segue renomeações do arquivo |

## range-diff

| Comando | Descrição |
| --- | --- |
| `git range-diff <base1> <top1> <base2> <top2>` | Compara dois ranges de commits |
| `git range-diff main antigo..novo` | Vê o que mudou após um rebase |
| `git range-diff --no-patch ...` | Saída resumida |

## replace

| Comando | Descrição |
| --- | --- |
| `git replace <antigo> <novo>` | Substitui um objeto |
| `git replace -l` | Lista as substituições |
| `git replace -d <obj>` | Remove uma substituição |
| `git replace --graft <commit> <pai>` | Troca o pai de um commit |

## update-index

| Comando | Descrição |
| --- | --- |
| `git update-index --assume-unchanged <arquivo>` | Ignora verificação (performance) |
| `git update-index --no-assume-unchanged <arquivo>` | Desfaz |
| `git update-index --skip-worktree <arquivo>` | Ignora mudanças locais |
| `git update-index --no-skip-worktree <arquivo>` | Desfaz |
| `git ls-files -v` | Mostra os flags (H/h/S) |

## request-pull

| Comando | Descrição |
| --- | --- |
| `git request-pull <base> <url> <branch>` | Gera pedido de pull por e-mail |

## Stash avançado

| Comando | Descrição |
| --- | --- |
| `git stash push -p` | Guarda trechos selecionados |
| `git stash push --staged` | Guarda apenas o stage |
| `git stash push -- <arquivos>` | Guarda arquivos específicos |
| `git stash create` | Cria stash sem guardar na pilha |
| `git stash branch <nome>` | Cria branch a partir do stash |
| `git stash show -p` | Mostra o diff do stash |

## Interoperabilidade

| Comando | Descrição |
| --- | --- |
| `git svn clone <url>` | Clona um repositório SVN |
| `git svn rebase` | Atualiza com o SVN |
| `git svn dcommit` | Envia commits ao SVN |
| `git p4 clone //depot/projeto@all` | Clona um depot do Perforce |
| `git p4 sync` / `git p4 submit` | Baixa / envia no Perforce |

## Erros comuns

- **Usar `git push --force` em branch compartilhada** (prefira `--force-with-lease`).
- **Reescrever histórico sem backup nem avisar a equipe**.
- **Achar que `git push` envia notas e tags** (refs separadas).
- **Fazer bisect/rebase em clone shallow**, sem histórico completo.
- **Apagar packfiles ou mexer em `.git/objects`** manualmente.

## Casos de uso

| Situação | Comandos |
| --- | --- |
| Reutilizar uma lib externa | `git subtree add` |
| Contribuir por e-mail | `git format-patch` + `git am` |
| Evitar resolver o mesmo conflito | `git config rerere.enabled true` |
| Trabalhar em parte de um monorepo | `git sparse-checkout set` |
| Otimizar repo grande | `git maintenance start` |
| Remover um segredo do histórico | `git filter-repo --replace-text` |
| Transferir commits sem rede | `git bundle create` |
| Limpar build/dependências | `git clean -fdx` |
| Revisar o que mudou após um rebase | `git range-diff` |
| Ignorar alterações locais de um arquivo | `git update-index --skip-worktree` |
| Guardar só parte do trabalho | `git stash push -p` |
| Usar Git com SVN/Perforce | `git svn` / `git p4` |
