---
titulo: Monorepo e polyrepo
tipo: conceito
nivel: intermediario
categoria: Git
tags: [git, monorepo, polyrepo, arquitetura, sparse-checkout, subtree]
resumo: "Comparação entre monorepo e polyrepo, vantagens, desvantagens e as ferramentas do Git usadas em monorepos."
relacionados: ["sparse-checkout", "Clone parcial e shallow", "git subtree"]
fonte: https://git-scm.com/docs
---

# Monorepo e polyrepo

## O que é?

São duas formas de organizar o código em repositórios:

- **Monorepo**: **um único repositório** contém vários projetos/serviços/bibliotecas.
- **Polyrepo**: cada projeto tem seu **próprio repositório**.

A escolha afeta o fluxo de trabalho, o CI/CD e as ferramentas de Git usadas.

## Monorepo

```
monorepo/
├── apps/
│   ├── web/
│   └── mobile/
├── libs/
│   └── shared/
└── services/
    └── pagamentos/
```

**Vantagens**
- Mudanças atômicas entre projetos (um commit).
- Compartilhamento de código e padrões.
- Refatorações globais mais fáceis.

**Desvantagens**
- Repositório **grande** (clone lento, mais espaço).
- CI/CD precisa ser seletivo (rodar só o afetado).
- Exige disciplina e ferramentas.

## Polyrepo

```
projeto-web/       (repo)
projeto-mobile/    (repo)
lib-compartilhada/ (repo)
```

**Vantagens**
- Repositórios pequenos e independentes.
- Times autônomos e deploy separado.
- Permissões isoladas.

**Desvantagens**
- Mudanças entre projetos exigem vários PRs.
- Versões de dependências podem divergir.
- Mais trabalho de sincronização.

## Comparação

| Critério | Monorepo | Polyrepo |
| --- | --- | --- |
| Tamanho do repo | Grande | Pequeno |
| Mudança entre projetos | Atômica | Vários PRs |
| CI/CD | Seletivo | Simples por repo |
| Autonomia dos times | Menor | Maior |
| Ferramentas Git | Avançadas | Básicas |

## Ferramentas de Git para monorepo

| Ferramenta | Uso |
| --- | --- |
| `git sparse-checkout` | Ver só as pastas necessárias |
| Clone parcial/shallow | Clonar mais rápido |
| `git subtree` | Incorporar projetos externos |
| Git LFS | Arquivos grandes |
| `git maintenance` | Manter performance |

## Erros comuns

- **Adotar monorepo sem ferramentas**, tornando o clone/CI insuportável.
- **Achar que monorepo = uma branch para tudo sem cuidado**.
- **Espalhar dependências duplicadas** no polyrepo.
- **Não definir fronteiras** entre projetos no monorepo.

## Casos de uso

| Situação | Escolha |
| --- | --- |
| Vários serviços com código compartilhado | Monorepo |
| Times autônomos com deploys independentes | Polyrepo |
| Refatorações globais frequentes | Monorepo |
| Projetos open source independentes | Polyrepo |
| Biblioteca usada por vários apps | Polyrepo (ou monorepo) |
