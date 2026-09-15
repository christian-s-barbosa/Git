---
titulo: git stash
tipo: comando
nivel: basico
categoria: Git
tags: [git, stash, temporario, wip, guardar]
resumo: "Como guardar e recuperar alterações temporárias com git stash, listar, aplicar e remover stashes."
relacionados: ["git stash avançado", "Desfazer alterações (restore, reset, revert)", "git worktree"]
fonte: https://git-scm.com/docs/git-stash
---

# git stash

## O que é?

O `git stash` **guarda temporariamente** as alterações não commitadas (do working directory e do stage) em uma pilha, deixando a pasta de trabalho **limpa**. Depois, essas alterações podem ser **recuperadas** quando você quiser.

É útil para "deixar de lado" o que você estava fazendo sem precisar commitar.

## Por que usar?

- Você precisa **trocar de branch** mas tem alterações incompletas.
- Precisa fazer um `pull` e não quer misturar com o trabalho atual.
- Quer testar algo rapidamente e depois voltar ao que estava fazendo.
- Não quer criar um commit "pela metade".

## Guardar alterações

```bash
# guarda as alterações rastreadas
git stash

# guarda com uma descrição (recomendado)
git stash push -m "WIP tela de login"

# inclui arquivos não rastreados (untracked)
git stash -u

# inclui também arquivos ignorados pelo .gitignore
git stash -a
```

Após o `stash`, a pasta de trabalho volta ao estado do último commit.

## Listar os stashes

```bash
git stash list
```

Exemplo de saída:

```
stash@{0}: On main: WIP tela de login
stash@{1}: WIP on main: 3f2a1b9 Adiciona rodapé
```

- Cada stash recebe um índice (`stash@{0}` é o mais recente).

## Recuperar alterações

```bash
# aplica o último stash e o remove da pilha
git stash pop

# aplica o stash sem removê-lo da pilha
git stash apply

# aplica um stash específico
git stash pop stash@{1}
git stash apply stash@{1}
```

- **pop** = apply + drop.
- **apply** mantém o stash guardado.

## Remover stashes

```bash
# remove um stash específico
git stash drop stash@{0}

# remove todos os stashes
git stash clear
```

## Ver o conteúdo

```bash
# resume as alterações de um stash
git stash show

# mostra o diff completo
git stash show -p
```

## Comandos

| Comando | Descrição |
| --- | --- |
| `git stash` | Guarda as alterações rastreadas |
| `git stash push -m "msg"` | Guarda com descrição |
| `git stash -u` | Inclui arquivos não rastreados |
| `git stash list` | Lista os stashes |
| `git stash pop` | Aplica e remove o último stash |
| `git stash apply` | Aplica sem remover |
| `git stash drop` | Remove um stash |
| `git stash clear` | Remove todos os stashes |
| `git stash show -p` | Mostra o diff do stash |

## Observações

- O `stash` é **local**: não é enviado para o repositório remoto com `git push`.
- Não é um substituto para commits: use para trabalho **temporário**.
- Conflitos podem ocorrer ao aplicar um stash sobre um código que mudou.

## Erros comuns

- **Usar o stash como se fosse commit** e esquecer as alterações guardadas.
- **Perder um stash** com `git stash clear` sem conferir.
- **Aplicar stash na branch errada**, gerando conflitos.
- **Esquecer o `-u`** e não guardar arquivos novos (untracked).
- **Confiar no stash para algo permanente**: ele é temporário e local.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Guardar trabalho para trocar de branch | `git stash push -m "msg"` |
| Guardar incluindo arquivos novos | `git stash -u` |
| Listar o que está guardado | `git stash list` |
| Recuperar e remover | `git stash pop` |
| Recuperar sem remover | `git stash apply` |
