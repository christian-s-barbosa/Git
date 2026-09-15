---
titulo: Fluxos de trabalho
tipo: conceito
nivel: intermediario
categoria: Git
tags: [git, git-flow, github-flow, trunk-based, fluxo, workflow, branches]
resumo: "Comparação entre Git Flow, GitHub Flow e trunk-based development e como escolher o fluxo adequado."
relacionados: ["Branches (Ramificações)", "Monorepo e polyrepo", "Git em CI-CD"]
fonte: https://git-scm.com/book/pt-br/v2
---

# Fluxos de trabalho

## O que é?

Um **fluxo de trabalho (workflow)** é um **conjunto de regras** que define como a equipe usa branches, commits e merges no dia a dia. Ele organiza quem trabalha onde, como as funcionalidades entram na versão principal e como são lançadas as releases.

Não existe um fluxo "certo": o melhor depende do tamanho da equipe, da frequência de entregas e do processo de revisão.

## Git Flow

Modelo mais estruturado, com **várias branches de longa duração**.

| Branch | Função |
| --- | --- |
| `main` | Código em produção (estável) |
| `develop` | Integração do próximo release |
| `feature/*` | Novas funcionalidades |
| `release/*` | Preparação de uma versão |
| `hotfix/*` | Correções urgentes em produção |

Fluxo:

```
feature/* --> develop --> release/* --> main
                                  hotfix/* --> main e develop
```

- Bom para projetos com **releases agendadas** e equipes maiores.
- Pode ser **complexo** e pesado para entregas contínuas.

## GitHub Flow

Modelo simples, baseado em **branch + pull request**.

1. Crie uma branch a partir da `main`.
2. Faça commits.
3. Abra um **pull request**.
4. Revise e discuta.
5. Faça **merge** na `main`.
6. Implante (deploy).

- A `main` está sempre pronta para produção.
- Ideal para **entrega contínua** e equipes pequenas/médias.

## Trunk-based Development

Todos integram na **trunk** (branch principal) com **muita frequência** (ao menos diariamente).

- Branches são **curtas** (horas ou poucos dias) ou nem existem.
- Usa **feature flags** para esconder código incompleto.
- Exige testes automatizados e CI forte.
- Ideal para equipes maduras com **deploy contínuo**.

## Comparação

| Característica | Git Flow | GitHub Flow | Trunk-based |
| --- | --- | --- | --- |
| Complexidade | Alta | Média | Baixa |
| Branches longas | Sim | Não | Não |
| Frequência de integração | Baixa | Média | Alta |
| Releases | Agendadas | Contínuas | Contínuas |
| Revisão por PR | Sim | Sim | Sim (opcional) |
| Indicado para | Equipes grandes | Maioria dos projetos | DevOps maduro |

## Como escolher

- **Git Flow**: releases versionadas, múltiplas versões em produção.
- **GitHub Flow**: a maioria dos projetos com PR e deploy frequente.
- **Trunk-based**: entrega contínua, testes automatizados e equipe experiente.

## Boas práticas (valem para qualquer fluxo)

- Commits pequenos e com mensagens claras.
- Branches curtas, com um único objetivo.
- Sempre passar por **revisão** (pull request) antes do merge.
- Manter a branch principal **sempre funcionando**.

## Erros comuns

- **Adotar Git Flow em um projeto pequeno**, gerando burocracia desnecessária.
- **Trabalhar direto na `main`** em vez de usar branches.
- **Branches longevas**: quanto mais tempo uma branch vive, maiores os conflitos.
- **Misturar assuntos** em uma mesma branch/PR.
- **Não definir o fluxo com a equipe**, cada um fazendo de um jeito.
- **Fazer deploy a partir de branch desatualizada**.

## Casos de uso

| Contexto | Fluxo indicado |
| --- | --- |
| Startup com deploy diário | GitHub Flow |
| Produto com versões agendadas | Git Flow |
| Equipe madura com CI/CD | Trunk-based |
| Projeto open source com PRs | GitHub Flow (fork + PR) |
| Manutenção de várias versões | Git Flow (release/hotfix) |
