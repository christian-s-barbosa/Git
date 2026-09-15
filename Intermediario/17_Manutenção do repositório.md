---
titulo: Manutenção do repositório
tipo: comando
nivel: intermediario
categoria: Git
tags: [git, gc, fsck, prune, repack, manutencao, objetos]
resumo: "Comandos de manutenção do Git: git gc, fsck, prune, repack e verificação do tamanho do repositório."
relacionados: ["git maintenance", "Internos a fundo (packfiles e gc)", "git clean e arquivos não rastreados"]
fonte: https://git-scm.com/docs/git-gc
---

# Manutenção do repositório

## O que é?

Com o tempo, o repositório acumula **objetos soltos**, referências antigas e dados que podem ser otimizados. Os comandos de manutenção **compactam**, **verificam** e **limpam** o repositório.

## git gc

**Garbage collection**: compacta objetos em packfiles e remove o que não é mais alcançável.

```bash
git gc
git gc --aggressive    # otimização mais profunda (mais lenta)
```

- Roda **automaticamente** em algumas operações (o Git decide quando).
- Normalmente **não é preciso** rodar manualmente.

## git fsck

**Verifica a integridade** do repositório e encontra objetos corrompidos ou órfãos.

```bash
git fsck
git fsck --full
```

Saída comum:

```
dangling commit 3f2a1b9...
```

- `dangling` = objeto não referenciado (candidato a remoção).
- Útil após uma recuperação com reflog ou suspeita de corrupção.

## git count-objects

Mostra o **tamanho** e a quantidade de objetos.

```bash
git count-objects -v
git count-objects -vH    # em formato legível (KB, MB...)
```

## git prune

Remove objetos que **não são mais referenciados** por nada.

```bash
git prune
```

> Cuidado: objetos "perdidos" que você pretendia recuperar pelo reflog podem ser removidos.

## git repack

Reorganiza os objetos em **packfiles**.

```bash
git repack -a -d
```

## Comandos

| Comando | Descrição |
| --- | --- |
| `git gc` | Compacta e limpa o repositório |
| `git fsck` | Verifica a integridade |
| `git count-objects -vH` | Mostra o tamanho dos objetos |
| `git prune` | Remove objetos não referenciados |
| `git repack -a -d` | Reorganiza os packfiles |

## Erros comuns

- **Rodar `git gc --aggressive` sempre**: é lento e raramente necessário.
- **Usar `git prune` logo após perder commits**, apagando o que o reflog ainda poderia recuperar.
- **Ignorar avisos do `git fsck`** em repositórios importantes.
- **Confundir `gc` com `clean`**: `gc` mexe em objetos internos; `clean` remove arquivos não rastreados.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Ver o tamanho do repositório | `git count-objects -vH` |
| Verificar corrupção | `git fsck --full` |
| Compactar após muitas operações | `git gc` |
| Reduzir tamanho após remover arquivos | `git gc` / `git repack` |
