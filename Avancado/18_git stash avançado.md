---
titulo: git stash avançado
tipo: comando
nivel: avancado
categoria: Git
tags: [git, stash, parcial, patch, stash-branch, recuperar]
resumo: "Recursos avançados do git stash: stash parcial, create, branch a partir do stash e recuperação de stashes perdidos."
relacionados: ["git stash", "git worktree", "Desfazer alterações (restore, reset, revert)"]
fonte: https://git-scm.com/docs/git-stash
---

# git stash avançado

## O que é?

Além do `git stash` básico, existem formas de guardar **apenas parte** das alterações, criar um stash **sem adicioná-lo à pilha**, transformar um stash em **branch** e até **recuperar um stash perdido**.

## Guardar parcialmente

```bash
# escolhe interativamente os trechos a guardar (patch)
git stash push -p

# guarda apenas arquivos específicos
git stash push -m "WIP" -- src/app.js src/util.js

# guarda apenas o que está preparado (staged)
git stash push --staged
```

## Guardar incluindo untracked e ignorados

```bash
git stash push -u    # inclui não rastreados
git stash push -a    # inclui também os ignorados
```

## Criar sem adicionar à pilha

```bash
# cria um objeto de stash e imprime o hash (não guarda na pilha)
git stash create

# aplica o stash criado
git stash apply <hash>
```

- Útil em scripts: você controla quando aplicar/descartar.

## Criar uma branch a partir do stash

```bash
git stash branch feature-do-stash
```

- Cria uma branch no commit em que o stash foi feito e aplica o stash.
- Se o stash aplicar limpo, ele é removido da pilha.

## Ver e recuperar

```bash
# mostra o diff completo
git stash show -p

# mostra um stash específico
git stash show -p stash@{2}

# lista
git stash list
```

### Recuperar um stash perdido

Se você fez `stash drop`/`clear` por engano, o stash pode estar nos objetos órfãos:

```bash
git fsck --unreachable | grep commit
git show <hash>
git stash apply <hash>
```

## Comandos

| Comando | Descrição |
| --- | --- |
| `git stash push -p` | Guarda trechos selecionados |
| `git stash push --staged` | Guarda apenas o stage |
| `git stash push -- <arquivos>` | Guarda arquivos específicos |
| `git stash create` | Cria stash sem guardar na pilha |
| `git stash branch <nome>` | Cria branch a partir do stash |
| `git stash show -p` | Mostra o diff do stash |

## Erros comuns

- **Guardar tudo quando queria só um arquivo** (esqueça o pathspec).
- **Perder stash com `clear`** e não saber recuperar via `fsck`.
- **Aplicar stash sobre código muito diferente**, gerando conflitos.
- **Confundir `--staged` com o stash padrão**.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Guardar só parte do trabalho | `git stash push -p` |
| Continuar um WIP em branch nova | `git stash branch feature` |
| Usar stash em script | `git stash create` |
| Recuperar stash apagado | `git fsck --unreachable` + `apply` |
