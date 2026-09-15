---
titulo: Repositório Local e Remoto
tipo: conceito
nivel: basico
categoria: Git
tags: [git, repositorio-local, repositorio-remoto, configuracao, ssh, token]
resumo: "Diferenças entre repositório local e remoto, principais plataformas, configuração de usuário e autenticação por SSH e token."
relacionados: ["Git e GitHub", "Sincronização (remote, fetch, pull, push)", "Aliases e configurações"]
fonte: https://git-scm.com/doc
---

# Repositório Local e Remoto

## O que é?

### Repositório
Repositório (ou "repo") é o local onde o Git armazena todo o histórico de um projeto: arquivos, commits, branches e configurações. Existem dois tipos principais: o **repositório local** e o **repositório remoto**.

### Repositório Local
É a cópia do repositório que fica **na sua máquina**. É onde você trabalha: cria e edita arquivos, faz commits e cria branches. Um repositório local é criado com `git init` ou obtido com `git clone`.

### Repositório Remoto
É a cópia do repositório hospedada em um **servidor** (na internet ou em outra máquina). Serve para compartilhar o projeto, fazer backup e sincronizar o trabalho entre várias pessoas. Normalmente é referenciado pelo nome `origin`.

## Quais as diferenças?

| Característica | Repositório Local | Repositório Remoto |
| --- | --- | --- |
| Onde fica | Na sua máquina | Em um servidor (nuvem) |
| Precisa de internet | Não | Sim, para sincronizar |
| Quem acessa | Você | Várias pessoas |
| Função | Trabalhar e commitar | Compartilhar e fazer backup |
| Como criar | `git init` ou `git clone` | Plataformas (GitHub, GitLab...) |
| Papel na sincronização | Origem do envio | Destino do `push` / origem do `pull` |

Na prática, o fluxo é:

1. Você trabalha e faz commits no **repositório local**.
2. Envia as alterações para o **repositório remoto** com `git push`.
3. Para trazer as alterações do remoto para o local, usa-se `git pull`.

## Quais os principais Repositórios Remotos?

- **GitHub**: plataforma mais popular, pertencente à Microsoft. Hospeda repositórios públicos e privados.
- **GitLab**: plataforma completa de DevOps, disponível na nuvem e para instalação própria (self-hosted).
- **Bitbucket**: da Atlassian, integrado a ferramentas como Jira e Trello.
- **Gitea / Gogs**: opções leves e de código aberto para hospedagem própria.
- **Azure DevOps Repos**: serviço da Microsoft integrado ao Azure DevOps.

O endereço de um repositório remoto pode ser:

- **HTTPS**: `https://github.com/usuario/repositorio.git`
- **SSH**: `git@github.com:usuario/repositorio.git`

## Configurações

As configurações do Git ficam em três níveis:

- **--system**: para todos os usuários da máquina.
- **--global**: para o seu usuário (o mais comum).
- **--local**: apenas para o repositório atual (tem prioridade sobre o global).

### Selecionar Usuário

Define o nome e o e-mail que serão gravados como autor dos commits:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

Verificar as configurações:

```bash
git config --list
git config --global --list
```

### Trocar Usuário

Para trocar o usuário global, basta rodar os comandos novamente com os novos dados:

```bash
git config --global user.name "Novo Nome"
git config --global user.email "novo@email.com"
```

Isso vale para os **próximos commits**. Os commits já feitos permanecem com o autor original.

### Troca Dinâmica de Usuário

É possível usar um usuário diferente em cada repositório, configurando no nível **local**:

```bash
git config --local user.name "Nome do Projeto"
git config --local user.email "projeto@email.com"
```

Assim, o repositório atual usa esse usuário e os demais continuam usando o global.

Outra forma é usar **condicionais de configuração** no arquivo `~/.gitconfig`, aplicando usuários diferentes conforme a pasta do repositório:

```ini
[includeIf "gitdir:~/trabalho/"]
    path = ~/.gitconfig-trabalho
[includeIf "gitdir:~/pessoal/"]
    path = ~/.gitconfig-pessoal
```

Cada arquivo incluído pode conter um `user.name` e um `user.email` próprios, aplicados automaticamente.

> **Importante**: `user.name` e `user.email` definem apenas o **autor dos commits** (metadado). Eles **não** definem com qual conta você se autentica no repositório remoto. A autenticação é feita por **chave SSH** ou por **token de acesso** (no caso de HTTPS).

## Autenticação com Chave SSH

Uma chave SSH permite autenticar no repositório remoto sem digitar senha a cada operação. É possível ter **várias chaves**, uma para cada conta (por exemplo, trabalho e pessoal).

### Gerar a chave

```bash
ssh-keygen -t ed25519 -C "seu@email.com"
```

