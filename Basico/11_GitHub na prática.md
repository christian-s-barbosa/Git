---
titulo: GitHub na prática (Fork, Pull Request e Issues)
tipo: conceito
nivel: basico
categoria: Git
tags: [github, fork, pull-request, pr, issues, code-review, colaboracao]
resumo: "Fluxo de colaboração no GitHub com fork, clone, upstream, pull request, issues e code review."
relacionados: ["Code review", "Sincronização (remote, fetch, pull, push)", "Git e GitHub"]
fonte: https://docs.github.com/pt
---

# GitHub na prática (Fork, Pull Request e Issues)

## O que é?

Além de hospedar repositórios, o GitHub oferece ferramentas de **colaboração**. As principais são **fork**, **pull request** e **issues**. Elas permitem que várias pessoas trabalhem juntas em um projeto, mesmo sem permissão de escrita no repositório original.

## Fluxo de colaboração

```
Fork  →  Clone  →  Branch  →  Commits  →  Push  →  Pull Request  →  Review  →  Merge
```

1. Você faz um **fork** do projeto.
2. **Clona** o seu fork.
3. Cria uma **branch** para a sua alteração.
4. Faz os **commits**.
5. Envia (**push**) para o seu fork.
6. Abre um **pull request** para o projeto original.
7. A alteração é **revisada** e, se aprovada, **mesclada** (merge).

## Fork

Um **fork** é uma **cópia do repositório** de outra pessoa na **sua conta** do GitHub. Você passa a ter controle total sobre essa cópia.

- Usado quando você **não tem permissão** de escrita no repositório original.
- O fork fica independente: suas alterações vão para ele.

No GitHub: botão **Fork** no canto superior direito do repositório.

## Clone

Depois do fork, copie o repositório para a sua máquina:

```bash
git clone https://github.com/seu-usuario/repositorio.git
```

## Sincronizar o fork com o original

O fork **não se atualiza sozinho**. Para trazer as novidades do projeto original, adicione-o como `upstream`:

```bash
# adiciona o repositório original como upstream
git remote add upstream https://github.com/original/repositorio.git

# verifica os remotos
git remote -v

# atualiza a sua branch main
git fetch upstream
git switch main
git merge upstream/main
git push origin main
```

## Pull Request (PR)

Um **pull request** é um **pedido para que suas alterações sejam integradas** ao repositório original. Nele, o mantenedor revisa o código antes de aceitar.

### Como abrir um PR

1. Faça as alterações em uma **branch** do seu fork.
2. Envie a branch: `git push origin minha-branch`.
3. No GitHub, clique em **Compare & pull request**.
4. Escolha a branch de **origem** (seu fork) e a de **destino** (repositório original).
5. Escreva um **título** e uma **descrição** explicando a mudança.
6. Clique em **Create pull request**.

### O que pode acontecer

- **Aprovado e mesclado (merged)**: sua alteração entra no projeto.
- **Comentários e pedidos de ajuste**: você altera a branch e envia de novo.
- **Fechado sem merge**: o PR não é aceito.

## Issues

Uma **issue** é uma forma de **registrar e discutir** algo sobre o projeto, como:

- **Bugs** (erros a corrigir).
- **Sugestões** de melhoria.
- **Dúvidas** e tarefas.

Boas issues são claras, com passos para reproduzir o problema e, se possível, imagens e exemplos.

## Code review

É a **revisão do código** feita em um pull request antes do merge. O revisor pode:

- Comentar linhas específicas.
- Sugerir mudanças.
- Aprovar (**Approve**).
- Pedir alterações (**Request changes**).

Objetivo: melhorar a qualidade do código e compartilhar conhecimento.

## Fork x Clone

| Característica | Fork | Clone |
| --- | --- | --- |
| Onde acontece | No GitHub (conta) | Na sua máquina |
| O que faz | Cópia do repositório na sua conta | Cópia para trabalhar localmente |
| Precisa de fork? | — | Não, dá para clonar direto |
| Uso típico | Contribuir sem permissão de escrita | Trabalhar em qualquer repositório |

## Boas práticas

- Crie uma **branch por contribuição** (não trabalhe na `main` do fork).
- Mantenha o fork **atualizado** com o `upstream`.
- Faça **commits pequenos** e com mensagens claras.
- Um PR deve resolver **um único assunto**.
- Descreva bem o PR: o que mudou, por quê e como testar.

## Erros comuns

- **Abrir PR da branch errada** (origem/destino trocados).
- **PR gigante** com muitos assuntos.
- **Não atualizar o fork** com o `upstream`, acumulando divergência.
- **Trabalhar na `main` do fork** em vez de uma branch.
- **Abrir PR sem descrever** a mudança.
- **Esquecer de rodar/testar** antes de abrir o PR.

## Casos de uso

| Situação | Ação |
| --- | --- |
| Contribuir sem permissão de escrita | fork + branch + PR |
| Propor uma melhoria | issue ou PR |
| Reportar um bug | issue |
| Revisar o código de alguém | code review no PR |
| Manter o fork atualizado | `fetch upstream` + merge |
