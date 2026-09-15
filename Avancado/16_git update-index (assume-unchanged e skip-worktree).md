---
titulo: git update-index (assume-unchanged e skip-worktree)
tipo: comando
nivel: avancado
categoria: Git
tags: [git, update-index, assume-unchanged, skip-worktree, flags, sparse]
resumo: "Como marcar arquivos com assume-unchanged e skip-worktree usando git update-index e a diferença entre as flags."
relacionados: ["sparse-checkout", ".gitignore", "Aliases e configurações"]
fonte: https://git-scm.com/docs/git-update-index
---

# git update-index (assume-unchanged e skip-worktree)

## O que é?

O `git update-index` altera o **índice** (staging) e permite marcar arquivos com **flags especiais**. Duas são muito conhecidas: `assume-unchanged` e `skip-worktree`.

## assume-unchanged

Informa ao Git que ele **não precisa verificar** alterações naquele arquivo. É uma otimização de performance — **não** foi feita para ignorar arquivos.

```bash
git update-index --assume-unchanged arquivo.txt

# desfazer
git update-index --no-assume-unchanged arquivo.txt
```

- O Git "assume" que o arquivo não mudou.
- Pode ser **perdido** se o arquivo mudar no remoto.

## skip-worktree

Informa ao Git para **ignorar o arquivo no working directory**, mantendo a versão do índice. É a flag usada internamente pelo **sparse-checkout**.

```bash
git update-index --skip-worktree arquivo.txt

# desfazer
git update-index --no-skip-worktree arquivo.txt
```

- Mais "persistente" que o `assume-unchanged`.
- Recomendada quando você precisa **editar localmente** um arquivo versionado (ex.: configuração).

## Ver os flags

```bash
git ls-files -v
```

| Letra | Significado |
| --- | --- |
| `H` | Normal (rastreado) |
| `h` | assume-unchanged |
| `S` | skip-worktree |

## assume-unchanged x skip-worktree

| Característica | assume-unchanged | skip-worktree |
| --- | --- | --- |
| Objetivo | Performance | Ignorar mudanças locais |
| Persistência | Menor | Maior |
| Usado por | Otimizações | sparse-checkout |
| Ideal para | Arquivos grandes raramente alterados | Config local editável |

## Erros comuns

- **Usar `assume-unchanged` para "ignorar" um arquivo** e se confundir quando ele voltar a aparecer.
- **Esperar que essas flags sejam compartilhadas**: são **locais**.
- **Marcar arquivos que mudam no remoto** e gerar conflitos.
- **Confundir com `.gitignore`**: aqui o arquivo **continua rastreado**.

## Casos de uso

| Situação | Flag |
| --- | --- |
| Arquivo de config local que não deve subir | `skip-worktree` |
| Arquivo grande raramente alterado | `assume-unchanged` |
| Reduzir verificações de performance | `assume-unchanged` |
| Trabalhar com sparse-checkout | `skip-worktree` (automático) |
