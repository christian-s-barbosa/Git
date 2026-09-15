---
titulo: Variantes de rebase (--onto e --root)
tipo: comando
nivel: avancado
categoria: Git
tags: [git, rebase, onto, root, exec, reescrita]
resumo: "Como usar git rebase --onto e --root para mover commits entre bases e reescrever todo o histórico."
relacionados: ["git rebase", "git cherry-pick", "git range-diff"]
fonte: https://git-scm.com/docs/git-rebase
---

# Variantes de rebase (--onto e --root)

## O que é?

Além do rebase comum, o Git oferece variantes para cenários específicos de **mover commits entre bases** e **reescrever todo o histórico**.

## git rebase --onto

Move um intervalo de commits de uma base para outra.

```
git rebase --onto <nova-base> <antiga-base> <branch>
```

- `<antiga-base>`: de onde os commits serão "desencaixados" (exclusivo).
- `<nova-base>`: onde serão reaplicados.
- `<branch>`: branch a ser movida (opcional; padrão é a atual).

### Exemplo

```
        A --- B --- C   (feature)
       /
D --- E --- F --- G     (main)
```

Quer mover apenas `B` e `C` (sem `A`) para cima de `G`:

```bash
git rebase --onto main feature~2 feature
```

Resultado: `B'` e `C'` passam a partir de `G`.

### Caso clássico

Remover commits que foram feitos na branch errada:

```bash
# move os commits de "topic" para cima da main
git rebase --onto main master topic
```

## git rebase --root

Reaplica **todos** os commits desde o primeiro (o root), reescrevendo o histórico inteiro.

```bash
git rebase --root
git rebase -i --root
```

- Útil para **editar o primeiro commit** ou reescrever tudo de uma vez.
- Muito perigoso em repositórios compartilhados.

## Rebase interativo com exec

Executa um comando após cada commit durante o rebase:

```bash
git rebase -i HEAD~3
# na lista, adicione:
# pick abc123 ...
# exec npm test
```

- `exec`: roda o comando a cada parada (ex.: testar cada commit).

## Cuidados

- **Nunca** faça rebase de commits já publicados sem combinar com a equipe.
- Sempre tenha um **backup** ou confie no `reflog`.
- Use `git rebase --abort` para cancelar.

## Erros comuns

- **Confundir a ordem dos argumentos** do `--onto`.
- **Usar `--root`** sem necessidade e reescrever tudo.
- **Reaplicar commits errados** por informar a base errada.
- **Esquecer que os hashes mudam** após o rebase.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Mover commits de uma base para outra | `git rebase --onto nova antiga branch` |
| Corrigir commits na branch errada | `git rebase --onto main master topic` |
| Editar o primeiro commit | `git rebase -i --root` |
| Testar cada commit do rebase | `rebase -i` + `exec` |
