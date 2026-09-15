---
titulo: Merge avançado
tipo: conceito
nivel: intermediario
categoria: Git
tags: [git, merge, no-ff, squash, ff-only, mergetool, estrategias, conflitos]
resumo: "Opções e estratégias de merge (--no-ff, --squash, --ff-only, octopus), resolução de conflitos e git mergetool."
relacionados: ["Branches (Ramificações)", "git rebase", "git rerere"]
fonte: https://git-scm.com/docs/git-merge
---

# Merge avançado

## O que é?

Além do merge comum, o Git oferece **opções e estratégias** para controlar como as branches são unidas e como os conflitos são resolvidos. Isso dá mais controle sobre o formato do histórico.

## Opções principais

| Opção | Efeito |
| --- | --- |
| `--ff` (padrão) | Faz fast-forward quando possível |
| `--no-ff` | **Sempre** cria um commit de merge, mesmo que dê fast-forward |
| `--ff-only` | Só faz merge se for fast-forward; caso contrário, falha |
| `--squash` | Junta as alterações em um único conjunto, **sem** commit de merge |
| `-m "msg"` | Define a mensagem do commit de merge |

```bash
git merge --no-ff feature/login -m "Mescla feature/login"
git merge --ff-only feature/login
git merge --squash feature/login
git commit -m "Adiciona login (squash)"
```

- `--no-ff` preserva o registro de que existiu uma branch (útil em Git Flow).
- `--squash` não cria o merge: você precisa commitar depois.

## Estratégias de merge

| Estratégia | Uso |
| --- | --- |
| `ort` (padrão) | Merge de duas branches |
| `ours` | Ignora totalmente a outra branch |
| `octopus` | Une mais de duas branches |
| `subtree` | Ajustada para subárvores |

```bash
git merge -s octopus branch1 branch2 branch3
```

## Resolução automática de conflitos

Com `-X`, você escolhe um lado em caso de conflito:

```bash
# em conflito, prefere a versão da branch atual
git merge -X ours feature

# em conflito, prefere a versão da outra branch
git merge -X theirs feature
```

> `-X ours` só resolve **conflitos**; o restante das alterações é mesclado normalmente.

## Ferramenta visual (mergetool)

```bash
git mergetool
```

Abre uma ferramenta gráfica para resolver conflitos. Configure a preferida:

```bash
git config --global merge.tool vscode
```

## Durante um conflito

```bash
# lista os arquivos em conflito
git diff --name-only --diff-filter=U

# escolhe a versão da branch atual (ours)
git checkout --ours arquivo.txt

# escolhe a versão da outra branch (theirs)
git checkout --theirs arquivo.txt

# marca como resolvido
git add arquivo.txt
git commit

# cancela o merge
git merge --abort
```

## Erros comuns

- **Usar `-X ours` achando que descarta a outra branch**: ele só decide nos conflitos.
- **Confundir `--squash` com `--no-ff`**: o squash não cria merge commit.
- **Fazer `--ff-only` quando as branches divergiram** e receber erro.
- **Resolver conflitos sem revisar** e commitar código quebrado.
- **Esquecer de `git add`** antes de finalizar o merge.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Preservar o histórico da feature | `git merge --no-ff feature` |
| Entrar com um único commit | `git merge --squash feature` |
| Garantir histórico linear | `git merge --ff-only feature` |
| Resolver conflitos visualmente | `git mergetool` |
| Unir várias branches de uma vez | `git merge -s octopus a b c` |
