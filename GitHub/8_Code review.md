---
titulo: Code review
tipo: conceito
nivel: intermediario
categoria: GitHub
tags: [github, code-review, pull-request, revisao, boas-praticas]
resumo: "Como funciona o code review em pull requests no GitHub, boas práticas para autor e revisor e proteção de branch."
relacionados: ["GitHub na prática (Fork, Pull Request e Issues)", "Projects", "Discussions"]
fonte: https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests
---

# Code review

## O que é?

**Code review** é a **revisão do código** feita em um **pull request** antes de integrá-lo à branch principal. O objetivo é melhorar a qualidade, encontrar bugs e compartilhar conhecimento.

## Fluxo de revisão

```
Abre PR → Revisores analisam → Comentam/Sugerem → Autor ajusta → Aprovam → Merge
```

## O que o revisor pode fazer

| Ação | Significado |
| --- | --- |
| **Comment** | Comentário sem aprovar/reprovar |
| **Approve** | Aprova a mudança |
| **Request changes** | Pede ajustes antes do merge |
| **Sugestão** | Propõe uma alteração direta na linha |

As **sugestões** podem ser aplicadas com um clique (ou commit em lote).

## Boas práticas para quem abre o PR

- Um PR = **um assunto**.
- Título e **descrição claros** (o que, por quê, como testar).
- PRs **pequenos** (mais fáceis de revisar).
- Vincule a **issue** relacionada.
- Rode testes/lint **antes** de abrir.
- Responda aos comentários e ajuste.

## Boas práticas para quem revisa

- Revise **em tempo razoável**.
- Seja **específico** e **respeitoso**.
- Explique o **porquê**, não só aponte.
- Diferencie **bloqueador** de **sugestão**.
- Elogie o que estiver bom.
- Aprove quando estiver adequado; não exija perfeição.

## Proteção de branch

Em **Settings → Branches**, é possível exigir:

- Revisão aprovada antes do merge.
- Status checks (CI) verdes.
- Histórico linear / sem force push.
- Resolução de conversas.

## Erros comuns

- **PR gigante** e impossível de revisar.
- **Aprovar sem ler** (rubber stamp).
- **Comentários vagos** ("isso está errado") sem explicar.
- **Levar para o lado pessoal**.
- **Revisar só no fim**, acumulando conflitos.
- **Fazer merge sem os checks passarem**.

## Casos de uso

| Situação | Prática |
| --- | --- |
| Nova funcionalidade | PR + revisão obrigatória |
| Correção de bug | PR pequeno e focado |
| Refatoração | PR com descrição clara |
| Projeto open source | Revisão da comunidade |
| Padronização | Proteção de branch + checks |
