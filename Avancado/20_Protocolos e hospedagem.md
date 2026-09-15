---
titulo: Protocolos e hospedagem
tipo: conceito
nivel: avancado
categoria: Git
tags: [git, protocolos, ssh, https, git-daemon, hospedagem, remoto]
resumo: "Protocolos de transporte do Git (file, SSH, HTTPS, git) e as principais opções de hospedagem de repositórios."
relacionados: ["Repositório Local e Remoto", "Refspecs", "git bundle"]
fonte: https://git-scm.com/book/pt-br/v2
---

# Protocolos e hospedagem

## O que é?

O Git se comunica com repositórios remotos por **protocolos de transporte**. Conhecer as opções ajuda a escolher o mais adequado em segurança, velocidade e autenticação.

## Protocolos

| Protocolo | URL | Autenticação | Segurança | Observação |
| --- | --- | --- | --- | --- |
| **file** | `file:///caminho` | Nenhuma | Local | Acesso a disco/rede local |
| **SSH** | `git@host:repo.git` | Chave SSH | Alta | Mais usado para escrita |
| **HTTPS** | `https://host/repo.git` | Token/senha | Alta (TLS) | Fácil de atravessar firewalls |
| **git** | `git://host/repo.git` | Nenhuma | **Baixa** | Somente leitura, **não recomendado** |

### file
Acesso direto ao sistema de arquivos (mesma máquina ou pasta de rede).

### SSH
Autenticação por chave, criptografia forte e sem senha a cada operação. Ideal para **escrita**.

### HTTPS
Túnel TLS; autenticação por **token**. Bom para redes restritas e para quem não quer gerenciar chaves.

### git://
Protocolo anônimo, **sem autenticação e sem criptografia**. Hoje é pouco usado e considerado inseguro.

## git daemon

Servidor simples para publicar repositórios via protocolo `git://` (somente leitura).

```bash
git daemon --reuseaddr --base-path=/srv/git /srv/git
```

- Normalmente usado com `git://` para clones públicos.
- Prefira SSH/HTTPS para escrita.

## Hospedagem

| Serviço | Observação |
| --- | --- |
| **GitHub** | Mais popular, da Microsoft |
| **GitLab** | DevOps completo, self-hosted disponível |
| **Bitbucket** | Da Atlassian, integra Jira |
| **Gitea / Gogs** | Leves, open source, self-hosted |
| **Azure DevOps Repos** | Integrado ao Azure DevOps |

- **Self-hosted**: você mesmo hospeda (mais controle, mais manutenção).
- **Cloud**: serviço gerenciado (menos manutenção).

## Escolhendo o protocolo

- **Escrita**: SSH (recomendado) ou HTTPS com token.
- **Leitura pública**: HTTPS.
- **Rede restritiva**: HTTPS (porta 443).
- **Sem autenticação**: evite `git://`.

## Erros comuns

- **Usar `git://`** pensando que é seguro (não tem criptografia).
- **Compartilhar token na URL** e vazá-lo.
- **Esquecer de configurar a chave SSH** e não entender a falha de autenticação.
- **Confundir protocolo com serviço de hospedagem**: são coisas diferentes.

## Casos de uso

| Situação | Protocolo/serviço |
| --- | --- |
| Escrever com segurança | SSH |
| Atravessar firewall corporativo | HTTPS |
| Repositório público interno | HTTPS ou `git://` (com cautela) |
| Controle total do servidor | Self-hosted (GitLab/Gitea) |
| Menos manutenção | Cloud (GitHub/GitLab) |
