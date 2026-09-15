---
titulo: GitHub Pages
tipo: conceito
nivel: intermediario
categoria: GitHub
tags: [github, pages, hospedagem, site, estatico, jekyll]
resumo: "Como publicar sites estáticos com GitHub Pages, fontes de publicação, domínio personalizado e limitações."
relacionados: ["GitHub Actions", "Gists", "Releases"]
fonte: https://docs.github.com/pt/pages
---

# GitHub Pages

## O que é?

**GitHub Pages** é um serviço de **hospedagem de sites estáticos** diretamente de um repositório GitHub. Ideal para documentação, portfólios e blogs.

## Fontes de publicação

| Fonte | Descrição |
| --- | --- |
| Branch `main` (raiz) | Publica a raiz da branch |
| Branch `main` + pasta `/docs` | Publica apenas a pasta `docs` |
| Branch `gh-pages` | Branch dedicada à publicação |
| GitHub Actions | Build customizado (recomendado) |

## Publicar (passo a passo)

1. Vá em **Settings → Pages**.
2. Em **Source**, escolha a branch/pasta ou **GitHub Actions**.
3. Salve e aguarde o build.
4. O site fica em `https://usuario.github.io/repositorio/`.

Para o site na raiz (`https://usuario.github.io`), crie um repositório chamado `usuario.github.io`.

## Site estático

O Pages serve apenas arquivos **estáticos** (HTML, CSS, JS, imagens). Para conteúdo dinâmico, é preciso um backend separado.

- Suporta **Jekyll** nativamente (processa Markdown).
- Com **Actions**, dá para usar geradores como Hugo, Next.js (export), Astro, etc.

## Domínio personalizado

```text
Settings → Pages → Custom domain
```

- Adicione um arquivo `CNAME` com o domínio.
- Configure o DNS (registro `CNAME` ou `A`).
- Ative **Enforce HTTPS**.

## Limitações

- Apenas conteúdo estático.
- Limite de tamanho e de build.
- Repositórios públicos (em planos gratuitos) para Pages.

## Erros comuns

- **Esperar backend/dinâmico** (não suporta).
- **Esquecer o `CNAME`** ao usar domínio próprio.
- **Publicar segredos** em site público.
- **Não configurar HTTPS**.
- **Confundir a pasta publicada** e ver uma página em branco.

## Casos de uso

| Situação | Uso |
| --- | --- |
| Documentação do projeto | Pages a partir de `/docs` |
| Portfólio pessoal | Repositório `usuario.github.io` |
| Blog estático | Jekyll/Hugo + Pages |
| Site de uma biblioteca | Pages + Actions |
| Demonstração de projeto | Pages |
