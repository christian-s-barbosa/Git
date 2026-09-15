---
titulo: Clone parcial e shallow
tipo: comando
nivel: intermediario
categoria: Git
tags: [git, clone, shallow, partial-clone, depth, filter, monorepo]
resumo: "Como clonar de forma mais rápida e leve com shallow, clone parcial e single-branch, e como voltar ao completo."
relacionados: ["sparse-checkout", "Monorepo e polyrepo", "git bisect"]
fonte: https://git-scm.com/docs/git-clone
---

# Clone parcial e shallow

## O que é?

Por padrão, o `git clone` baixa **todo o histórico** e **todos os arquivos**. Em repositórios muito grandes, isso pode ser lento e ocupar muito espaço. O **clone shallow** e o **clone parcial** permitem baixar apenas o necessário.

| Tipo | O que limita |
| --- | --- |
| **Shallow** | Profundidade do histórico (número de commits) |
| **Parcial** | Conteúdo (blobs/trees) baixado sob demanda |
| **Single-branch** | Baixa apenas uma branch |

## Clone shallow

```bash
# baixa apenas o último commit
git clone --depth 1 <url>

# baixa os últimos 50 commits
git clone --depth 50 <url>

# baixa a partir de uma data
git clone --shallow-since="2026-01-01" <url>
```

- Muito mais rápido e leve.
- Não traz o histórico completo (limita `log`, `blame`, `bisect`).

## Clone parcial

```bash
# baixa commits e trees, mas os arquivos (blobs) sob demanda
git clone --filter=blob:none <url>

# baixa apenas as trees mais recentes
git clone --filter=tree:0 <url>

# baixa blobs maiores que 1 MB apenas quando necessário
git clone --filter=blob:limit=1m <url>
```

- Ideal para **monorepos** e integração com `sparse-checkout`.
- O conteúdo é baixado quando você acessa o arquivo.

## Single-branch

```bash
git clone --single-branch --branch main <url>
```

Baixa apenas a branch informada, e não todas.

## Voltar a ter o histórico completo

```bash
# transforma um clone shallow em completo
git fetch --unshallow
```

## Combinando com sparse-checkout

```bash
git clone --filter=blob:none --sparse <url>
cd repositorio
git sparse-checkout set app libs
```

## Limitações

- `git log`, `git blame` e `git bisect` podem não ter todo o histórico.
- `git describe` pode não encontrar tags antigas.
- Alguns comandos exigem baixar mais dados sob demanda.

## Erros comuns

- **Usar `--depth 1` e depois precisar do histórico** (é preciso `--unshallow`).
- **Achar que o clone parcial economiza espaço permanentemente**: os blobs baixados ficam.
- **Fazer bisect em clone shallow**, que não tem os commits necessários.
- **Esquecer que o `--single-branch`** não traz as outras branches.

## Casos de uso

| Situação | Comando |
| --- | --- |
| CI/CD rápido | `git clone --depth 1 <url>` |
| Monorepo gigante | `git clone --filter=blob:none <url>` |
| Só uma branch interessa | `git clone --single-branch --branch x <url>` |
| Trabalhar em parte do repo | clone parcial + `sparse-checkout` |
| Recuperar histórico completo | `git fetch --unshallow` |
