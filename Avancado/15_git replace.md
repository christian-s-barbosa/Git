---
titulo: git replace
tipo: comando
nivel: avancado
categoria: Git
tags: [git, replace, objetos, substituto, refs]
resumo: "Como substituir objetos do Git sem reescrever o histórico usando git replace e git replace --graft."
relacionados: ["Reescrever histórico (filter-repo)", "Internos a fundo (packfiles e gc)", "Como o Git funciona por dentro"]
fonte: https://git-scm.com/docs/git-replace
---

# git replace

## O que é?

O `git replace` permite **substituir um objeto** (commit, tree, blob) por outro, **sem reescrever o histórico**. A substituição vale localmente e é registrada em uma ref especial (`refs/replace/`).

É útil para **testar** mudanças de histórico ou corrigir um objeto problemático sem alterar os hashes.

## Comandos

```bash
# substitui um commit por outro
git replace <objeto-antigo> <objeto-novo>

# lista as substituições
git replace -l

# remove uma substituição
git replace -d <objeto-antigo>

# edita um objeto interativamente
git replace --edit <objeto>

# cria um commit substituto a partir de um existente
git replace --graft <commit> <novo-pai>
```

## Exemplo

```bash
# faz o commit A "apontar" para o conteúdo do commit B
git replace a1b2c3d b2c3d4e

# a partir de agora, o Git enxerga B no lugar de A
git log

# remover a substituição
git replace -d a1b2c3d
```

## Substituir pai (--graft)

Muda o histórico "enxergado", sem reescrever os commits:

```bash
# faz o commit X ter como pai o commit Y
git replace --graft <X> <Y>
```

## Tornar a substituição permanente

O `filter-repo` pode "assar" as substituições no histórico:

```bash
git filter-repo --replace-refs update-no-add
```

## Erros comuns

- **Achar que a substituição é enviada no push normal**: as refs de replace são locais, a menos que você as envie explicitamente.
- **Esquecer que a substituição é reversível** (`git replace -d`).
- **Confundir `replace` com `filter-repo`**: o primeiro não reescreve; o segundo sim.
- **Usar em produção sem entender** o efeito no histórico visto.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Testar uma mudança de histórico | `git replace` |
| Corrigir o pai de um commit | `git replace --graft` |
| Editar um commit antigo localmente | `git replace --edit` |
| Tornar a substituição permanente | `git filter-repo --replace-refs` |
