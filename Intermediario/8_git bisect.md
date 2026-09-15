---
titulo: git bisect
tipo: comando
nivel: intermediario
categoria: Git
tags: [git, bisect, bug, busca-binaria, depuracao]
resumo: "Como usar busca binária com git bisect para encontrar o commit que introduziu um bug, inclusive de forma automática."
relacionados: ["Inspeção do histórico", "git reflog", "Clone parcial e shallow"]
fonte: https://git-scm.com/docs/git-bisect
---

# git bisect

## O que é?

O `git bisect` usa **busca binária** para descobrir **qual commit introduziu um bug**. Em vez de testar commit por commit, ele divide o intervalo pela metade a cada passo, encontrando o culpado muito mais rápido.

Por exemplo, entre 1000 commits, são necessários cerca de **10 testes** para achar o commit problemático.

## Como funciona?

Você informa um commit **bom** (onde tudo funcionava) e um commit **ruim** (onde o bug aparece). O Git vai marcando commits intermediários até isolar o primeiro commit ruim.

```
bom ------------------------- ruim
              |             |
        testa o meio, descarta metade
              |     |
        testa o meio, descarta metade
                  |
             commit culpado
```

## Fluxo manual

```bash
# 1. inicia o bisect
git bisect start

# 2. marca o estado atual (ou um commit) como ruim
git bisect bad

# 3. marca um commit antigo como bom
git bisect good <hash>

# 4. o Git faz checkout de um commit intermediário
#    teste o projeto e informe o resultado:
git bisect good     # se estiver funcionando
git bisect bad      # se estiver com o bug

# 5. repita até o Git indicar o primeiro commit ruim

# 6. encerra e volta ao estado original
git bisect reset
```

Ao final, o Git mostra algo como:

```
3f2a1b9c... is the first bad commit
```

## Automatizando

Se você tem um **script de teste** que retorna `0` para bom e diferente de `0` para ruim, o processo é automático:

```bash
git bisect start
git bisect bad HEAD
git bisect good <hash>
git bisect run ./teste.sh
```

- O script roda em cada commit testado.
- O Git encontra o commit culpado sem intervenção manual.

## Comandos

| Comando | Descrição |
| --- | --- |
| `git bisect start` | Inicia a busca |
| `git bisect good <hash>` | Marca um commit bom |
| `git bisect bad <hash>` | Marca um commit ruim |
| `git bisect run <script>` | Automatiza a busca |
| `git bisect reset` | Encerra e volta ao estado original |
| `git bisect log` | Mostra o histórico da sessão |

## Quando usar?

- Quando você **sabe que algo funcionava** antes e parou de funcionar.
- Para localizar rapidamente a origem de uma **regressão**.
- Quando há **muitos commits** entre o estado bom e o ruim.

## Cuidados

- Sempre encerre com `git bisect reset` para voltar à branch original.
- Anote os hashes de início (bom e ruim) antes de começar.

## Erros comuns

- **Não encerrar com `git bisect reset`**, deixando o repositório em estado destacado.
- **Marcar um commit errado como bom/ruim**, inviabilizando a busca.
- **Não ter um teste confiável** para reproduzir o bug, tornando o resultado incerto.
- **Esquecer de anotar os hashes** de início (bom e ruim).
- **Testar commits que não compilam** e confundir isso com o bug.

## Casos de uso

| Cenário | Comando |
| --- | --- |
| Achar o commit que introduziu um bug | `git bisect start` + `good`/`bad` |
| Busca automática com script de teste | `git bisect run ./teste.sh` |
| Investigar uma regressão de performance | bisect com teste de benchmark |
| Localizar quando um comportamento mudou | bisect manual |
