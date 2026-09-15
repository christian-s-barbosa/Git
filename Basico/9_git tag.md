---
titulo: git tag
tipo: comando
nivel: basico
categoria: Git
tags: [git, tag, versao, release, anotada, leve]
resumo: "O que são tags, diferença entre leve e anotada, como criar, listar, enviar e remover tags, e versionamento semântico."
relacionados: ["Releases", "Git commit", "Branches (Ramificações)"]
fonte: https://git-scm.com/docs/git-tag
---

# git tag

## O que é?

Uma **tag** é um **marcador fixo** que aponta para um commit específico. Diferente de uma branch, ela **não se move**: serve para marcar pontos importantes no histórico, como o lançamento de uma versão.

Exemplo: marcar o commit que corresponde à versão `v1.0.0`.

## Para que serve?

- Marcar **versões e releases** do projeto.
- Identificar pontos estáveis no histórico.
- Facilitar o download de uma versão específica.
- Servir de referência para documentação e changelogs.

## Tipos de tag

| Tipo | Descrição | Guarda informações extras? |
| --- | --- | --- |
| **Leve (lightweight)** | Apenas um ponteiro para o commit | Não |
| **Anotada (annotated)** | Objeto completo com autor, data e mensagem | Sim |

Recomenda-se usar **tags anotadas** para releases.

## Criar tags

```bash
# tag leve
git tag v1.0.0

# tag anotada (recomendada)
git tag -a v1.0.0 -m "Versão 1.0.0"

# marcar um commit específico
git tag -a v0.9.0 <hash> -m "Versão 0.9.0"
```

## Listar e visualizar

```bash
git tag                    # lista todas as tags
git tag -l "v1.*"          # lista tags por padrão
git show v1.0.0            # mostra os detalhes da tag
git tag -n                 # lista com as mensagens
```

## Enviar tags para o remoto

Por padrão, o `git push` **não envia** tags. É preciso enviá-las separadamente:

```bash
# envia uma tag específica
git push origin v1.0.0

# envia todas as tags
git push origin --tags
```

## Trocar de versão

```bash
# ver o projeto no estado da tag (modo destacado)
git checkout v1.0.0

# voltar para a branch principal
git checkout main
```

## Remover tags

```bash
# remove a tag localmente
git tag -d v1.0.0

# remove a tag no remoto
git push origin --delete v1.0.0
```

## Comandos

| Comando | Descrição |
| --- | --- |
| `git tag` | Lista as tags |
| `git tag v1.0.0` | Cria uma tag leve |
| `git tag -a v1.0.0 -m "msg"` | Cria uma tag anotada |
| `git show v1.0.0` | Mostra os detalhes da tag |
| `git push origin v1.0.0` | Envia uma tag ao remoto |
| `git push origin --tags` | Envia todas as tags |
| `git tag -d v1.0.0` | Remove a tag local |
| `git push origin --delete v1.0.0` | Remove a tag remota |

## Boas práticas

- Use **versionamento semântico** (SemVer): `MAJOR.MINOR.PATCH`, como `v1.2.3`.
  - **MAJOR**: mudanças incompatíveis.
  - **MINOR**: novas funcionalidades compatíveis.
  - **PATCH**: correções compatíveis.
- Prefira tags **anotadas** para releases.
- Nunca mova ou reutilize uma tag de versão já publicada.

## Erros comuns

- **Achar que `git push` envia tags**: é preciso `git push --tags` ou enviar a tag.
- **Mover ou reutilizar uma tag** já publicada.
- **Criar tag leve** para releases (o ideal é a anotada).
- **Esquecer de remover a tag remota** ao deletar apenas a local.
- **Nomear versões de forma inconsistente**.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Marcar uma versão | `git tag -a v1.0.0 -m "msg"` |
| Listar versões | `git tag` |
| Enviar uma tag | `git push origin v1.0.0` |
| Enviar todas as tags | `git push origin --tags` |
| Voltar ao estado de uma versão | `git checkout v1.0.0` |
