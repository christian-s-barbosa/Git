---
titulo: git clean e arquivos não rastreados
tipo: comando
nivel: avancado
categoria: Git
tags: [git, clean, untracked, limpeza, arquivos-nao-rastreados]
resumo: "Como remover arquivos não rastreados com git clean, suas opções e a diferença para restore e reset."
relacionados: [".gitignore", "Desfazer alterações (restore, reset, revert)", "Manutenção do repositório"]
fonte: https://git-scm.com/docs/git-clean
---

# git clean e arquivos não rastreados

## O que é?

O `git clean` **remove arquivos não rastreados** do diretório de trabalho — ou seja, arquivos que o Git ainda não conhece. É usado para "limpar" o projeto de arquivos gerados, temporários ou criados por engano.

> É uma operação **irreversível**: os arquivos removidos **não** vão para o reflog nem para o lixo do Git.

## Opções

| Opção | Efeito |
| --- | --- |
| `-n` / `--dry-run` | Mostra o que seria removido, sem remover |
| `-f` | Confirma a remoção (obrigatório se `clean.requireForce`) |
| `-d` | Inclui diretórios não rastreados |
| `-x` | Inclui arquivos **ignorados** pelo `.gitignore` |
| `-X` | Remove **apenas** os ignorados |
| `-i` | Modo interativo |

## Exemplos

```bash
# ver o que seria removido (sempre faça isso antes)
git clean -n

# remove arquivos não rastreados
git clean -f

# remove arquivos e pastas não rastreados
git clean -fd

# remove também os ignorados (ex.: build/, node_modules/)
git clean -fdx

# remove apenas os ignorados
git clean -fX
```

## clean x restore x reset

| Comando | O que faz |
| --- | --- |
| `git clean` | Remove arquivos **não rastreados** |
| `git restore` | Desfaz alterações em arquivos **rastreados** |
| `git reset` | Move o histórico/stage |

- `clean` age sobre o que o Git **não conhece**.
- `restore`/`reset` agem sobre o que o Git **já rastreia**.

## Erros comuns

- **Rodar `git clean -fdx` sem `-n`** e apagar arquivos que precisava.
- **Achar que dá para recuperar** os arquivos removidos (não dá).
- **Confundir `clean` com `restore`** e não limpar o que queria.
- **Esquecer o `-d`** e não remover pastas.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Ver arquivos temporários | `git clean -n` |
| Limpar build/dependências | `git clean -fdx` |
| Remover pastas não rastreadas | `git clean -fd` |
| Limpar só o que está ignorado | `git clean -fX` |
| Revisar antes de apagar | `git clean -i` |
