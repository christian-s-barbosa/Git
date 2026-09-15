---
titulo: git subtree
tipo: comando
nivel: avancado
categoria: Git
tags: [git, subtree, submodule, monorepo, dependencias]
resumo: "Como incorporar um repositório externo no histórico com git subtree, comparado ao submodule, e seus comandos."
relacionados: ["git submodules", "Monorepo e polyrepo", "git am e format-patch"]
fonte: https://git-scm.com/docs/git-subtree
---

# git subtree

## O que é?

O `git subtree` permite **incorporar um repositório dentro de outro**, mas de forma diferente do submodule: o código do projeto externo é **copiado para o histórico** do repositório principal.

Enquanto o submodule guarda um **ponteiro** para outro repositório, o subtree **faz parte** do histórico principal.

## subtree x submodule

| Característica | Submodule | Subtree |
| --- | --- | --- |
| Onde fica o código | Repositório separado | Dentro do histórico |
| Clonar já funciona? | Precisa de `--recurse-submodules` | Sim, é transparente |
| Histórico | Separado | Incorporado |
| Atualizar | `submodule update` | `subtree pull` |
| Complexidade | Média | Maior nos comandos |
| Contribuir de volta | Fácil | Requer `subtree push`/`split` |

## Adicionar um subtree

```bash
git subtree add --prefix=libs/biblioteca https://github.com/usuario/biblioteca.git main --squash
```

- `--prefix`: pasta de destino.
- `--squash`: junta o histórico do projeto externo em um único commit.

## Atualizar (puxar mudanças)

```bash
git subtree pull --prefix=libs/biblioteca https://github.com/usuario/biblioteca.git main --squash
```

## Enviar mudanças de volta

```bash
git subtree push --prefix=libs/biblioteca https://github.com/usuario/biblioteca.git main
```

## Extrair o subtree como repositório

```bash
# gera um histórico separado do subtree
git subtree split --prefix=libs/biblioteca -b biblioteca-standalone
```

## Comandos

| Comando | Descrição |
| --- | --- |
| `git subtree add --prefix=<dir> <url> <branch>` | Adiciona um subtree |
| `git subtree pull --prefix=<dir> <url> <branch>` | Atualiza o subtree |
| `git subtree push --prefix=<dir> <url> <branch>` | Envia mudanças |
| `git subtree split --prefix=<dir>` | Separa o subtree em uma branch |
| `git subtree merge --prefix=<dir> <ref>` | Mescla uma ref no subtree |

## Erros comuns

- **Confundir com submodule** e esperar um ponteiro.
- **Esquecer `--squash`**, trazendo todo o histórico do projeto externo.
- **Mover/renomear a pasta do subtree** sem ajustar os comandos.
- **Fazer push sem permissão** no repositório externo.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Usar uma lib externa sem complicar o clone | `subtree add` |
| Manter a lib atualizada | `subtree pull` |
| Contribuir de volta para a lib | `subtree push` |
| Extrair um projeto de um monorepo | `subtree split` |
