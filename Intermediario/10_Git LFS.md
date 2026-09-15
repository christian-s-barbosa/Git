---
titulo: Git LFS
tipo: comando
nivel: intermediario
categoria: Git
tags: [git, lfs, large-file-storage, arquivos-grandes, binarios]
resumo: "Como versionar arquivos grandes com Git LFS, instalar, rastrear tipos de arquivo e migrar o histórico."
relacionados: [".gitattributes", "Monorepo e polyrepo", "Internos a fundo (packfiles e gc)"]
fonte: https://git-lfs.com
---

# Git LFS

## O que é?

**Git LFS** (Large File Storage) é uma **extensão do Git** para versionar **arquivos grandes** (imagens, vídeos, áudios, modelos, binários). Em vez de guardar o arquivo inteiro no histórico, o Git guarda apenas um **ponteiro de texto** e o arquivo real fica em um servidor LFS.

## Como funciona?

Sem o LFS, cada versão de um arquivo grande é armazenada por completo no histórico, deixando o repositório enorme. Com o LFS:

- O repositório Git guarda um **ponteiro** (pequeno, em texto).
- O conteúdo real fica no **servidor LFS** e é baixado sob demanda.

```
versão 1 -> ponteiro -> arquivo real (servidor LFS)
versão 2 -> ponteiro -> arquivo real (servidor LFS)
```

## Instalar

```bash
# instala os hooks do LFS no usuário (uma vez)
git lfs install
```

> O Git LFS é um programa separado e precisa estar instalado na máquina.

## Rastrear arquivos

```bash
# rastreia todos os arquivos .psd
git lfs track "*.psd"

# rastreia uma pasta
git lfs track "assets/videos/*"
```

O comando cria/atualiza o arquivo **`.gitattributes`**, que **deve ser commitado**:

```bash
git add .gitattributes
git commit -m "Configura Git LFS para .psd"
```

Depois disso, os arquivos que casam com os padrões passam a ser versionados via LFS.

## Comandos

| Comando | Descrição |
| --- | --- |
| `git lfs install` | Ativa o LFS na máquina |
| `git lfs track "*.psd"` | Passa a rastrear um tipo de arquivo |
| `git lfs untrack "*.psd"` | Para de rastrear |
| `git lfs ls-files` | Lista os arquivos gerenciados pelo LFS |
| `git lfs pull` | Baixa os arquivos do LFS |
| `git lfs fetch` | Busca os arquivos sem aplicar |
| `git lfs migrate` | Converte arquivos já no histórico para LFS |

## Quando usar?

- Arquivos **grandes e binários** (imagens, vídeos, áudios, PDFs, datasets, modelos 3D).
- Quando o repositório fica **muito pesado** por causa desses arquivos.
- Projetos de jogos, design, dados e machine learning.

## Cuidados

- O LFS depende de um **servidor compatível** (GitHub, GitLab, Bitbucket e outros oferecem, com limites de armazenamento/tráfego).
- **Não** resolve arquivos que já estão no histórico: é preciso migrar (`git lfs migrate`).
- Nem todos os arquivos grandes precisam de LFS; para muitos casos, é melhor **não versioná-los** (usar `.gitignore`).

## Erros comuns

- **Rastrear um arquivo depois de já tê-lo commitado**: o histórico antigo continua pesado; é preciso migrar (`git lfs migrate`).
- **Esquecer de commitar o `.gitattributes`**, então o LFS não funciona para os outros.
- **Não instalar o LFS** e clonar um repositório que o usa, ficando com ponteiros em vez dos arquivos.
- **Estourar os limites** de armazenamento/tráfego do serviço.
- **Usar LFS para arquivos que deveriam ser ignorados** (builds, temporários).
- **Clonar sem LFS** e achar que os arquivos estão corrompidos.

## Casos de uso

| Cenário | Exemplo |
| --- | --- |
| Versionar imagens/vídeos em um projeto | `git lfs track "*.mp4"` |
| Guardar datasets de ML | LFS para `.csv`/`.parquet` grandes |
| Projetos de design (PSD, AI) | LFS para arquivos pesados |
| Assets de jogos | LFS para texturas/modelos |
| Migrar repositório pesado para LFS | `git lfs migrate import --include="*.psd"` |
