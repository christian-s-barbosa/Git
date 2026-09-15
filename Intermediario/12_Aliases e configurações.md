---
titulo: Aliases e configurações
tipo: conceito
nivel: intermediario
categoria: Git
tags: [git, alias, config, configuracao, includeIf, produtividade]
resumo: "Como criar aliases e ajustar configurações do Git nos níveis global, local e condicional, com opções úteis."
relacionados: ["Repositório Local e Remoto", "git hooks", "Refspecs"]
fonte: https://git-scm.com/docs/git-config
---

# Aliases e configurações

## O que é?

**Aliases** são **atalhos** que você cria para comandos do Git. Em vez de digitar `git status`, você pode digitar `git st`. Já as **configurações** ajustam o comportamento do Git (editor, estratégia de pull, fim de linha, etc.).

## Níveis de configuração

| Nível | Escopo | Arquivo |
| --- | --- | --- |
| `--system` | Toda a máquina | `gitconfig` do sistema |
| `--global` | Seu usuário | `~/.gitconfig` |
| `--local` | Repositório atual | `.git/config` |

O nível mais específico **sobrescreve** o mais genérico (local > global > system).

## Criar aliases

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage "restore --staged"
```

Depois:

```bash
git st          # equivale a git status
git unstage arquivo.txt
```

## Aliases com shell

Use `!` para executar comandos do sistema:

```bash
git config --global alias.lg "log --oneline --graph --all --decorate"
git config --global alias.last "log -1 HEAD"
git config --global alias.aliases "config --get-regexp ^alias\."
```

```bash
git config --global alias.cleanup "!git branch --merged | grep -v main | xargs -n 1 git branch -d"
```

## Gerenciar aliases

```bash
# listar todos os aliases
git config --get-regexp ^alias\.

# remover um alias
git config --global --unset alias.st
```

## Configurações úteis

| Configuração | Efeito |
| --- | --- |
| `core.editor "code --wait"` | Define o editor padrão |
| `init.defaultBranch main` | Nome padrão da branch inicial |
| `pull.rebase true` | Faz rebase em vez de merge no `pull` |
| `push.default current` | Envia a branch atual para a de mesmo nome |
| `merge.conflictStyle zdiff3` | Mostra a versão base nos conflitos |
| `core.autocrlf true` | Conversão de fim de linha (Windows) |
| `rerere.enabled true` | Reaproveita resolução de conflitos |

```bash
git config --global pull.rebase true
git config --global push.default current
```

## Ver a origem das configurações

```bash
git config --list --show-origin
```

Mostra **de qual arquivo** veio cada configuração.

## Configuração condicional (includeIf)

Aplica configurações diferentes por pasta (útil para trabalho x pessoal):

```ini
[includeIf "gitdir:~/trabalho/"]
    path = ~/.gitconfig-trabalho
```

## Erros comuns

- **Criar alias com o mesmo nome de um comando existente**, sobrescrevendo o comportamento.
- **Configurar global quando queria local** (ou vice-versa).
- **Usar `!` sem entender** que o comando roda no shell.
- **Esquecer aspas** em aliases com espaços/argumentos.

## Casos de uso

| Situação | Configuração |
| --- | --- |
| Encurtar comandos do dia a dia | `alias.st`, `alias.co` |
| Histórico visual rápido | `alias.lg` |
| Padronizar o pull com rebase | `pull.rebase true` |
| Usar usuário diferente por pasta | `includeIf` |
| Descobrir de onde vem uma config | `config --show-origin` |
