---
titulo: Assinatura de commits e tags
tipo: conceito
nivel: intermediario
categoria: Git
tags: [git, assinatura, gpg, ssh, signed-commits, seguranca, verified]
resumo: "Como assinar commits e tags com GPG ou SSH para garantir autenticidade e integridade, e verificar as assinaturas."
relacionados: ["git tag", "GitHub na prática (Fork, Pull Request e Issues)", "Repositório Local e Remoto"]
fonte: https://git-scm.com/book/pt-br/v2
---

# Assinatura de commits e tags

## O que é?

Assinar commits e tags significa adicionar uma **assinatura criptográfica** a eles, comprovando que foram criados por você e que **não foram alterados** depois. No GitHub, commits assinados aparecem com o selo **"Verified"**.

## Por que usar?

- **Autenticidade**: comprova a autoria real do commit.
- **Integridade**: garante que o conteúdo não foi modificado.
- **Confiança**: evita que alguém se passe por você (spoofing de autor).
- **Boas práticas**: exigido em muitos projetos sérios e pipelines.

## Assinatura com GPG

### 1. Gerar uma chave

```bash
gpg --full-generate-key
```

### 2. Listar a chave

```bash
gpg --list-secret-keys --keyid-format=long
```

### 3. Configurar a chave no Git

```bash
git config --global user.signingkey <ID_DA_CHAVE>
```

### 4. Assinar

```bash
# assinar um commit
git commit -S -m "Mensagem"

# assinar uma tag
git tag -s v1.0.0 -m "Versão 1.0.0"

# assinar todos os commits automaticamente
git config --global commit.gpgsign true
git config --global tag.gpgsign true
```

### 5. Verificar

```bash
git log --show-signature
git tag -v v1.0.0
```

### 6. Cadastrar no GitHub

Adicione a chave pública em **Settings → SSH and GPG keys → New GPG key**.

```bash
gpg --armor --export <ID_DA_CHAVE>
```

## Assinatura com SSH

Disponível a partir do **Git 2.34**, usando a mesma chave SSH.

```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub

# opcional: arquivo de signatários confiáveis
git config --global gpg.ssh.allowedSignersFile ~/.ssh/allowed_signers
```

No GitHub, a mesma chave SSH pode ser cadastrada como **signing key**.

## GPG x SSH

| Característica | GPG | SSH |
| --- | --- | --- |
| Reaproveita chave SSH | Não | Sim |
| Configuração | Mais complexa | Mais simples |
| Suporte | Universal | Git 2.34+ |
| Uso comum | Projetos tradicionais | Desenvolvedores com SSH |

## Erros comuns

- **Assinar sem cadastrar a chave no GitHub**, então não aparece como "Verified".
- **Esquecer `commit.gpgsign`** e assinar só alguns commits.
- **Chave GPG expirada** ou sem `user.signingkey` configurado.
- **Confundir a chave de assinatura com a de autenticação** (SSH).
- **Reescrever histórico assinado** e invalidar as assinaturas.

## Casos de uso

| Situação | Comando |
| --- | --- |
| Assinar um commit | `git commit -S -m "msg"` |
| Assinar uma release | `git tag -s v1.0.0 -m "msg"` |
| Assinar sempre | `commit.gpgsign true` |
| Verificar um commit | `git log --show-signature` |
| Verificar uma tag | `git tag -v v1.0.0` |
