---
titulo: Sincronização (remote, fetch, pull, push)
tipo: conceito
nivel: basico
categoria: Git
tags: [git, remote, fetch, pull, push, origin, upstream, sincronizacao]
resumo: "Como sincronizar o repositório local com o remoto usando remote, fetch, pull e push, incluindo tracking e push rejeitado."
relacionados: ["Repositório Local e Remoto", "Refspecs", "GitHub na prática (Fork, Pull Request e Issues)"]
fonte: https://git-scm.com/docs
---

# Sincronização (remote, fetch, pull, push)

## O que é?

Sincronização é o processo de **enviar** e **receber** commits entre o repositório **local** e o repositório **remoto**. Isso permite trabalhar com outras pessoas e manter o projeto atualizado.

- **Enviar** alterações locais para o remoto: `git push`.
- **Receber** alterações do remoto: `git fetch` e `git pull`.

## Repositório remoto (`git remote`)

Um **remote** é um apelido para o endereço de um repositório na nuvem. O mais comum é chamado de **origin**.

| Comando | Descrição |
| --- | --- |
| `git remote` | Lista os nomes dos remotos |
| `git remote -v` | Lista os remotos com os endereços (fetch e push) |
| `git remote add origin <url>` | Adiciona um remoto chamado origin |
| `git remote rename origin novo` | Renomeia um remoto |
| `git remote remove origin` | Remove um remoto |
| `git remote set-url origin <url>` | Altera o endereço do remoto |

### origin e upstream

- **origin**: nome padrão do remoto de onde você clonou.
- **upstream**: nome comum para o repositório original, quando se trabalha com **fork** (uma cópia do repositório original na sua conta).

```bash
git remote add upstream https://github.com/original/repositorio.git
```

## git fetch

**Baixa** as novidades do remoto para o repositório local, mas **não altera** seus arquivos nem faz merge.

```bash
git fetch origin
git fetch --all        # busca de todos os remotos
```

- É seguro: apenas atualiza as referências remotas (ex.: `origin/main`).
- Depois você decide o que fazer (comparar, fazer merge, etc.).

## git pull

É a combinação de **fetch + merge**: baixa as alterações do remoto e **já as integra** na sua branch atual.

```bash
git pull
git pull origin main
```

Equivale a:

```bash
git fetch origin
git merge origin/main
```

> Como o `pull` faz merge automático, pode gerar **conflitos**. Se preferir revisar antes, use `fetch` e depois `merge` manualmente.

## git push

**Envia** os commits locais para o repositório remoto.

```bash
git push
git push origin main
git push -u origin main    # envia e define o upstream (só na primeira vez)
git push origin feature/login
```

- `-u` (ou `--set-upstream`) liga a branch local à branch remota. Depois disso, basta `git push` e `git pull`.
- Só é possível enviar o que já foi **commitado**.

## Branch de rastreamento (tracking)

Quando uma branch local é ligada a uma remota, ela passa a **rastrear** a remota (ex.: `main` rastreia `origin/main`).

```bash
git branch -vv             # mostra as branches e seus upstreams
```

- `git status` informa se você está à frente (ahead) ou atrás (behind) do remoto.

## Fetch x Pull

| Característica | git fetch | git pull |
| --- | --- | --- |
| Baixa alterações | Sim | Sim |
| Integra (merge) | Não | Sim |
| Altera arquivos locais | Não | Sim |
| Pode gerar conflito | Não | Sim |
| Segurança | Mais seguro | Menos previsível |

## Divergência e push rejeitado

Se alguém enviou commits antes de você, o Git pode **recusar o push**:

```
! [rejected] main -> main (non-fast-forward)
```

Solução básica: **primeiro receber, depois enviar**.

```bash
git pull          # traz e integra as alterações do remoto
# resolve conflitos, se houver
git push          # agora o envio funciona
```

## Fluxo típico de sincronização

```bash
# começar o dia atualizado
git switch main
git pull

# trabalhar
git add .
git commit -m "Implementa funcionalidade"

# publicar
git push
```

## Clonar um repositório

O `clone` já cria o repositório local, configura o `origin` e baixa o histórico:

```bash
git clone https://github.com/usuario/repositorio.git
```

## Erros comuns

- **Confundir `fetch` com `pull`**: o `pull` já faz merge.
- **Fazer `push` sem ter feito `pull`** e receber "rejected".
- **Achar que `commit` envia para o remoto**.
- **Esquecer o `-u`** no primeiro push e ter que indicar a branch sempre.
- **Resolver conflitos no meio de um pull** de forma apressada.
- **Trabalhar em cima de um `origin/main` desatualizado**.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Baixar sem alterar arquivos | `git fetch` |
| Baixar e integrar | `git pull` |
| Enviar commits | `git push` |
| Primeiro push de uma branch | `git push -u origin branch` |
| Listar remotos | `git remote -v` |
| Adicionar um remoto | `git remote add origin <url>` |
