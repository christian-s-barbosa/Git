---
titulo: git notes
tipo: comando
nivel: avancado
categoria: Git
tags: [git, notes, anotacoes, metadados, review, ci]
resumo: "Como anexar anotações a commits com git notes, sem alterar o histórico, e como compartilhá-las."
relacionados: ["Inspeção do histórico", "Code review", "Git em CI-CD"]
fonte: https://git-scm.com/docs/git-notes
---

# git notes

## O que é?

O `git notes` permite **anexar anotações** a objetos (geralmente commits) **sem alterar o commit** nem seu hash. É como um "post-it" colado no commit.

Como não muda o hash, as notas podem ser adicionadas **depois** que o commit já foi publicado.

## Comandos básicos

```bash
# adiciona uma nota ao commit atual
git notes add -m "Revisado por Maria"

# adiciona a um commit específico
git notes add <hash> -m "Nota"

# mostra a nota de um commit
git notes show <hash>

# edita a nota
git notes edit <hash>

# remove a nota
git notes remove <hash>

# lista todas as notas
git notes list
```

## Ver notas no log

```bash
git log --show-notes
git log --notes=refs/notes/commits
```

## Compartilhar notas (push/pull)

As notas ficam em uma ref própria e **não** vão no push comum:

```bash
# enviar as notas
git push origin refs/notes/commits

# buscar as notas
git fetch origin refs/notes/commits:refs/notes/commits
```

Configure para buscar sempre:

```bash
git config --add remote.origin.fetch "+refs/notes/*:refs/notes/*"
```

## Usos comuns

- Registrar o resultado de **code review**.
- Anotar o status de **CI/build** em um commit.
- Vincular **tickets** (ex.: `JIRA-123`) a commits.
- Guardar observações que não cabem na mensagem do commit.

## Erros comuns

- **Achar que as notas são enviadas no `git push` normal**: é preciso enviar a ref.
- **Esperar que as notas alterem o commit**: elas são objetos separados.
- **Confundir nota com a mensagem do commit**.
- **Não configurar o fetch das notas**, ficando sem vê-las em outros clones.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Marcar um commit como revisado | `git notes add -m "Revisado"` |
| Ver a nota no histórico | `git log --show-notes` |
| Compartilhar notas | `git push origin refs/notes/commits` |
| Vincular um ticket | `git notes add -m "JIRA-123"` |
