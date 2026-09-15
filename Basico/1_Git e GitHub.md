---
titulo: Git e GitHub
tipo: conceito
nivel: basico
categoria: Git
tags: [git, github, controle-de-versao, instalacao]
resumo: "Conceito de Git e GitHub, como funcionam, por que usar, quem criou e instalação no Windows e Linux."
relacionados: ["Repositório Local e Remoto", "Git commit", "GitHub na prática (Fork, Pull Request e Issues)"]
fonte: https://git-scm.com/doc
---

# Git e GitHub

## O que é?

### Git
Git é um **sistema de controle de versão distribuído** (DVCS - Distributed Version Control System). Ele rastreia e registra o histórico de alterações de arquivos ao longo do tempo, permitindo voltar a versões anteriores e desenvolver várias linhas de trabalho em paralelo.

O Git é um software que roda **na sua máquina** (local) e não precisa de internet para funcionar. Cada cópia de um repositório Git contém todo o histórico do projeto.

### GitHub
GitHub é uma **plataforma de hospedagem de repositórios Git na nuvem** e também uma rede de colaboração para desenvolvedores. Ele permite armazenar código, trabalhar em equipe, revisar alterações, abrir issues e automatizar tarefas.

**Git não é a mesma coisa que GitHub:**
- **Git** é a ferramenta de controle de versão.
- **GitHub** é um serviço online que hospeda repositórios Git.
- Existem outras plataformas além do GitHub, como GitLab e Bitbucket.

## Como funciona?

O Git organiza o trabalho em três áreas principais:

1. **Diretório de trabalho (Working Directory)**: onde os arquivos são criados e editados.
2. **Área de preparação (Staging Area / Index)**: onde se seleciona o que vai entrar no próximo commit.
3. **Repositório (Repository)**: onde os commits ficam gravados permanentemente no histórico.

Fluxo básico:

```
Working Directory  --git add-->  Staging Area  --git commit-->  Repository
```

Pontos importantes:

- Cada alteração salva gera um **commit**, identificado por um código único (hash).
- O conjunto de commits forma um **histórico** em forma de linha do tempo.
- Como o Git é **distribuído**, cada pessoa tem uma cópia completa do repositório e pode trabalhar offline, sincronizando depois com um repositório remoto.
- O Git guarda **snapshots** (fotos) do projeto a cada commit, não apenas as diferenças.

## Por quê usar?

- **Histórico completo**: registra todas as alterações e permite voltar atrás quando necessário.
- **Trabalho em equipe**: várias pessoas podem trabalhar no mesmo projeto sem sobrescrever o trabalho umas das outras.
- **Branches (ramificações)**: permite desenvolver funcionalidades isoladas e depois uni-las.
- **Integridade**: cada commit tem um identificador único, o que garante a confiabilidade do histórico.
- **Distribuído**: funciona sem internet e não depende de um único servidor central.
- **Padrão de mercado**: é a ferramenta de controle de versão mais usada no mundo.

## Quem criou?

- **Git** foi criado por **Linus Torvalds** (criador do kernel Linux) em **2005**, para substituir a ferramenta BitKeeper, que deixou de ser gratuita para o projeto Linux.
- O nome "Git" é uma gíria britânica que significa "pessoa desagradável".
- O **GitHub** foi fundado em **2008** por Tom Preston-Werner, Chris Wanstrath, P. J. Hyett e Scott Chacon.
- Em **2018**, o GitHub foi comprado pela **Microsoft**.

## Como instalar

### Windows

1. Acesse o site oficial: https://git-scm.com/download/win
2. Baixe o instalador (Git for Windows).
3. Execute o instalador e avance com as opções padrão (Next).
4. Recomenda-se manter as opções "Git Bash Here" e "Git from the command line".
5. Verifique a instalação abrindo o **Git Bash** ou o **Prompt de Comando** e digitando:

```bash
git --version
```

Alternativas por gerenciador de pacotes:

```bash
# winget
winget install --id Git.Git -e --source winget

# Chocolatey
choco install git
```

### Linux

**Debian / Ubuntu:**

```bash
sudo apt update
sudo apt install git
```

**Fedora:**

```bash
sudo dnf install git
```

**Arch Linux:**

```bash
sudo pacman -S git
```

**Verificar a instalação (qualquer distribuição):**

```bash
git --version
```

## Erros comuns

- **Confundir Git com GitHub**: Git é a ferramenta de controle de versão; GitHub é um serviço de hospedagem.
- **Achar que precisa de internet** para usar o Git: o Git funciona localmente.
- **Não verificar a instalação** com `git --version` após instalar.
- **Esquecer de configurar `user.name` e `user.email`** antes do primeiro commit.
- **Pensar que o GitHub é o único serviço**: existem GitLab, Bitbucket, etc.

## Casos de uso

| Situação | Uso |
| --- | --- |
| Guardar o histórico de um projeto pessoal | Git local |
| Compartilhar código com a equipe | Git + GitHub |
| Contribuir com projetos open source | Git + fork/PR |
| Fazer backup do código | Repositório remoto |
| Trabalhar offline e sincronizar depois | Git distribuído |
