---
titulo: git shortlog e log --follow
tipo: comando
nivel: avancado
categoria: Git
tags: [git, shortlog, log, follow, estatisticas, renomeacao]
resumo: "Como gerar estatísticas por autor com git shortlog e seguir renomeações de arquivos com git log --follow."
relacionados: ["Inspeção do histórico", "git range-diff", "Code review"]
fonte: https://git-scm.com/docs/git-shortlog
---

# git shortlog e log --follow

## O que é?

- **`git shortlog`**: resume os commits **por autor** (estatísticas de contribuição).
- **`git log --follow`**: segue um arquivo **mesmo quando ele foi renomeado**, mostrando o histórico completo.

## git shortlog

```bash
# commits agrupados por autor
git shortlog

# apenas a contagem
git shortlog -s

# ordenado por número de commits
git shortlog -sn

# mostra os e-mails
git shortlog -sne

# de um intervalo/branch
git shortlog -sn main..feature
```

Exemplo:

```bash
git shortlog -sn
#  42  Maria Silva
#  18  João Souza
#   7  Ana Lima
```

- Útil para gerar **changelogs** e ver a distribuição de contribuições.

## git log --follow

Por padrão, o `git log` de um arquivo **para** quando o arquivo é renomeado. O `--follow` continua o histórico antes do rename.

```bash
# histórico de um arquivo seguindo renomeações
git log --follow -- arquivo.txt

# resumido
git log --oneline --follow -- arquivo.txt
```

Sem `--follow`:

```
commit ... Renomeia config.js para config.ts
commit ... (fim do histórico rastreado)
```

Com `--follow`, aparecem os commits anteriores ao rename.

## Comandos

| Comando | Descrição |
| --- | --- |
| `git shortlog` | Commits agrupados por autor |
| `git shortlog -sn` | Contagem por autor, ordenada |
| `git shortlog -sne` | Inclui e-mail |
| `git log --follow -- <arquivo>` | Segue renomeações do arquivo |
| `git log --oneline --follow -- <arquivo>` | Versão resumida |

## Erros comuns

- **Achar que `git log -- arquivo` mostra tudo**: ele para nas renomeações.
- **Esperar que `--follow` funcione com múltiplos arquivos** (só aceita um).
- **Confundir `shortlog` com `log`**: o primeiro resume por autor.
- **Ignorar o `--follow`** ao investigar a história de um arquivo.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Ver quem mais contribuiu | `git shortlog -sn` |
| Gerar changelog por autor | `git shortlog` |
| Rastrear um arquivo renomeado | `git log --follow -- arquivo` |
| Ver contribuições em um período | `git shortlog -sn --since="2026-01-01"` |
