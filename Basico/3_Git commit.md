---
titulo: Git commit
tipo: conceito
nivel: basico
categoria: Git
tags: [git, commit, versionamento, historico, staging]
resumo: "O que é um commit, como funciona, ciclo de vida dos arquivos, mensagens, boas práticas e como alterar ou desfazer commits."
relacionados: ["Os três estados do Git", "Branches (Ramificações)", "Desfazer alterações (restore, reset, revert)"]
fonte: https://git-scm.com/docs/git-commit
---

# Git commit

## O que é?

Um **commit** é o registro de um conjunto de alterações no repositório. Ele funciona como uma **foto (snapshot)** do projeto em um determinado momento e fica gravado permanentemente no histórico.

Cada commit:

- É identificado por um **código único** (hash), como `3f2a1b9c`.
- Guarda o **autor**, a **data**, a **mensagem** e o estado dos arquivos.
- Aponta para o commit anterior, formando uma **linha do tempo** (histórico).

## Como funciona?

O commit é o passo final do fluxo de três áreas do Git:

```
Working Directory  --git add-->  Staging Area  --git commit-->  Repositório
```

1. Você edita os arquivos no **diretório de trabalho**.
2. Seleciona o que vai entrar no commit com `git add` (**staging area**).
3. Salva o conjunto com `git commit` (**repositório**).

Pontos importantes:

- O commit grava **apenas o que está na área de preparação**, não tudo o que foi alterado.
- O Git guarda **snapshots** completos, e não apenas as diferenças.
- Cada commit aponta para o commit anterior, ligando os registros em cadeia.
- O primeiro commit do projeto **não tem pai**.
- Um commit de merge pode ter **dois ou mais pais**.

## Ciclo de vida dos arquivos

Um arquivo passa por estados até ser commitado:

| Estado | Descrição |
| --- | --- |
| **Não rastreado (untracked)** | O Git ainda não conhece o arquivo |
| **Não modificado (unmodified)** | Arquivo rastreado e sem alterações desde o último commit |
| **Modificado (modified)** | Arquivo rastreado que foi alterado |
| **Preparado (staged)** | Alteração marcada para entrar no próximo commit |

Fluxo:

```
untracked --git add--> staged --git commit--> unmodified
unmodified --edição--> modified --git add--> staged
```

## Anatomia de um commit

Ao rodar `git log`, cada commit mostra:

```
commit 3f2a1b9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a
Author: Seu Nome <seu@email.com>
Date:   Mon Sep 14 10:30:00 2026 -0300

    Adiciona a página inicial
```

- **Hash**: identificador único gerado a partir do conteúdo (algoritmo SHA-1).
- **Author**: quem criou o commit (definido em `user.name` e `user.email`).
- **Date**: data e hora do commit.
- **Mensagem**: descrição do que foi feito.

## Criando commits

```bash
# prepara os arquivos
git add arquivo.txt

# cria o commit com mensagem
git commit -m "Adiciona arquivo de configuração"

# cria o commit abrindo o editor de texto
git commit

# adiciona arquivos já rastreados e commita de uma vez
git commit -am "Corrige erro de digitação"
```

## Mensagem de commit

A mensagem deve explicar **o que** e **por que** a alteração foi feita. Uma boa prática:

1. Uma **linha curta** (até ~50 caracteres) resumindo a mudança.
2. Uma **linha em branco**.
3. Um **corpo** com detalhes, se necessário.

```bash
git commit -m "Corrige cálculo do total" -m "O valor era somado duas vezes quando havia desconto."
```

Convenção comum (Conventional Commits):

| Prefixo | Uso |
| --- | --- |
| `feat:` | Nova funcionalidade |
| `fix:` | Correção de bug |
| `docs:` | Alteração na documentação |
| `style:` | Formatação, sem mudar o código |
| `refactor:` | Refatoração sem mudar o comportamento |
| `test:` | Testes |
| `chore:` | Tarefas gerais |

## Quando fazer um commit?

- Um commit por **mudança lógica** concluída.
- Commits **pequenos e frequentes** são melhores que um commit gigante.
- Nunca commitar arquivos temporários, segredos ou senhas (use o `.gitignore`).
- Sempre escrever uma mensagem clara.

## Commits e o histórico

```bash
git log --oneline              # histórico resumido
git log --oneline --graph      # histórico com ramificações
git show <hash>                # detalhes de um commit
git diff                       # alterações ainda não preparadas
git diff --staged              # alterações já preparadas
```

## Alterar e desfazer commits

```bash
git commit --amend             # corrige o último commit (mensagem/conteúdo)
git reset HEAD~1               # desfaz o último commit, mantendo as alterações
git reset --hard HEAD          # descarta todas as alterações não commitadas
```

> Atenção: `--amend` e `reset` **reescrevem o histórico**. Evite usá-los em commits que já foram enviados para o repositório remoto.

## Commit x push

- **commit**: salva a alteração no repositório **local**.
- **push**: envia os commits locais para o repositório **remoto**.

Ou seja, é possível fazer vários commits sem internet e enviá-los depois com `git push`.

## Erros comuns

- **Commitar tudo sem revisar** (`git add .` às cegas), incluindo arquivos indesejados.
- **Mensagens vagas** ("update", "fix"), dificultando o histórico.
- **Um commit gigante** misturando vários assuntos.
- **Commitar segredos** (`.env`, senhas, chaves).
- **Usar `--amend` em commit já enviado**, reescrevendo histórico público.
- **Confundir commit com push**: o commit é local.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Salvar uma alteração concluída | `git commit -m "..."` |
| Corrigir a mensagem do último commit | `git commit --amend` |
| Commitar só arquivos já rastreados | `git commit -am "..."` |
| Desfazer o último commit mantendo alterações | `git reset HEAD~1` |
| Ver o que foi commitado | `git show <hash>` |
