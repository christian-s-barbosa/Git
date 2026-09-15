---
titulo: Como o Git funciona por dentro
tipo: conceito
nivel: intermediario
categoria: Git
tags: [git, internos, objetos, blob, tree, commit, packfile, cat-file, hash]
resumo: "O modelo de objetos do Git (blob, tree, commit, tag), endereçamento por hash, estrutura do .git e packfiles."
relacionados: ["Internos a fundo (packfiles e gc)", "Manutenção do repositório", "Git commit"]
fonte: https://git-scm.com/book/pt-br/v2
---

# Como o Git funciona por dentro

## O que é?

Entender o modelo interno do Git ajuda a compreender por que ele é rápido, seguro e distribuído. O Git é, no fundo, um **banco de dados de objetos** endereçados por conteúdo.

## O modelo de objetos

O Git armazena quatro tipos de objetos:

| Objeto | O que guarda |
| --- | --- |
| **blob** | O conteúdo de um arquivo (sem nome) |
| **tree** | Uma pasta: lista de nomes, permissões e blobs/subtrees |
| **commit** | Aponta para uma tree, autor, data, mensagem e o(s) pai(s) |
| **tag** | Uma tag anotada apontando para um objeto |

## Endereçamento por conteúdo

- Cada objeto recebe um **hash SHA-1** calculado a partir do seu conteúdo.
- O mesmo conteúdo gera **sempre o mesmo hash**.
- Os objetos ficam em `.git/objects/`.

```
.git/objects/3f/2a1b9c...   <- objeto (comprimido)
```

- Isso garante **integridade**: se o conteúdo mudar, o hash muda.
- Como o commit aponta para a tree e a tree para os blobs, **qualquer alteração** propaga um novo hash.

## Como um commit é montado

```
commit -> tree (raiz do projeto)
             ├── blob  (arquivo A)
             ├── blob  (arquivo B)
             └── tree  (subpasta)
                    └── blob (arquivo C)
```

- O commit guarda **um snapshot completo** (via tree), não apenas o diff.
- Para economizar espaço, o Git usa **delta compression** dentro dos packfiles.

## A pasta .git

| Item | Função |
| --- | --- |
| `objects/` | Todos os objetos (blobs, trees, commits, tags) |
| `refs/` | Ponteiros para commits (branches, tags) |
| `HEAD` | Indica a branch/commit atual |
| `index` | A área de preparação (staging) |
| `config` | Configurações do repositório |
| `logs/` | O reflog |

## Explorando os objetos

```bash
# tipo e conteúdo de um objeto
git cat-file -t <hash>      # mostra o tipo (blob, tree, commit)
git cat-file -p <hash>      # mostra o conteúdo

# criar um objeto a partir de um texto
echo "Olá" | git hash-object -w --stdin

# listar a tree de um commit
git ls-tree HEAD
git ls-tree -r HEAD         # recursivo

# ver a tree de uma pasta
git ls-tree HEAD src/
```

Exemplo:

```bash
git cat-file -p HEAD
# tree 8c1d4e2...
# parent a7b3f10...
# author Seu Nome <email> 1710000000 -0300
# committer Seu Nome <email> 1710000000 -0300
#
# Mensagem do commit
```

## Packfiles

- Objetos "soltos" (loose) são comprimidos individualmente.
- O `git gc` agrupa vários objetos em **packfiles** (`.pack` + `.idx`), com compressão delta.
- É por isso que o repositório é compacto mesmo com muito histórico.

## Erros comuns

- **Achar que o Git guarda apenas diffs**: ele guarda **snapshots** (e usa deltas só internamente).
- **Mexer manualmente em `.git/objects`** e corromper o repositório.
- **Confundir hash com número sequencial**: o hash depende do conteúdo.
- **Apagar a pasta `.git`** achando que só perde o histórico (perde tudo).

## Casos de uso

| Objetivo | Comando |
| --- | --- |
| Ver o tipo de um objeto | `git cat-file -t <hash>` |
| Ver o conteúdo de um commit | `git cat-file -p <hash>` |
| Listar arquivos de um commit | `git ls-tree -r HEAD` |
| Descobrir o hash de um texto | `git hash-object --stdin` |
| Entender o tamanho do repositório | `git count-objects -vH` |
