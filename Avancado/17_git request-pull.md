---
titulo: git request-pull
tipo: comando
nivel: avancado
categoria: Git
tags: [git, request-pull, patch, email, contribuicao, pull]
resumo: "Como gerar uma solicitação de pull por e-mail com git request-pull, no fluxo de contribuição por e-mail."
relacionados: ["git am e format-patch", "GitHub na prática (Fork, Pull Request e Issues)", "Protocolos e hospedagem"]
fonte: https://git-scm.com/docs/git-request-pull
---

# git request-pull

## O que é?

O `git request-pull` gera um **texto de solicitação de pull** para ser enviado por e-mail. Ele descreve um intervalo de commits e o endereço do repositório, permitindo que outra pessoa aplique o trabalho.

É parte do fluxo de contribuição por **e-mail**, tradicional em projetos como o **kernel do Linux**, antes dos pull requests das plataformas.

## Sintaxe

```
git request-pull <inicio> <url> [<fim>]
```

- `<inicio>`: commit/branch onde o trabalho começa (base).
- `<url>`: repositório que contém os commits.
- `<fim>`: branch/commit final (padrão: HEAD).

## Exemplo

```bash
git request-pull origin/main https://github.com/usuario/projeto.git feature/login
```

Saída (resumida):

```
The following changes since commit a1b2c3d:

  Última alteração da main (2026-09-01)

are available in the Git repository at:

  https://github.com/usuario/projeto.git feature/login

for you to fetch changes up to d4e5f6a:

  Adiciona tela de login (2026-09-10)

------------------------------------------------
Maria Silva (2):
      Adiciona formulário
      Valida credenciais

 src/login.js | 40 +++++++++++++++++++++
 1 file changed, 40 insertions(+)
```

## Como usar

1. Envie os commits para um repositório acessível (ex.: seu fork).
2. Gere o texto com `git request-pull`.
3. Envie por e-mail para o mantenedor.
4. O mantenedor busca (`fetch`) e integra.

## request-pull x pull request

| Característica | git request-pull | Pull request (GitHub) |
| --- | --- | --- |
| Canal | E-mail | Plataforma web |
| Revisão | Na lista de e-mails | Interface do PR |
| Uso | Projetos como o kernel | Maioria dos projetos |
| Automação | Manual | Integrada |

## Erros comuns

- **URL inacessível** para o mantenedor (o texto não serve de nada).
- **Base errada** no `<inicio>`, listando commits a mais ou a menos.
- **Não enviar os commits** ao repositório antes de gerar o pedido.
- **Confundir com `format-patch`**: aqui não se anexam patches, só a referência.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Pedir pull por e-mail | `git request-pull base <url> branch` |
| Contribuir com projeto por e-mail | request-pull + e-mail |
| Publicar um intervalo de commits | request-pull |
