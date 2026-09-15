---
titulo: Interoperabilidade (git svn e git p4)
tipo: comando
nivel: avancado
categoria: Git
tags: [git, svn, p4, perforce, interoperabilidade, migracao]
resumo: "Como usar o Git como cliente de SVN e Perforce com git svn e git p4, e suas limitações."
relacionados: ["Protocolos e hospedagem", "git subtree", "Reescrever histórico (filter-repo)"]
fonte: https://git-scm.com/docs/git-svn
---

# Interoperabilidade (git svn e git p4)

## O que é?

O Git pode atuar como **cliente** de outros sistemas de controle de versão, permitindo usar os comandos do Git enquanto o repositório "oficial" continua em **Subversion (SVN)** ou **Perforce (P4)**.

## git svn

Permite clonar, atualizar e enviar alterações para um repositório SVN usando o Git.

```bash
# clona um repositório SVN
git svn clone <url-svn> projeto

# baixa as novidades do SVN
git svn fetch

# atualiza a branch local com o SVN (rebase)
git svn rebase

# envia commits locais para o SVN
git svn dcommit
```

- `dcommit`: converte seus commits Git em commits SVN.
- `rebase`: aplica os commits do SVN mantendo o histórico linear.

## git p4

Permite trabalhar com **Perforce** usando o Git.

```bash
# clona um depot do Perforce
git p4 clone //depot/projeto@all

# baixa as novidades
git p4 sync

# envia as alterações para o Perforce
git p4 submit
```

## Limitações

- O histórico do SVN/P4 é convertido, mas nem tudo se traduz perfeitamente.
- Operações como `merge`, `rebase` complexo e branches podem ter comportamento limitado.
- **Não** é a forma ideal de usar o Git: é uma ponte.
- Migrações definitivas devem ser planejadas (e podem usar `filter-repo` depois).

## Erros comuns

- **Misturar branches Git com o SVN** sem entender o mapeamento.
- **Fazer merges complexos** e depois `dcommit`, gerando confusão no SVN.
- **Achar que é uma migração**: é interoperabilidade, o SVN/P4 continua sendo a fonte.
- **Esquecer de `git svn rebase`** antes de enviar, criando divergência.

## Casos de uso

| Situação | Ferramenta |
| --- | --- |
| Empresa com SVN querendo usar Git localmente | `git svn` |
| Time em Perforce usando Git | `git p4` |
| Migração gradual de SVN para Git | `git svn` |
| Contribuir com projeto legado | `git svn` / `git p4` |
