---
titulo: git range-diff
tipo: comando
nivel: avancado
categoria: Git
tags: [git, range-diff, comparar, rebase, patch, revisao]
resumo: "Como comparar dois intervalos de commits com git range-diff, útil para revisar rebases e versões de pull request."
relacionados: ["git rebase", "git cherry-pick", "git am e format-patch"]
fonte: https://git-scm.com/docs/git-range-diff
---

# git range-diff

## O que é?

O `git range-diff` compara **dois intervalos de commits** (ranges), mostrando o que mudou entre eles. É especialmente útil para comparar uma branch **antes e depois de um rebase**, ou duas versões de um **pull request**.

Diferente do `git diff`, que compara conteúdo de arquivos, o `range-diff` compara **commits** entre si.

## Sintaxe

```
git range-diff <base1> <topo1> <base2> <topo2>
```

Ou, em uma branch após rebase:

```bash
git range-diff main feature@{1}..feature
```

## Exemplo

```bash
# compara a versão antiga e a nova de uma branch
git range-diff main old-feature main new-feature

# saída resumida (uma linha por commit)
git range-diff --no-patch main old..new
```

Saída típica:

```
1:  a1b2c3d = 1:  a1b2c3d Adiciona login
2:  d4e5f6a ! 2:  f6a7b8c Corrige validação
    - valida apenas email
    + valida email e senha
3:  9c8b7a6 < -:  ------- Remove código morto
```

- `=` commit igual.
- `!` commit alterado.
- `<` commit removido.
- `>` commit adicionado.

## Quando usar

- Revisar uma branch após um **rebase**.
- Conferir se um **force push** alterou mais do que deveria.
- Comparar a versão 1 e a versão 2 de um **pull request**.
- Validar uma **série de patches** reenviada.

## Erros comuns

- **Confundir com `git diff`**: o `range-diff` compara commits, não arquivos.
- **Passar apenas dois argumentos** e receber erro (precisa de 4, ou de uma configuração de range).
- **Usar em ranges sem relação** e obter uma saída confusa.
- **Achar que altera algo**: é um comando apenas de leitura.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Ver o que mudou após um rebase | `git range-diff main antigo..novo` |
| Revisar uma nova versão de PR | `git range-diff main v1..v2` |
| Conferir um force push | `git range-diff` |
| Validar série de patches | `git range-diff` |
