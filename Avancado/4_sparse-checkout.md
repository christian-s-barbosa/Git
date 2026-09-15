---
titulo: sparse-checkout
tipo: comando
nivel: avancado
categoria: Git
tags: [git, sparse-checkout, monorepo, parcial, cone]
resumo: "Como trabalhar com apenas parte dos arquivos do repositório usando sparse-checkout, especialmente em monorepos."
relacionados: ["Clone parcial e shallow", "Monorepo e polyrepo", "git update-index (assume-unchanged e skip-worktree)"]
fonte: https://git-scm.com/docs/git-sparse-checkout
---

# sparse-checkout

## O que é?

O `sparse-checkout` permite ter **apenas parte dos arquivos** do repositório no seu diretório de trabalho. Em vez de baixar tudo (comum em **monorepos**), você escolhe as pastas que quer ver.

Os arquivos fora do escopo **continuam no histórico** e são baixados sob demanda, mas não aparecem no seu disco.

## Modo cone (recomendado)

O **cone mode** trabalha com **pastas**, é mais rápido e simples.

```bash
# inicializa no modo cone
git sparse-checkout init --cone

# define as pastas que você quer
git sparse-checkout set app libs/shared

# lista o que está incluído
git sparse-checkout list

# desativa o sparse-checkout (volta a ver tudo)
git sparse-checkout disable
```

## Exemplo

```bash
# clona de forma parcial e esparsa
git clone --filter=blob:none --sparse https://github.com/empresa/monorepo.git
cd monorepo

# seleciona apenas o serviço em que vai trabalhar
git sparse-checkout set services/pagamentos
```

Agora só os arquivos de `services/pagamentos` (e arquivos da raiz) aparecem.

## Adicionar e remover pastas

```bash
# adiciona uma pasta
git sparse-checkout add services/usuarios

# redefine a lista
git sparse-checkout set services/pagamentos services/usuarios

# reaplica as regras
git sparse-checkout reapply
```

## Modo não-cone (padrão por arquivo)

Permite padrões como no `.gitignore`:

```bash
git sparse-checkout init
git sparse-checkout set --no-cone '/*' '!/docs/'
```

## Comandos

| Comando | Descrição |
| --- | --- |
| `git sparse-checkout init --cone` | Inicializa no modo cone |
| `git sparse-checkout set <dirs>` | Define as pastas incluídas |
| `git sparse-checkout add <dir>` | Adiciona uma pasta |
| `git sparse-checkout list` | Lista as pastas incluídas |
| `git sparse-checkout disable` | Desativa e volta a ver tudo |
| `git sparse-checkout reapply` | Reaplica as regras |

## Erros comuns

- **Usar `--no-cone` sem necessidade**: o modo cone é mais rápido e previsível.
- **Esperar que os arquivos excluídos não existam**: eles continuam no repositório.
- **Editar arquivos fora do sparse-checkout** e estranhar conflitos.
- **Confundir sparse-checkout com clone parcial**: um limita os arquivos no disco, o outro limita o que é baixado.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Trabalhar em um serviço de um monorepo | `sparse-checkout set services/x` |
| Reduzir uso de disco | `sparse-checkout set` |
| Clonar monorepo gigante rapidamente | `clone --filter=blob:none --sparse` |
| Voltar a ver todos os arquivos | `sparse-checkout disable` |
