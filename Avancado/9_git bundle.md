---
titulo: git bundle
tipo: comando
nivel: avancado
categoria: Git
tags: [git, bundle, offline, transferencia, backup]
resumo: "Como empacotar um repositório em um único arquivo com git bundle para transferência offline e backup."
relacionados: ["git grep e git archive", "Refspecs", "Protocolos e hospedagem"]
fonte: https://git-scm.com/docs/git-bundle
---

# git bundle

## O que é?

O `git bundle` **empacota** um repositório (ou parte dele) em **um único arquivo**, que pode ser transferido como qualquer arquivo comum. É útil para **transferir commits sem rede** (pendrive, e-mail, servidor isolado) e para backups.

## Criar um bundle

```bash
# empacota todas as refs (histórico completo)
git bundle create repositorio.bundle --all

# empacota apenas uma branch
git bundle create main.bundle main

# empacota um intervalo (ex.: commits que faltam no outro lado)
git bundle create incremento.bundle main~5..main
```

## Verificar um bundle

```bash
git bundle verify repositorio.bundle
```

Confirma se o arquivo é válido e se as dependências (commits base) existem.

## Clonar a partir de um bundle

```bash
git clone repositorio.bundle novo-repositorio
```

## Fazer fetch/pull de um bundle

```bash
# trata o bundle como um "remoto"
git remote add bundle /caminho/para/repositorio.bundle
git fetch bundle
git merge bundle/main
```

## Exemplo: transferir commits para uma máquina offline

```bash
# máquina A: gera o bundle com os commits novos
git bundle create novos.bundle main~10..main

# copia o arquivo para a máquina B (pendrive)
# máquina B: aplica
git fetch novos.bundle main:minha-branch
```

## Comandos

| Comando | Descrição |
| --- | --- |
| `git bundle create arquivo.bundle --all` | Cria um bundle com tudo |
| `git bundle create x.bundle main` | Bundle de uma branch |
| `git bundle create x.bundle a..b` | Bundle de um intervalo |
| `git bundle verify arquivo.bundle` | Verifica o bundle |
| `git clone arquivo.bundle` | Clona a partir do bundle |
| `git fetch arquivo.bundle <ref>` | Busca refs do bundle |

## Erros comuns

- **Gerar um bundle sem incluir a base necessária**, fazendo o `verify`/aplicação falhar.
- **Achar que o bundle atualiza sozinho**: é um arquivo estático.
- **Usar bundle para colaboração contínua**: para isso, um remoto normal é melhor.
- **Esquecer de incluir todas as refs** ao querer um backup completo (`--all`).

## Casos de uso

| Situação | Comando |
| --- | --- |
| Levar commits para ambiente sem rede | `git bundle create` |
| Backup completo do repositório | `git bundle create --all` |
| Transferir via pendrive | bundle + `git fetch` |
| Entregar um recorte de commits | `git bundle create a..b` |
