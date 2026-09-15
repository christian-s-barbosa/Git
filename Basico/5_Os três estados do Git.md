---
titulo: Os três estados do Git
tipo: conceito
nivel: basico
categoria: Git
tags: [git, working-directory, staging-area, index, repositorio, estados]
resumo: "Os três estados do Git (working directory, staging e repositório), o ciclo de vida dos arquivos e os comandos que mudam de estado."
relacionados: ["Git commit", "Desfazer alterações (restore, reset, revert)", ".gitignore"]
fonte: https://git-scm.com/book/pt-br/v2
---

# Os três estados do Git

## O que é?

No Git, todo arquivo pode estar em **três estados principais**. Entender isso é a base para usar o Git corretamente, pois cada comando move o arquivo de um estado para outro.

| Estado | Nome em inglês | Onde fica |
| --- | --- | --- |
| **Diretório de trabalho** | Working Directory | Na sua pasta do projeto |
| **Área de preparação** | Staging Area / Index | Dentro do `.git` |
| **Repositório** | Repository | Dentro do `.git` (commits) |

## Os três estados

### 1. Diretório de trabalho (Working Directory)

É a pasta onde você vê e edita os arquivos. É uma **cópia** de uma versão do projeto, extraída do repositório para você trabalhar.

- Alterações aqui ainda **não** foram registradas.
- Aparecem como **modificadas** ou **não rastreadas** no `git status`.

### 2. Área de preparação (Staging Area / Index)

É uma área intermediária onde você **seleciona** o que vai entrar no próximo commit. Também chamada de **index**.

- Você adiciona arquivos aqui com `git add`.
- Permite montar um commit apenas com parte das alterações.
- Aparecem como **preparadas (staged)** no `git status`.

### 3. Repositório (Repository)

É onde os commits ficam **gravados permanentemente** no histórico, dentro da pasta oculta `.git`.

- Atingido com `git commit`.
- Os arquivos passam a ser considerados **não modificados** até serem editados de novo.

## O fluxo

```
+---------------------+   git add    +------------------+   git commit   +---------------+
| Diretório de        | -----------> | Área de          | -------------> | Repositório   |
| trabalho (working)  |              | preparação       |                | (commits)     |
+---------------------+              | (staging/index)  |                +---------------+
          ^                          +------------------+                       |
          |                                                                      |
          +--------------------------- git checkout / git restore --------------+
```

- `git add`: working directory → staging area.
- `git commit`: staging area → repositório.
- `git restore` / `git checkout`: repositório → working directory.

## Ciclo de vida de um arquivo

| Estado | Descrição |
| --- | --- |
| **Não rastreado (untracked)** | O Git ainda não conhece o arquivo |
| **Não modificado (unmodified)** | Arquivo rastreado e sem alterações desde o último commit |
| **Modificado (modified)** | Arquivo rastreado que foi alterado no working directory |
| **Preparado (staged)** | Alteração marcada para entrar no próximo commit |

## Por que existe a área de preparação?

A staging area existe para dar **controle** sobre o que será commitado:

- Permite commitar **apenas parte** das alterações.
- Possibilita revisar (`git diff --staged`) antes de salvar.
- Ajuda a manter commits **pequenos e organizados**.

## Exemplo prático

```bash
# 1. cria um arquivo (fica "untracked")
echo "Olá" > index.html

# 2. verifica o estado
git status

# 3. move para a área de preparação
git add index.html

# 4. confirma o que está preparado
git diff --staged

# 5. grava no repositório
git commit -m "Adiciona index.html"

# 6. o arquivo agora está "não modificado"
git status
```

## Comandos que mudam o estado

| Comando | De → Para |
| --- | --- |
| `git add <arquivo>` | Working → Staging |
| `git commit` | Staging → Repositório |
| `git restore <arquivo>` | Staging → Working (descarta alterações) |
| `git restore --staged <arquivo>` | Staging → Working (remove do stage) |
| `git reset` | Repositório → Staging/Working |
| `git checkout <arquivo>` | Repositório → Working |

## Erros comuns

- **Achar que `git add` já salva no histórico**: ele só move para o stage.
- **Confundir `git commit` com `git add`**.
- **Usar `git add .` sem revisar** o que será preparado.
- **Não entender por que um arquivo não aparece** no `git status` (pode estar ignorado).
- **Perder alterações com `git restore`** sem querer.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Ver o estado atual | `git status` |
| Preparar um arquivo | `git add arquivo` |
| Preparar tudo | `git add .` |
| Remover do stage | `git restore --staged arquivo` |
| Descartar alteração local | `git restore arquivo` |
| Gravar no histórico | `git commit -m "..."` |
