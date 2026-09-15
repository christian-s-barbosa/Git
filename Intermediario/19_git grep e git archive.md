---
titulo: git grep e git archive
tipo: comando
nivel: intermediario
categoria: Git
tags: [git, grep, archive, busca, exportar, snapshot]
resumo: "Como buscar texto nos arquivos rastreados com git grep e exportar snapshots do projeto com git archive."
relacionados: ["Inspeção do histórico", "Releases", ".gitattributes"]
fonte: https://git-scm.com/docs/git-grep
---

# git grep e git archive

## O que é?

- **`git grep`**: busca por texto **dentro dos arquivos rastreados** (working directory, índice ou um commit).
- **`git archive`**: **exporta** um snapshot do repositório (ou parte dele) em um arquivo compactado, sem o histórico.

## git grep

Busca muito mais rápida que ferramentas genéricas em repositórios Git, pois considera apenas arquivos versionados.

```bash
# busca por "funcao" nos arquivos rastreados
git grep "funcao"

# mostra o número da linha
git grep -n "funcao"

# ignora maiúsculas/minúsculas
git grep -i "funcao"

# busca por palavra inteira
git grep -w "total"

# lista apenas os nomes dos arquivos
git grep -l "funcao"

# conta ocorrências
git grep -c "funcao"
```

### Buscar em commits e branches

```bash
# busca em um commit específico
git grep "funcao" HEAD~5

# busca em uma tag
git grep "funcao" v1.0.0

# busca em várias branches
git grep "funcao" main feature
```

### Combinar padrões

```bash
git grep -e "login" --and -e "senha"
git grep "TODO" -- "*.js"
```

## git archive

Cria um arquivo (zip, tar) com o conteúdo de um commit/tag, **sem a pasta `.git`**.

```bash
# exporta o HEAD em zip
git archive --format=zip -o projeto.zip HEAD

# exporta em tar.gz
git archive --format=tar.gz -o projeto.tar.gz main

# exporta uma tag
git archive -o v1.0.0.zip v1.0.0

# adiciona um prefixo de pasta
git archive --prefix=projeto-1.0/ -o projeto.zip v1.0.0

# exporta apenas uma subpasta
git archive HEAD src/ -o src.zip
```

- Útil para gerar **releases** e pacotes de distribuição.
- O `.gitattributes` pode excluir arquivos com `export-ignore`.

## Comandos

| Comando | Descrição |
| --- | --- |
| `git grep "texto"` | Busca nos arquivos rastreados |
| `git grep -n "texto"` | Mostra o número da linha |
| `git grep -l "texto"` | Lista só os arquivos |
| `git grep "texto" <commit>` | Busca em um commit/tag/branch |
| `git archive -o arq.zip HEAD` | Exporta o snapshot |
| `git archive --prefix=dir/ ...` | Exporta com prefixo |
| `git archive HEAD src/ ...` | Exporta uma subpasta |

## Erros comuns

- **Usar `grep` do sistema em vez de `git grep`** e perder velocidade/escopo.
- **Achar que `git grep` busca em arquivos ignorados**: ele busca só nos rastreados.
- **Esperar que `git archive` inclua o histórico**: ele gera apenas um snapshot.
- **Esquecer que `export-ignore`** pode excluir arquivos do archive.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Encontrar onde uma função é usada | `git grep -n "funcao"` |
| Ver quando um TODO entrou | `git grep "TODO" <commit>` |
| Gerar pacote de release | `git archive --prefix=app/ -o app.zip v1.0.0` |
| Exportar só o código-fonte | `git archive HEAD src/ -o src.zip` |
