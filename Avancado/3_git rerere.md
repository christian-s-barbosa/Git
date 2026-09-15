---
titulo: git rerere
tipo: comando
nivel: avancado
categoria: Git
tags: [git, rerere, conflitos, resolucao, rebase, reuse]
resumo: "Como o git rerere grava e reutiliza resoluções de conflitos, útil em rebases longos."
relacionados: ["Merge avançado", "git rebase", "git am e format-patch"]
fonte: https://git-scm.com/docs/git-rerere
---

# git rerere

## O que é?

**rerere** significa **"reuse recorded resolution"** (reutilizar resolução gravada). O Git **memoriza como você resolveu um conflito** e, se o mesmo conflito aparecer de novo, aplica a resolução **automaticamente**.

É muito útil em **rebases longos** ou branches que são constantemente atualizadas.

## Como funciona?

1. Ao resolver um conflito, o Git grava a resolução em `.git/rr-cache/`.
2. Se o mesmo conflito reaparecer, o Git aplica a resolução anterior.
3. Você só precisa revisar e continuar.

## Ativar

```bash
git config --global rerere.enabled true
```

- Também pode ser ativado por repositório (sem `--global`).
- Ative **antes** de começar o rebase/merge.

## Comandos

```bash
# mostra o estado do rerere
git rerere status

# mostra as alterações que o rerere aplicou
git rerere diff

# esquece a resolução gravada de um conflito
git rerere forget arquivo.txt

# aplica a resolução gravada (sem esperar o conflito)
git rerere
```

## Fluxo típico

```bash
git config rerere.enabled true

git rebase main
# ... conflito ...
# resolve e marca
git add arquivo.txt
git rebase --continue

# mais adiante, o mesmo conflito aparece
# o rerere resolve automaticamente
```

## Erros comuns

- **Ativar o rerere depois de já ter começado** o rebase: ele não grava o que já passou.
- **Confiar cegamente na resolução automática** sem revisar o resultado.
- **Esquecer que o `.git/rr-cache` é local** e não é compartilhado.
- **Não limpar resoluções erradas** com `git rerere forget`.

## Casos de uso

| Situação | Benefício |
| --- | --- |
| Rebase de branch longa | Evita resolver o mesmo conflito várias vezes |
| Atualizações frequentes da main | Reaplica resoluções conhecidas |
| Múltiplos rebases | Automatiza conflitos repetidos |
| Merges recorrentes | Reduz trabalho manual |
