---
titulo: Codespaces
tipo: conceito
nivel: intermediario
categoria: GitHub
tags: [github, codespaces, ambiente, devcontainer, nuvem, vscode]
resumo: "Como usar GitHub Codespaces para desenvolvimento na nuvem, devcontainer, vantagens e limites."
relacionados: ["GitHub Actions", "Code review", "Aliases e configurações"]
fonte: https://docs.github.com/pt/codespaces
---

# Codespaces

## O que é?

**GitHub Codespaces** é um **ambiente de desenvolvimento na nuvem**. Ele cria uma máquina virtual com o repositório já clonado, ferramentas instaladas e um editor (VS Code no navegador ou desktop).

Assim, você programa sem depender da configuração da sua máquina local.

## Vantagens

- **Zero setup**: ambiente pronto em segundos.
- **Consistência**: todos usam o mesmo ambiente.
- **Acesso de qualquer lugar**: só precisa do navegador.
- **Isolamento**: não suja a máquina local.
- **Integração** com VS Code, extensões e terminal.

## Como criar

1. No repositório, clique em **Code → Codespaces → Create codespace**.
2. Aguarde o ambiente iniciar.
3. Edite, rode e faça commit pelo próprio editor.

Via CLI:

```bash
gh codespace create
gh codespace list
gh codespace ssh
gh codespace delete
```

## Configuração (devcontainer)

O ambiente é definido pelo arquivo:

```
.devcontainer/devcontainer.json
```

Exemplo:

```json
{
  "name": "Meu projeto",
  "image": "mcr.microsoft.com/devcontainers/javascript-node:20",
  "postCreateCommand": "npm install",
  "forwardPorts": [3000]
}
```

- Define imagem, ferramentas, comandos de setup e portas.
- Versionado no repositório, garantindo ambiente igual para todos.

## Limites e custos

- Há **limites de uso gratuito** por conta/plano.
- O ambiente consome horas de máquina; desligue quando não usar.
- Máquinas maiores consomem mais cota.

## Codespaces x ambiente local

| Característica | Codespaces | Local |
| --- | --- | --- |
| Setup | Automático | Manual |
| Consistência | Alta | Depende da máquina |
| Precisa de máquina potente | Não | Sim |
| Offline | Não | Sim |
| Custo | Cota/plano | Hardware próprio |

## Erros comuns

- **Esquecer de desligar** e consumir a cota.
- **Não usar devcontainer**, perdendo a padronização.
- **Guardar segredos** no repositório em vez de usar secrets.
- **Assumir que é ilimitado/gratuito** em todos os planos.

## Casos de uso

| Situação | Uso |
| --- | --- |
| Onboarding rápido | Codespace pronto |
| Contribuir sem configurar ambiente | Codespace |
| Desenvolver de máquina fraca | Codespace |
| Padronizar ambiente do time | `devcontainer.json` |
| Testar em ambiente limpo | Codespace |