- Gera dois arquivos em `~/.ssh/`: a chave **privada** (sem extensão) e a chave **pública** (`.pub`).
- A chave privada **nunca** deve ser compartilhada.
- É possível informar um nome diferente no prompt para ter chaves separadas, como `~/.ssh/id_trabalho` e `~/.ssh/id_pessoal`.

### Cadastrar a chave no servidor

Copie o conteúdo da chave pública (`.pub`) e cadastre na plataforma:

- **GitHub**: Settings → SSH and GPG keys → New SSH key.

Testar a conexão:

```bash
ssh -T git@github.com
```

### Usar chaves diferentes por conta

Crie (ou edite) o arquivo `~/.ssh/config`:

```ini
Host github-trabalho
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_trabalho
    IdentitiesOnly yes

Host github-pessoal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_pessoal
    IdentitiesOnly yes
```

Depois use o **alias** no endereço do remoto:

```bash
git remote add origin git@github-trabalho:usuario/repositorio.git
```

### Alternativa por repositório

Sem editar o `~/.ssh/config`, é possível apontar a chave apenas para um repositório:

```bash
git config --local core.sshCommand "ssh -i ~/.ssh/id_trabalho"
```

### Combinar SSH com a identidade dos commits

As duas coisas se complementam: a chave SSH define **quem autentica** no remoto, e o `includeIf`/config local define **quem assina** os commits. Exemplo completo para o cenário de trabalho:

```bash
# autenticação
git remote set-url origin git@github-trabalho:empresa/repo.git

# identidade dos commits
git config --local user.name "Seu Nome"
git config --local user.email "seu@empresa.com"
```

## Autenticação com Token (HTTPS)

No lugar da chave SSH, é possível autenticar via **HTTPS** usando um **token de acesso pessoal** (Personal Access Token - PAT) no lugar da senha.

### Por que usar token?

- Desde **2021** o GitHub **não aceita mais senha** para operações Git via HTTPS; é obrigatório usar um token.
- O token funciona como uma senha temporária, com **permissões** e **validade** definidas por você.
- Vantagem: configuração mais simples (não exige gerar chave) e pode ser restrito por escopo.

### Criar o token no GitHub

1. Settings → Developer settings → Personal access tokens.
2. Escolha **Tokens (classic)** ou **Fine-grained tokens**.
3. Defina descrição, validade e os escopos necessários (para repositórios, normalmente `repo`).
4. Copie o token gerado — ele **só aparece uma vez**.

### Usar o token

O endereço do remoto continua sendo HTTPS:

```bash
git remote add origin https://github.com/usuario/repositorio.git
```

Ao fazer `push` ou `pull`, o Git pede usuário e senha:

- **Usuário**: seu nome de usuário.
- **Senha**: cole o **token** (não a senha da conta).

Também é possível colocar o token direto na URL (não recomendado, pois fica visível):

```bash
git remote set-url origin https://usuario:TOKEN@github.com/usuario/repositorio.git
```

### Guardar o token (credential helper)

Para não digitar o token a cada operação, use um gerenciador de credenciais:

```bash
# guarda em cache por um tempo (em segundos)
git config --global credential.helper cache
git config --global credential.cacheTimeout 3600

# guarda permanentemente (Windows - Gerenciador de Credenciais)
git config --global credential.helper manager

# guarda permanentemente (Linux/macOS - arquivo em texto puro, menos seguro)
git config --global credential.helper store
```

### Trocar de usuário no HTTPS

Para usar contas diferentes, remova a credencial salva e informe o novo usuário/token:

```bash
# remove o helper configurado
git config --global --unset credential.helper

# no Windows, apague também a entrada no Gerenciador de Credenciais
```

E em cada repositório aponte o remoto com o usuário correto:

```bash
git remote set-url origin https://usuario-trabalho@github.com/empresa/repo.git
```

### SSH x Token HTTPS

| Característica | Chave SSH | Token HTTPS |
| --- | --- | --- |
| Como autentica | Par de chaves | Token no lugar da senha |
| Configuração | Gerar chave e cadastrar | Gerar token na plataforma |
| Validade | Não expira por padrão | Expira na data definida |
| Melhor para | Uso contínuo, várias máquinas | Acesso rápido e pontual |

## Erros comuns

- **Confundir repositório local com remoto**: um fica na máquina, o outro no servidor.
- **Achar que `commit` envia para o GitHub**: é preciso `push`.
- **Configurar usuário global quando queria só em um repositório** (ou vice-versa).
- **Colocar o token na URL e vazá-lo**.
- **Trocar name/email e esperar trocar a conta**: isso não altera a autenticação.
- **Esquecer de cadastrar a chave pública** no servidor.

## Casos de uso

| Situação | Comando/config |
| --- | --- |
| Definir identidade global | `git config --global user.name/email` |
| Usar identidade diferente em um projeto | `git config --local user.name/email` |
| Várias contas na mesma máquina | `~/.ssh/config` + aliases |
| Autenticar sem digitar senha | chave SSH |
| Autenticar via HTTPS | token de acesso |
