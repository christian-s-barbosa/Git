---
titulo: git maintenance
tipo: comando
nivel: avancado
categoria: Git
tags: [git, maintenance, gc, agendamento, otimizacao, performance]
resumo: "Como automatizar a manutenção do repositório com git maintenance, suas tarefas e diferenças para o git gc."
relacionados: ["Manutenção do repositório", "Internos a fundo (packfiles e gc)", "Clone parcial e shallow"]
fonte: https://git-scm.com/docs/git-maintenance
---

# git maintenance

## O que é?

O `git maintenance` é o comando **moderno de manutenção** do Git. Ele automatiza tarefas que antes eram feitas por `git gc` manual ou por agendadores externos (como `cron`).

É indicado para repositórios grandes, com uso intenso, onde a performance importa.

## Diferença para o git gc

| Característica | git gc | git maintenance |
| --- | --- | --- |
| Execução | Manual/automática | Agendada pelo Git |
| Escopo | Repositório atual | Vários repositórios |
| Tarefas | Compactação geral | Tarefas específicas |
| Otimizações modernas | Limitadas | commit-graph, incremental-repack |

## Comandos principais

```bash
# registra o repositório na manutenção
git maintenance register

# inicia o agendamento automático
git maintenance start

# roda as tarefas agora
git maintenance run

# para o agendamento
git maintenance stop

# remove o repositório do agendamento
git maintenance unregister
```

## Tarefas

| Tarefa | O que faz |
| --- | --- |
| `gc` | Coleta de lixo (objetos soltos) |
| `commit-graph` | Cria/atualiza o grafo de commits (acelera `log`) |
| `prefetch` | Busca commits do remoto em segundo plano |
| `loose-objects` | Compacta objetos soltos em lotes |
| `incremental-repack` | Reorganiza packfiles incrementalmente |

Rodar uma tarefa específica:

```bash
git maintenance run --task=commit-graph
git maintenance run --task=prefetch
```

## O que é agendado

O `git maintenance start` cria agendamentos no sistema:

- **Windows**: Tarefas Agendadas.
- **macOS**: `launchd`.
- **Linux**: `cron` (ou `systemd`).

As tarefas rodam em segundo plano para manter o repositório otimizado.

## Erros comuns

- **Rodar `git gc` manualmente** enquanto a manutenção já está agendada (pode competir).
- **Agendar em repositórios pequenos**: ganho irrelevante.
- **Esquecer que o `prefetch`** acessa a rede em segundo plano.
- **Não perceber que a manutenção é por usuário/repositório registrado**.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Monorepo grande e de uso intenso | `git maintenance start` |
| Acelerar `git log` em repo grande | `git maintenance run --task=commit-graph` |
| Manter vários repositórios otimizados | `git maintenance register` |
| Parar a manutenção automática | `git maintenance stop` |
