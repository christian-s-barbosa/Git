---
titulo: git cherry-pick
tipo: comando
nivel: intermediario
categoria: Git
tags: [git, cherry-pick, commit, seletivo, branch]
resumo: "Como copiar commits específicos de uma branch para outra com cherry-pick, conflitos e cuidados."
relacionados: ["git rebase", "Merge avançado", "git range-diff"]
fonte: https://git-scm.com/docs/git-cherry-pick
---

# git cherry-pick

## O que é?

O `git cherry-pick` **copia um commit específico** de uma branch e o aplica na branch atual. É como "escolher a dedo" um commit, sem precisar mesclar a branch inteira.

O nome vem da ideia de "colher" (pick) uma "cereja" (cherry) entre várias.

## Como funciona?

Considere:

```
A --- B --- C   (main)
       \
        D --- E   (feature)
```

Estando na `main`, ao rodar `git cherry-pick E`, o commit `E` é reaplicado na `main` com um **novo hash** (`E'`):

```
A --- B --- C --- E'   (main)
       \
        D --- E         (feature)
```

- O commit original (`E`) **permanece** na `feature`.
- O novo commit (`E'`) tem conteúdo igual, mas hash diferente.

## Comandos básicos

```bash
# aplica um commit específico
git cherry-pick <hash>

# aplica vários commits
git cherry-pick <hash1> <hash2>

# aplica um intervalo (exclusivo no início)
git cherry-pick <hash-inicial>..<hash-final>

# aplica sem criar o commit (apenas no stage/working)
git cherry-pick -n <hash>
```

## Conflitos

Podem ocorrer se o conteúdo do commit não se encaixar bem na branch atual.

```bash
# resolve os arquivos, marca e continua
git add arquivo.txt
git cherry-pick --continue

# cancela e volta ao estado anterior
git cherry-pick --abort

# pula o commit atual
git cherry-pick --skip
```

## Quando usar?

- Trazer uma **correção urgente** (hotfix) de uma branch para outra.
- Aplicar **um único commit** útil sem mesclar toda a branch.
- Reaplicar um commit que foi feito na branch errada.

## Cuidados

- **Duplica** o commit (novo hash): a mesma alteração passa a existir em dois lugares.
- Em excesso, deixa o histórico **confuso** e dificulta merges futuros.
- Se precisar de **muitos** commits de outra branch, normalmente **merge** ou **rebase** são melhores.

## Erros comuns

- **Duplicar commits** sem perceber: o cherry-pick cria um novo commit, então a mesma mudança passa a existir em dois lugares.
- **Usar cherry-pick em vez de merge** para trazer muitos commits, poluindo o histórico.
- **Esquecer de resolver os conflitos** e finalizar com `--continue`.
- **Fazer cherry-pick de um commit de merge** sem usar `-m`, gerando erro.
- **Trazer um commit que depende de outros** ausentes na branch atual, causando conflitos ou código quebrado.

## Casos de uso

| Cenário | Exemplo |
| --- | --- |
| Aplicar um hotfix da `main` em uma branch de release | `git cherry-pick <hash-do-fix>` |
| Trazer um commit feito na branch errada | `git cherry-pick <hash>` |
| Reaproveitar uma correção em várias branches | cherry-pick em cada branch |
| Aplicar apenas um commit útil de outra branch | `git cherry-pick <hash>` |
