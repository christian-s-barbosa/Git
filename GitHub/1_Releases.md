---
titulo: Releases
tipo: conceito
nivel: intermediario
categoria: GitHub
tags: [github, release, versao, tag, changelog, gh-cli]
resumo: "O que são releases no GitHub, a diferença para tags, como criar (web e gh cli), notas de versão e pre-releases."
relacionados: ["git tag", "Gists", "GitHub Actions"]
fonte: https://docs.github.com/pt/repositories/releasing-projects-on-github
---

# Releases

## O que é?

Uma **release** é uma **versão publicada** de um projeto no GitHub. Ela é criada a partir de uma **tag** e permite anexar **notas de versão** (changelog) e **arquivos** (binários, pacotes).

## Release x tag

| Característica | Tag | Release |
| --- | --- | --- |
| Onde existe | No Git | No GitHub |
| O que é | Marcador de commit | Publicação com notas/arquivos |
| Anexar arquivos | Não | Sim |
| Notas de versão | Não | Sim |

Toda release está ligada a uma tag, mas nem toda tag vira release.

## Criar uma release (web)

1. No repositório, vá em **Releases → Draft a new release**.
2. Escolha ou crie uma **tag** (ex.: `v1.0.0`).
3. Escreva o **título** e as **notas**.
4. Anexe **arquivos** (opcional).
5. Marque como **pre-release** se for o caso.
6. Clique em **Publish release**.

## Criar via GitHub CLI

```bash
# cria uma tag e uma release
gh release create v1.0.0 --title "v1.0.0" --notes "Primeira versão"

# com notas geradas automaticamente
gh release create v1.0.1 --generate-notes

# anexando arquivos
gh release create v1.0.0 ./dist/app.zip

# pré-release
gh release create v1.0.0-rc1 --prerelease
```

## Latest e pré-release

- **Latest**: a release mais recente considerada estável.
- **Pre-release**: versão de teste (ex.: `-rc1`, `-beta`), não marcada como latest.
- É possível marcar uma release antiga como "latest" manualmente.

## Boas práticas

- Use **versionamento semântico** (`v1.2.3`).
- Escreva notas claras (o que mudou, correções, breaking changes).
- Anexe **binários** e checksums quando fizer sentido.
- Marque versões instáveis como **pre-release**.

## Erros comuns

- **Criar a release na tag errada**.
- **Deixar as notas vazias**, dificultando o entendimento.
- **Confundir tag com release**.
- **Anexar arquivos grandes** ao repositório em vez da release (use a release).

## Casos de uso

| Situação | Ação |
| --- | --- |
| Publicar uma versão | Release com tag `vX.Y.Z` |
| Distribuir binários | Anexar arquivos à release |
| Divulgar mudanças | Notas de versão (changelog) |
| Teste beta | Pre-release |
| Automatizar | `gh release create` |
