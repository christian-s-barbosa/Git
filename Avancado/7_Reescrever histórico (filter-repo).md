---
titulo: Reescrever histórico (filter-repo)
tipo: comando
nivel: avancado
categoria: Git
tags: [git, filter-repo, filter-branch, bfg, reescrever, segredos, historico]
resumo: "Como reescrever o histórico do Git com git filter-repo para remover segredos, arquivos grandes e renomear autores."
relacionados: ["git replace", "Internos a fundo (packfiles e gc)", "git reflog"]
fonte: https://git-scm.com/docs/git-filter-repo
---

# Reescrever histórico (filter-repo)

## O que é?

**Reescrever o histórico** significa alterar commits já existentes: remover **segredos**, apagar **arquivos grandes**, renomear autores, mover pastas, etc. Como o hash depende do conteúdo e do histórico, **todos os commits afetados ganham novos hashes**.

> É uma operação **destrutiva e de alto risco**. Sempre faça backup (um clone espelho) e combine com a equipe.

## Ferramentas

| Ferramenta | Situação |
| --- | --- |
| **git filter-repo** | Recomendada (rápida e segura) |
| `git filter-branch` | Legada (lenta, desencorajada) |
| **BFG Repo-Cleaner** | Alternativa popular para limpar arquivos grandes/segredos |

O `filter-repo` **não vem** com o Git; instale separadamente.

## Antes de começar

```bash
# faça um clone espelho de segurança
git clone --mirror <url> repositorio-backup.git
```

## Remover um arquivo/diretório do histórico

```bash
# remove um arquivo de todo o histórico
git filter-repo --path segredos.txt --invert-paths

# remove uma pasta
git filter-repo --path config/ --invert-paths
```

- `--path`: seleciona o caminho.
- `--invert-paths`: **remove** os caminhos selecionados.

## Substituir textos (ex.: segredos)

```bash
# substitui um token por ***REMOVED***
echo "TOKEN_SECRETO==>***REMOVED***" > substituicoes.txt
git filter-repo --replace-text substituicoes.txt
```

## Manter apenas um caminho

```bash
git filter-repo --path src/
```

## Renomear autores

```bash
git filter-repo --mailmap mailmap.txt
```

Exemplo de `mailmap.txt`:

```
Nome Correto <email@certo.com> <email@antigo.com>
```

## Depois de reescrever

1. Enviar o histórico reescrito:

```bash
git push --force --all
git push --force --tags
```

2. **Todos os colaboradores** precisam **re-clonar** (ou resetar) o repositório.
3. Trocar as credenciais/segredos que vazaram (eles existiram no histórico).
4. Se for no GitHub, pode ser necessário pedir a limpeza do cache/rede.

## Erros comuns

- **Não fazer backup** antes de reescrever.
- **Achar que o segredo some do GitHub** após o force push: ele pode continuar acessível por hash/cache.
- **Não avisar a equipe**, que fica com histórico divergente.
- **Usar `filter-branch`** em repositórios grandes (muito lento).
- **Esquecer de trocar os segredos vazados**.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Remover um segredo do histórico | `filter-repo --replace-text` |
| Apagar arquivo grande antigo | `filter-repo --path x --invert-paths` |
| Renomear autores | `filter-repo --mailmap` |
| Extrair só uma pasta | `filter-repo --path src/` |
| Limpar binários pesados | BFG Repo-Cleaner |
