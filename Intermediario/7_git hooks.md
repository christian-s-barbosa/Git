---
titulo: git hooks
tipo: comando
nivel: intermediario
categoria: Git
tags: [git, hooks, pre-commit, automacao, scripts]
resumo: "Como automatizar ações com hooks do Git (pre-commit, commit-msg, pre-push etc.) e como compartilhá-los."
relacionados: ["Git em CI-CD", "GitHub Actions", "Aliases e configurações"]
fonte: https://git-scm.com/docs/githooks
---

# git hooks

## O que é?

**Hooks** são **scripts executados automaticamente** pelo Git em momentos específicos, como antes de um commit ou antes de um push. Eles permitem **automatizar** verificações e tarefas.

## Onde ficam?

Os hooks ficam na pasta **`.git/hooks/`** do repositório. Por padrão, o Git cria arquivos de exemplo com a extensão `.sample`, que **não são executados** até você removê-la.

```bash
ls .git/hooks/
```

> Atenção: a pasta `.git` **não é versionada**, então os hooks **não são compartilhados** automaticamente pelo repositório.

## Principais hooks (cliente)

| Hook | Quando executa |
| --- | --- |
| `pre-commit` | Antes de criar um commit |
| `prepare-commit-msg` | Antes de abrir o editor da mensagem |
| `commit-msg` | Após escrever a mensagem do commit |
| `post-commit` | Após o commit ser criado |
| `pre-push` | Antes de enviar um push |
| `pre-rebase` | Antes de um rebase |

## Principais hooks (servidor)

| Hook | Quando executa |
| --- | --- |
| `pre-receive` | Antes de aceitar os commits enviados |
| `update` | Para cada branch atualizada |
| `post-receive` | Após os commits serem aceitos |

## Exemplo de pre-commit

Arquivo `.git/hooks/pre-commit`:

```bash
#!/bin/sh
echo "Rodando verificações antes do commit..."

# roda os testes; se falhar, cancela o commit
npm test
if [ $? -ne 0 ]; then
    echo "Testes falharam. Commit cancelado."
    exit 1
fi
```

Para ativar, o arquivo precisa ter permissão de execução:

```bash
chmod +x .git/hooks/pre-commit
```

- `exit 0` (ou nenhum exit) permite a operação.
- `exit 1` **cancela** a operação.

## Compartilhar hooks com a equipe

Como `.git/hooks` não é versionada, existem formas de compartilhar:

- Guardar os hooks em uma pasta versionada (ex.: `.githooks/`) e apontar:

```bash
git config core.hooksPath .githooks
```

- Usar ferramentas como **Husky** (JavaScript) ou **pre-commit** (Python), que instalam e versionam os hooks.

## Cuidados

- Hooks podem ser **ignorados** com `git commit --no-verify` (no caso de `pre-commit`/`commit-msg`).
- Nunca dependa só de hooks para segurança: eles rodam na máquina do desenvolvedor.
- Mantenha os scripts **rápidos** para não atrapalhar o fluxo.

## Erros comuns

- **Esperar que os hooks sejam versionados**: `.git/hooks` não vai para o repositório.
- **Esquecer o `chmod +x`**, deixando o hook sem execução.
- **Hooks lentos** que atrapalham o commit.
- **Usar hooks como única barreira de segurança** (podem ser burlados com `--no-verify`).
- **Depender de ferramentas não instaladas** na máquina dos colegas.
- **Erros silenciosos**: não usar `exit 1` quando a verificação falha.

## Casos de uso

| Objetivo | Hook |
| --- | --- |
| Rodar lint/testes antes de commitar | `pre-commit` |
| Padronizar a mensagem do commit | `commit-msg` |
| Impedir push de código quebrado | `pre-push` |
| Rodar build/notificação após o commit | `post-commit` |
| Validar commits no servidor | `pre-receive` |
