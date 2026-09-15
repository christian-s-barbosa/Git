---
titulo: Inspeção do histórico
tipo: conceito
nivel: intermediario
categoria: Git
tags: [git, log, blame, diff, show, historico, inspecao]
resumo: "Consultar o histórico com git log e filtros, git show, git diff, git blame e git grep."
relacionados: ["git shortlog e log --follow", "git range-diff", "git reflog"]
fonte: https://git-scm.com/docs/git-log
---

# Inspeção do histórico

## O que é?

Inspecionar o histórico é **consultar o que aconteceu** no projeto: quais commits existem, quem alterou cada linha, quando e por quê. O Git oferece várias ferramentas para isso, sendo as principais `git log`, `git show`, `git diff` e `git blame`.

## git log

Mostra o histórico de commits. Aceita muitos filtros.

```bash
git log                          # histórico completo
git log --oneline                # uma linha por commit
git log --oneline --graph --all  # gráfico com todas as branches
git log -p                       # mostra o diff de cada commit
git log --stat                   # resumo de arquivos alterados
```

### Filtros úteis

```bash
git log --author="Maria"              # commits de um autor
git log --since="2026-01-01"          # a partir de uma data
git log --until="2026-06-30"          # até uma data
git log --grep="login"                # commits cuja mensagem contém "login"
git log -S"funcaoX"                   # commits que alteraram o número de ocorrências do texto
git log -- arquivo.txt                # histórico de um arquivo
git log main..feature                 # commits que estão na feature e não na main
```

## git show

Mostra os **detalhes de um objeto** (geralmente um commit):

```bash
git show <hash>          # detalhes de um commit
git show HEAD            # último commit
git show v1.0.0          # uma tag
```

## git diff

Mostra **diferenças** entre estados, commits ou branches.

```bash
git diff                     # working directory x staging
git diff --staged            # staging x último commit
git diff main feature        # diferença entre duas branches
git diff <hash1> <hash2>     # diferença entre dois commits
git diff <hash> -- arquivo   # diferença de um arquivo
```

## git blame

Mostra **quem alterou cada linha** de um arquivo e em qual commit.

```bash
git blame arquivo.txt
git blame -L 10,20 arquivo.txt    # apenas as linhas 10 a 20
```

Saída:

```
a7b3f10 (Maria  2026-03-02) const total = soma(itens);
3f2a1b9 (João   2026-03-05) return total * 1.1;
```

- Útil para entender **quando** e **por quem** uma linha foi introduzida.
- Ajuda a encontrar o commit que causou um bug.

## Comandos

| Comando | Descrição |
| --- | --- |
| `git log` | Histórico de commits |
| `git log --oneline --graph --all` | Histórico visual de todas as branches |
| `git log --author="X"` | Filtra por autor |
| `git log --since` / `--until` | Filtra por data |
| `git log --grep="texto"` | Filtra pela mensagem |
| `git show <hash>` | Detalhes de um commit |
| `git diff` | Diferenças entre estados |
| `git blame <arquivo>` | Autoria linha a linha |

## Boas práticas

- Use `git log --oneline --graph --all` para **visualizar** a estrutura das branches.
- Combine filtros (`--author`, `--since`, `--grep`) para achar commits rapidamente.
- Use `git blame` para investigar a origem de uma linha, não para "culpar" pessoas.

## Erros comuns

- **Confundir `git diff` e `git diff --staged`**: um mostra o working directory, o outro o que está preparado.
- **Achar que `git log` mostra tudo**: por padrão, mostra só a branch atual (use `--all`).
- **Usar `git blame` para culpar pessoas** em vez de investigar o código.
- **Ignorar os filtros** e percorrer um `log` gigante manualmente.
- **Interpretar `-S` como busca no código atual**: ele busca commits que alteraram o número de ocorrências do texto.

## Casos de uso

| Cenário | Comando |
| --- | --- |
| Ver quem alterou uma linha específica | `git blame -L 10,20 arquivo` |
| Achar quando um texto foi introduzido | `git log -S"funcaoX"` |
| Ver commits de um autor | `git log --author="Maria"` |
| Comparar duas branches | `git diff main feature` |
| Ver commits que não estão na main | `git log main..feature` |
