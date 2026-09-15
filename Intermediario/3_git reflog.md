---
titulo: git reflog
tipo: comando
nivel: intermediario
categoria: Git
tags: [git, reflog, recuperacao, head, commits-perdidos]
resumo: "O registro de movimentos do HEAD e como recuperar commits e branches perdidos com git reflog."
relacionados: ["Desfazer alterações (restore, reset, revert)", "Inspeção do histórico", "git bisect"]
fonte: https://git-scm.com/docs/git-reflog
---

# git reflog

## O que é?

O `git reflog` (reference log) é um **registro de todos os movimentos** das referências do Git — principalmente o **HEAD**. Ele guarda um histórico de onde o HEAD e as branches estiveram, mesmo que esses commits **não apareçam mais** no `git log`.

É a principal ferramenta para **recuperar commits e branches "perdidos"**.

## Como funciona?

Cada vez que o HEAD muda (commit, checkout, reset, rebase, merge), o Git registra uma entrada no reflog:

```
3f2a1b9 HEAD@{0}: commit: Adiciona rodapé
8c1d4e2 HEAD@{1}: reset: moving to HEAD~1
a7b3f10 HEAD@{2}: commit: Corrige cabeçalho
```

- `HEAD@{0}` é o estado **mais recente**.
- Quanto maior o número, **mais antigo** o registro.

## Comandos

```bash
# mostra o reflog do HEAD
git reflog

# mostra o reflog de uma branch específica
git reflog show main

# mostra o reflog com datas
git reflog --date=iso
```

## Recuperar commits e branches

Se você fez um `reset --hard` e "perdeu" commits, eles continuam no reflog por um tempo.

```bash
# 1. encontre o commit desejado no reflog
git reflog

# 2. volte para ele
git reset --hard <hash>

# ou crie uma branch a partir dele
git branch recuperada <hash>
```

## reflog x log

| Característica | git log | git reflog |
| --- | --- | --- |
| Mostra | Histórico de commits da branch | Movimentos do HEAD/referências |
| Inclui commits "perdidos" | Não | Sim |
| Uso principal | Consultar o histórico | Recuperar estados anteriores |
| Compartilhado no remoto | Sim | Não (é local) |

## Retenção

- O reflog é **local** (não vai para o remoto).
- As entradas expiram por padrão após cerca de **90 dias** (e as inalcançáveis, ~30 dias).
- Após esse período, a recuperação pode não ser mais possível.

## Cuidados

- O reflog registra **todos** os movimentos, então serve também para auditoria local.
- Recuperar com `reset --hard` descarta o estado atual: confirme o hash correto antes.

## Erros comuns

- **Não saber que o reflog existe** e achar que commits perdidos sumiram de vez.
- **Fazer `reset --hard` sem conferir o hash**, descartando o estado atual indevidamente.
- **Esperar demais** para recuperar: as entradas expiram (cerca de 90 dias).
- **Confundir `reflog` com `log`**: o reflog é local e mostra movimentos, não só commits.
- **Apagar a pasta `.git`** (ou clonar de novo) e perder o reflog, impossibilitando a recuperação local.

## Casos de uso

| Cenário | Comando |
| --- | --- |
| Recuperar commits após um `reset --hard` | `git reflog` + `git reset --hard <hash>` |
| Recuperar uma branch deletada | `git branch recuperada <hash>` |
| Desfazer um rebase/merge mal feito | `git reflog` + `git reset --hard HEAD@{n}` |
| Ver o histórico de movimentos do HEAD | `git reflog` |
