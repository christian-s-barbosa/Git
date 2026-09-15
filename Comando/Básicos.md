---
titulo: Comandos Básicos do Git
tipo: referencia
nivel: basico
categoria: Git
tags: [git, comandos, cli, cheatsheet]
resumo: "Cheatsheet dos comandos básicos do Git agrupados por categoria, com erros comuns e casos de uso."
relacionados: ["Comandos Intermediários do Git", "Comandos Avançados do Git", "Git commit"]
fonte: https://git-scm.com/docs
---

# Comandos Básicos do Git

## Configuração

| Comando | Descrição |
| --- | --- |
| `git config --global user.name "Nome"` | Define o nome do autor dos commits |
| `git config --global user.email "email"` | Define o e-mail do autor dos commits |
| `git config --global core.editor "editor"` | Define o editor padrão |
| `git config --global init.defaultBranch main` | Define o nome padrão da branch inicial |
| `git config --list` | Lista todas as configurações |
| `git config --global --list` | Lista apenas as configurações globais |

## Criar e clonar repositórios

| Comando | Descrição |
| --- | --- |
| `git init` | Cria um novo repositório local na pasta atual |
| `git init nome-da-pasta` | Cria um repositório em uma nova pasta |
| `git clone <url>` | Clona um repositório remoto para a máquina local |
| `git clone <url> nome-da-pasta` | Clona para uma pasta com nome específico |

## Verificar o estado

| Comando | Descrição |
| --- | --- |
| `git status` | Mostra o estado dos arquivos (modificados, preparados e não rastreados) |
| `git status -s` | Mostra o estado de forma resumida |

## Adicionar arquivos (staging)

| Comando | Descrição |
| --- | --- |
| `git add arquivo.txt` | Adiciona um arquivo específico à área de preparação |
| `git add .` | Adiciona todas as alterações da pasta atual |
| `git add -A` | Adiciona todas as alterações do repositório |
| `git add *.txt` | Adiciona arquivos por padrão de nome |

## Commitar

| Comando                     | Descrição                                      |
| --------------------------- | ---------------------------------------------- |
| `git commit -m "mensagem"`  | Cria um commit com as alterações preparadas    |
| `git commit -am "mensagem"` | Adiciona arquivos já rastreados e faz o commit |
| `git commit --amend`        | Corrige o último commit (mensagem ou conteúdo) |

## Histórico e diferenças

| Comando | Descrição |
| --- | --- |
| `git log` | Mostra o histórico de commits |
| `git log --oneline` | Mostra o histórico resumido (uma linha por commit) |
| `git log --oneline --graph` | Mostra o histórico com gráfico de branches |
| `git show <hash>` | Mostra os detalhes de um commit |
| `git diff` | Mostra as alterações ainda não preparadas |
| `git diff --staged` | Mostra as alterações já preparadas |

## Branches (ramificações)

| Comando                | Descrição                                    |
| ---------------------- | -------------------------------------------- |
| `git branch`           | Lista as branches locais                     |
| `git branch nome`      | Cria uma nova branch                         |
| `git checkout nome`    | Troca para uma branch existente              |
| `git checkout -b nome` | Cria e troca para uma nova branch            |
| `git switch nome`      | Troca para uma branch (comando mais recente) |
| `git switch -c nome`   | Cria e troca para uma nova branch            |
| `git merge nome`       | Une a branch informada à branch atual        |
| `git branch -d nome`   | Remove uma branch já mesclada                |

## Repositório remoto

| Comando | Descrição |
| --- | --- |
| `git remote -v` | Lista os repositórios remotos configurados |
| `git remote add origin <url>` | Adiciona um repositório remoto chamado origin |
| `git push` | Envia os commits locais para o remoto |
| `git push -u origin main` | Envia e define o remoto/upstream da branch |
| `git pull` | Traz e mescla as alterações do remoto |
| `git fetch` | Baixa as alterações do remoto sem mesclar |

## Desfazer alterações

| Comando | Descrição |
| --- | --- |
| `git restore arquivo` | Desfaz alterações de um arquivo no diretório de trabalho |
| `git restore --staged arquivo` | Remove um arquivo da área de preparação |
| `git reset HEAD~1` | Desfaz o último commit mantendo as alterações |
| `git reset --hard HEAD` | Descarta todas as alterações não commitadas |

## Ignorar arquivos

O arquivo `.gitignore` lista arquivos e pastas que o Git deve ignorar.

```
# Exemplo de .gitignore
node_modules/
*.log
.env
```

## Ajuda

| Comando | Descrição |
| --- | --- |
| `git --version` | Mostra a versão instalada do Git |
| `git help <comando>` | Abre a documentação de um comando |
| `git <comando> --help` | Abre a documentação de um comando |

## Erros comuns

- **Rodar `git add .` sem revisar** o que está sendo preparado.
- **Confundir `git commit` (local) com `git push` (remoto)**.
- **Esquecer de configurar `user.name` e `user.email`** antes do primeiro commit.
- **Usar `git reset --hard` sem certeza** e perder alterações.
- **Fazer `push` sem `pull`** e receber o erro "rejected".
- **Achar que `git fetch` altera os arquivos** (só o `pull` integra).

## Casos de uso

| Situação | Comandos |
| --- | --- |
| Iniciar um projeto | `git init` + `git add .` + `git commit -m` |
| Baixar um projeto | `git clone <url>` |
| Criar uma feature | `git switch -c feature` |
| Publicar alterações | `git add .` + `git commit -m` + `git push` |
| Atualizar do remoto | `git pull` |
| Ver o histórico | `git log --oneline` |
