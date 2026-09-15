---
titulo: Branches (Ramificações)
tipo: conceito
nivel: basico
categoria: Git
tags: [git, branches, branchs, ramificacoes, merge, conflitos]
resumo: "Conceito de branches, HEAD, branch principal, operações básicas, merge, conflitos e branches remotas."
relacionados: ["Git commit", "Merge avançado", "Fluxos de trabalho"]
fonte: https://git-scm.com/docs/git-branch
---

# Branches (Ramificações)

## O que é?

Uma **branch** (ramificação) é uma **linha independente de desenvolvimento**. Ela permite trabalhar em uma funcionalidade, correção ou teste sem afetar a versão principal do projeto.

No Git, uma branch é apenas um **ponteiro leve e móvel** que aponta para um commit. Criar uma branch **não copia arquivos** nem duplica o projeto — apenas cria um novo ponteiro.

## Como funciona?

- Cada commit aponta para o commit anterior, formando o histórico.
- Uma branch aponta para o **commit mais recente** daquela linha.
- Ao fazer um novo commit, a branch atual **avança automaticamente** para ele.
- O **HEAD** é um ponteiro especial que indica em qual branch você está no momento.

Exemplo:

```
A --- B --- C   (main)
             \
              D --- E   (feature)
```

- `main` aponta para `C`.
- `feature` aponta para `E`.
- `HEAD` indica a branch atual.

## Por que usar?

- **Isolamento**: desenvolver sem quebrar a versão principal.
- **Paralelismo**: várias pessoas (ou tarefas) trabalhando ao mesmo tempo.
- **Segurança**: testar ideias e descartar sem impacto.
- **Organização**: cada funcionalidade/correção em sua própria branch.

## A branch principal

Todo repositório tem uma branch principal, criada por padrão. Historicamente chamada de **master**, hoje costuma ser **main**.

```bash
git branch -m main      # renomeia a branch atual para main
```

É possível definir o nome padrão para novos repositórios:

```bash
git config --global init.defaultBranch main
```

## Operações básicas

| Comando | Descrição |
| --- | --- |
| `git branch` | Lista as branches locais |
| `git branch -a` | Lista branches locais e remotas |
| `git branch nome` | Cria uma nova branch (sem trocar) |
| `git checkout nome` | Troca para uma branch existente |
| `git checkout -b nome` | Cria e troca para uma nova branch |
| `git switch nome` | Troca para uma branch (comando mais recente) |
| `git switch -c nome` | Cria e troca para uma nova branch |
| `git branch -m novo-nome` | Renomeia a branch atual |
| `git branch -d nome` | Remove uma branch já mesclada |
| `git branch -D nome` | Força a remoção de uma branch |

## Fluxo típico de trabalho

```bash
# 1. atualiza a branch principal
git switch main
git pull

# 2. cria uma branch para a tarefa
git switch -c feature/login

# 3. trabalha e faz commits
git add .
git commit -m "Adiciona tela de login"

# 4. envia a branch para o remoto
git push -u origin feature/login

# 5. depois de revisada, a branch é mesclada na main
```

## Merge (mesclagem)

O **merge** une o trabalho de uma branch a outra.

```bash
git switch main
git merge feature/login
```

Existem dois tipos principais:

### Fast-forward

Quando a branch de destino **não mudou** desde que a outra foi criada. O Git apenas **avança o ponteiro**, sem criar um commit novo.

```
A --- B --- C   (main)
             \
              D --- E   (feature)

# após git merge feature/login:
A --- B --- C --- D --- E   (main e feature)
```

### Três vias (three-way)

Quando as duas branches **divergiram**. O Git combina as alterações e cria um **commit de merge**.

```
A --- B --- C -------- M   (main)
       \             /
        D --------- E      (feature)
```

- `M` é o commit de merge, que tem **dois pais** (`C` e `E`).

## Conflitos

Um **conflito** acontece quando as duas branches alteram **as mesmas linhas** de um arquivo de formas diferentes. O Git não sabe qual versão manter e pede uma decisão manual.

O arquivo fica marcado assim:

```
<<<<<<< HEAD
versão da branch atual
=======
versão da outra branch
>>>>>>> feature/login
```

Como resolver:

1. Abra o arquivo e **escolha** o conteúdo correto (removendo as marcações).
2. Marque como resolvido: `git add arquivo.txt`.
3. Finalize o merge: `git commit`.

Para cancelar o merge e voltar atrás:

```bash
git merge --abort
```

## Visualizar o histórico

```bash
git log --oneline --graph --all    # histórico com ramificações
git branch --merged                # branches já mescladas na atual
git branch --no-merged             # branches ainda não mescladas
```

## Branches remotas

Branches também podem existir no repositório remoto (ex.: `origin/main`).

```bash
git push -u origin main            # envia a branch e define o upstream
git push origin feature/login      # envia uma branch específica
git fetch                          # baixa as branches remotas
git switch -c local origin/remota  # cria branch local a partir da remota
```

## Boas práticas

- Use nomes **descritivos** (ex.: `feature/login`, `fix/erro-total`).
- Mantenha branches **curtas** e com um único objetivo.
- Atualize a branch com a principal com frequência.
- **Remova** branches depois do merge.
- Nunca trabalhe direto na branch principal em projetos com equipe.

## Erros comuns

- **Trabalhar direto na `main`** em projetos com equipe.
- **Branches longas**, que acumulam conflitos.
- **Esquecer de trocar de branch** e commitar no lugar errado.
- **Deletar branch sem mesclar** (use `-D` só com certeza).
- **Resolver conflitos escolhendo a versão errada** ou esquecer de remover os marcadores.
- **Não atualizar a branch** com a principal antes do merge.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Criar uma branch para uma feature | `git switch -c feature/x` |
| Trocar de branch | `git switch main` |
| Juntar a feature na main | `git merge feature/x` |
| Listar branches | `git branch` |
| Remover branch já mesclada | `git branch -d feature/x` |
