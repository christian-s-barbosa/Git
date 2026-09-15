---
titulo: Desfazer alterações (restore, reset, revert)
tipo: conceito
nivel: basico
categoria: Git
tags: [git, restore, reset, revert, desfazer, undo, reverter]
resumo: "Como desfazer alterações no working directory, no stage e em commits com restore, reset e revert, e quando usar cada um."
relacionados: ["Os três estados do Git", "Git commit", "git reflog"]
fonte: https://git-scm.com/docs
---

# Desfazer alterações (restore, reset, revert)

## O que é?

O Git oferece formas de **desfazer** alterações, dependendo de **onde** a mudança está (working directory, staging ou commit) e se ela **já foi enviada** para o remoto.

Antes de desfazer, identifique em qual estado está a alteração:

- No **diretório de trabalho** (ainda não preparada).
- Na **área de preparação** (staged).
- Em um **commit** (já salva no histórico).

## git restore

Serve para **desfazer alterações** no diretório de trabalho e no stage.

```bash
# descarta as alterações de um arquivo (volta ao último commit/stage)
git restore arquivo.txt

# remove um arquivo da área de preparação (unstage)
git restore --staged arquivo.txt

# restaura o arquivo a partir de um commit específico
git restore --source=HEAD~1 arquivo.txt
```

> Atenção: `git restore arquivo.txt` **descarta** as alterações não commitadas de forma permanente.

## git reset

Move a branch atual (e o HEAD) para um commit, podendo mexer no stage e no working directory.

```bash
# --soft: desfaz o commit, mas mantém as alterações PREPARADAS (staged)
git reset --soft HEAD~1

# --mixed (padrão): desfaz o commit e tira do stage, mantendo as alterações no working directory
git reset HEAD~1
git reset arquivo.txt        # remove apenas um arquivo do stage

# --hard: desfaz o commit e DESCARTA todas as alterações (perigoso)
git reset --hard HEAD~1
```

| Modo | Commit | Stage | Working directory |
| --- | --- | --- | --- |
| `--soft` | Desfaz | Mantém | Mantém |
| `--mixed` (padrão) | Desfaz | Limpa | Mantém |
| `--hard` | Desfaz | Limpa | **Descarta** |

> `git reset` **reescreve o histórico**. Evite usá-lo em commits que já foram enviados para o remoto.

## git revert

Cria um **novo commit** que desfaz um commit anterior, **sem apagar o histórico**. É a forma **segura** de desfazer em projetos compartilhados.

```bash
git revert <hash>
git revert HEAD          # desfaz o último commit
```

- O commit original permanece no histórico.
- O novo commit contém a alteração inversa.

## reset x revert

| Característica | git reset | git revert |
| --- | --- | --- |
| Como funciona | Move o histórico para trás | Cria um commit inverso |
| Apaga o commit? | Sim (reescreve) | Não |
| Seguro em remoto? | Não | Sim |
| Indicado para | Commits locais | Commits já publicados |

## Qual usar?

| Situação | Comando |
| --- | --- |
| Descartar alterações não commitadas de um arquivo | `git restore arquivo` |
| Tirar um arquivo do stage (unstage) | `git restore --staged arquivo` |
| Desfazer o último commit, mantendo tudo preparado | `git reset --soft HEAD~1` |
| Desfazer o último commit, mantendo as alterações | `git reset HEAD~1` |
| Descartar o último commit e as alterações | `git reset --hard HEAD~1` |
| Desfazer um commit já enviado ao remoto | `git revert <hash>` |
| Cancelar um merge em andamento | `git merge --abort` |

## Boas práticas

- **Nunca** use `reset --hard` sem ter certeza: as alterações são perdidas.
- Em branches compartilhadas, prefira **revert** a **reset**.
- Confirme o estado antes de agir com `git status` e `git log`.

## Erros comuns

- **Usar `reset --hard` sem querer**, perdendo alterações não commitadas.
- **Fazer `reset` em commits já publicados**, reescrevendo histórico compartilhado.
- **Confundir `reset` com `revert`**: um reescreve, o outro cria um commit inverso.
- **Achar que `restore --staged` apaga a alteração**: ele só tira do stage.
- **Não conferir o estado** antes de desfazer.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Descartar alteração de um arquivo | `git restore arquivo` |
| Tirar do stage | `git restore --staged arquivo` |
| Desfazer o último commit (mantendo alterações) | `git reset HEAD~1` |
| Desfazer commit já publicado | `git revert <hash>` |
| Cancelar merge em andamento | `git merge --abort` |
