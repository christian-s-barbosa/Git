---
titulo: Índice da Base de Conhecimento Git
tipo: indice
nivel: basico
categoria: Git
tags: [git, indice, sumario, knowledge-base, rag]
resumo: "Ponto de entrada da base de conhecimento de Git, com links para todos os arquivos organizados por nível e cheatsheets."
relacionados: ["Comandos Básicos do Git", "Comandos Intermediários do Git", "Comandos Avançados do Git"]
---

# Base de Conhecimento Git

Base de estudos de Git organizada por **nível** e por **cheatsheets de comandos**. Cada arquivo é autocontido e possui frontmatter (`titulo`, `tipo`, `nivel`, `categoria`, `tags`, `resumo`, `relacionados`, `fonte`), pensado para uso em **RAG** (chunking por seção e filtro por metadados).

## Estrutura

| Pasta | Conteúdo | Arquivos |
| --- | --- | --- |
| `Basico/` | Fundamentos do Git | 11 |
| `Intermediario/` | Temas intermediários | 21 |
| `Avancado/` | Temas avançados | 20 |
| `GitHub/` | Recursos do GitHub (não é Git puro) | 8 |
| `Comando/` | Cheatsheets de comandos | 3 |

## Basico

- [Git e GitHub](<Basico/1_Git e GitHub.md>) — conceito, funcionamento, criadores e instalação.
- [Repositório Local e Remoto](<Basico/2_Repositório Local e Remoto.md>) — diferenças, plataformas, usuário, SSH e token.
- [Git commit](<Basico/3_Git commit.md>) — o que é, ciclo de vida, mensagens e boas práticas.
- [Branches (Ramificações)](<Basico/4_Branchs.md>) — branches, HEAD, merge e conflitos.
- [Os três estados do Git](<Basico/5_Os três estados do Git.md>) — working, staging e repositório.
- [Sincronização (remote, fetch, pull, push)](<Basico/6_Sincronização.md>) — sincronizar local e remoto.
- [Desfazer alterações (restore, reset, revert)](<Basico/7_Desfazer alterações.md>) — como desfazer com segurança.
- [git stash](<Basico/8_git stash.md>) — guardar alterações temporárias.
- [git tag](<Basico/9_git tag.md>) — marcar versões e releases.
- [.gitignore](<Basico/10_.gitignore.md>) — ignorar arquivos e padrões.
- [GitHub na prática (Fork, Pull Request e Issues)](<Basico/11_GitHub na prática.md>) — colaboração.

## Intermediario

- [git rebase](<Intermediario/1_git rebase.md>)
- [git cherry-pick](<Intermediario/2_git cherry-pick.md>)
- [git reflog](<Intermediario/3_git reflog.md>)
- [Inspeção do histórico](<Intermediario/4_Inspeção do histórico.md>)
- [Fluxos de trabalho](<Intermediario/5_Fluxos de trabalho.md>)
- [git submodules](<Intermediario/6_git submodules.md>)
- [git hooks](<Intermediario/7_git hooks.md>)
- [git bisect](<Intermediario/8_git bisect.md>)
- [git worktree](<Intermediario/9_git worktree.md>)
- [Git LFS](<Intermediario/10_Git LFS.md>)
- [.gitattributes](<Intermediario/11_.gitattributes.md>)
- [Aliases e configurações](<Intermediario/12_Aliases e configurações.md>)
- [Assinatura de commits e tags](<Intermediario/13_Assinatura de commits e tags.md>)
- [Merge avançado](<Intermediario/14_Merge avançado.md>)
- [Revisões e ranges](<Intermediario/15_Revisões e ranges.md>)
- [Clone parcial e shallow](<Intermediario/16_Clone parcial e shallow.md>)
- [Manutenção do repositório](<Intermediario/17_Manutenção do repositório.md>)
- [Como o Git funciona por dentro](<Intermediario/18_Como o Git funciona por dentro.md>)
- [git grep e git archive](<Intermediario/19_git grep e git archive.md>)
- [Monorepo e polyrepo](<Intermediario/20_Monorepo e polyrepo.md>)
- [Git em CI-CD](<Intermediario/21_Git em CI-CD.md>)

## Avancado

- [git subtree](<Avancado/1_git subtree.md>)
- [git am e format-patch](<Avancado/2_git am e format-patch.md>)
- [git rerere](<Avancado/3_git rerere.md>)
- [sparse-checkout](<Avancado/4_sparse-checkout.md>)
- [git maintenance](<Avancado/5_git maintenance.md>)
- [Refspecs](<Avancado/6_Refspecs.md>)
- [Reescrever histórico (filter-repo)](<Avancado/7_Reescrever histórico (filter-repo).md>)
- [git notes](<Avancado/8_git notes.md>)
- [git bundle](<Avancado/9_git bundle.md>)
- [Internos a fundo (packfiles e gc)](<Avancado/10_Internos a fundo (packfiles e gc).md>)
- [git clean e arquivos não rastreados](<Avancado/11_git clean e arquivos não rastreados.md>)
- [Variantes de rebase (--onto e --root)](<Avancado/12_Variantes de rebase (--onto e --root).md>)
- [git shortlog e log --follow](<Avancado/13_git shortlog e log --follow.md>)
- [git range-diff](<Avancado/14_git range-diff.md>)
- [git replace](<Avancado/15_git replace.md>)
- [git update-index (assume-unchanged e skip-worktree)](<Avancado/16_git update-index (assume-unchanged e skip-worktree).md>)
- [git request-pull](<Avancado/17_git request-pull.md>)
- [git stash avançado](<Avancado/18_git stash avançado.md>)
- [Interoperabilidade (git svn e git p4)](<Avancado/19_Interoperabilidade (git svn e git p4).md>)
- [Protocolos e hospedagem](<Avancado/20_Protocolos e hospedagem.md>)

## GitHub

- [Releases](<GitHub/1_Releases.md>)
- [Gists](<GitHub/2_Gists.md>)
- [GitHub Pages](<GitHub/3_GitHub Pages.md>)
- [GitHub Actions](<GitHub/4_GitHub Actions.md>)
- [Projects](<GitHub/5_Projects.md>)
- [Discussions](<GitHub/6_Discussions.md>)
- [Codespaces](<GitHub/7_Codespaces.md>)
- [Code review](<GitHub/8_Code review.md>)

## Comando

- [Comandos Básicos do Git](<Comando/Básicos.md>)
- [Comandos Intermediários do Git](<Comando/Intermediario.md>)
- [Comandos Avançados do Git](<Comando/Avançado.md>)
