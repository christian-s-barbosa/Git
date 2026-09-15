---
titulo: Internos a fundo (packfiles e gc)
tipo: conceito
nivel: avancado
categoria: Git
tags: [git, packfile, gc, delta, commit-graph, multi-pack-index, objetos]
resumo: "Como o Git armazena objetos em packfiles, compressão delta e estruturas de aceleração como commit-graph e multi-pack-index."
relacionados: ["Como o Git funciona por dentro", "Manutenção do repositório", "git maintenance"]
fonte: https://git-scm.com/book/pt-br/v2
---

# Internos a fundo (packfiles e gc)

## O que é?

Este tópico aprofunda **como o Git armazena os objetos por baixo dos panos**: objetos soltos, packfiles, compressão delta e as estruturas que aceleram a leitura. Entender isso ajuda a **otimizar repositórios grandes**.

## Objetos soltos (loose objects)

- Cada objeto novo é gravado individualmente e comprimido com zlib em `.git/objects/`.
- São fáceis de criar, mas **ineficientes em quantidade**.

```
.git/objects/3f/2a1b9c8d...   (objeto solto, comprimido)
```

## Packfiles

- O `git gc`/`git repack` agrupa muitos objetos em **packfiles**.
- Um packfile é composto por:
  - `.pack`: os objetos comprimidos.
  - `.idx`: um índice para localizar objetos rapidamente.

```
.git/objects/pack/pack-xxxx.pack
.git/objects/pack/pack-xxxx.idx
```

## Compressão delta

Dentro de um packfile, o Git guarda objetos **similares** como **deltas** (diferenças) de um objeto base, em vez do conteúdo completo. Isso reduz muito o tamanho.

- `delta chain`: uma sequência de deltas até o objeto base.
- Cadeias muito longas deixam a leitura lenta; o `gc` as reestrutura.

## Estruturas de aceleração

| Estrutura | Função |
| --- | --- |
| `commit-graph` | Acelera a navegação do histórico (`log`, `merge-base`) |
| `multi-pack-index` (MIDX) | Índice único sobre vários packfiles |
| `bitmap` | Acelera operações como `fetch`/`clone` |

O `git maintenance` cria e mantém essas estruturas automaticamente.

## Inspecionando

```bash
# quantidade e tamanho de objetos (loose e packed)
git count-objects -vH

# estatísticas de um packfile
git verify-pack -v .git/objects/pack/pack-xxxx.idx

# lista objetos de um commit
git ls-tree -r HEAD

# tipo e conteúdo de um objeto
git cat-file -p <hash>
```

## Quando se preocupar

- Repositórios com **milhares de commits** e arquivos grandes.
- `git log`/`git status` lentos.
- Clones e fetches demorados.
- Uso intenso em **monorepos**.

Soluções: `git maintenance`, `commit-graph`, `multi-pack-index`, `sparse-checkout` e clone parcial.

## Erros comuns

- **Apagar packfiles manualmente**: corrompe o repositório.
- **Rodar `git gc --aggressive`** sem necessidade (lento e pouco ganho).
- **Ignorar objetos `dangling`** que poderiam ser recuperados pelo reflog.
- **Confundir tamanho do working directory com o do `.git`**.

## Casos de uso

| Situação | Comando/estrutura |
| --- | --- |
| Ver tamanho real do repositório | `git count-objects -vH` |
| Acelerar o histórico | `git maintenance run --task=commit-graph` |
| Otimizar vários packfiles | `git repack` / `multi-pack-index` |
| Investigar um packfile | `git verify-pack -v ...` |
