---
titulo: Projects
tipo: conceito
nivel: intermediario
categoria: GitHub
tags: [github, projects, kanban, tarefas, gestao, issues]
resumo: "Como organizar tarefas com GitHub Projects (board, table, roadmap), campos e diferenças para issues."
relacionados: ["Discussions", "Code review", "GitHub na prática (Fork, Pull Request e Issues)"]
fonte: https://docs.github.com/pt/issues/planning-and-tracking-with-projects
---

# Projects

## O que é?

**GitHub Projects** é uma ferramenta de **gerenciamento de tarefas** integrada ao repositório. Permite organizar **issues** e **pull requests** em quadros (estilo Kanban), tabelas e roteiros (roadmaps).

## Para que serve?

- Planejar e acompanhar o trabalho.
- Visualizar o andamento (a fazer, em andamento, concluído).
- Priorizar e agrupar tarefas.
- Conectar issues/PRs a um plano.

## Visões (views)

| Visão | Formato |
| --- | --- |
| **Board** | Quadro Kanban por colunas |
| **Table** | Planilha com campos |
| **Roadmap** | Linha do tempo (datas/marcos) |

## Campos

Além dos campos padrão (status, responsável), é possível criar campos customizados:

- **Status**: Todo, In Progress, Done.
- **Prioridade**: Baixa, Média, Alta.
- **Sprint**, **Tamanho**, **Data de entrega**, etc.

## Como usar

1. Vá na aba **Projects** do repositório ou perfil.
2. Crie um novo projeto (board/table).
3. Adicione **issues** e **pull requests**.
4. Organize nas colunas e campos.
5. Use **automações** (ex.: mover para "Done" ao fechar a issue).

## Projects x Issues

| Característica | Issue | Project |
| --- | --- | --- |
| O que é | Item/tarefa individual | Painel que organiza itens |
| Escopo | Um assunto | Vários itens |
| Visualização | Lista | Board/Table/Roadmap |

## Erros comuns

- **Criar muitas colunas** e complicar o fluxo.
- **Não vincular issues** ao projeto, perdendo o rastreio.
- **Usar Project como documentação** em vez de tarefas.
- **Não automatizar** e atualizar tudo manualmente.

## Casos de uso

| Situação | Uso |
| --- | --- |
| Organizar sprints | Board com status |
| Acompanhar roadmap | Visão Roadmap |
| Priorizar backlog | Table com campo prioridade |
| Planejar release | Agrupar issues por marco |
| Acompanhar bugs | Board de issues |
