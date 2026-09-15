---
titulo: git submodules
tipo: comando
nivel: intermediario
categoria: Git
tags: [git, submodule, submódulo, submodulos, dependencias]
resumo: "O que são submodules, como adicionar, clonar, atualizar e remover, e a comparação com alternativas."
relacionados: ["git subtree", "Monorepo e polyrepo", "Refspecs"]
fonte: https://git-scm.com/docs/git-submodule
---

# git submodules

## O que é?

Um **submodule** (submódulo) é um **repositório Git dentro de outro repositório**. Ele permite incluir um projeto externo em uma pasta específica, mantendo-o como um repositório independente, com seu próprio histórico.

O repositório principal **não guarda** os arquivos do submodule: ele guarda apenas um **ponteiro para um commit específico** dele.

## Como funciona?

- A configuração fica no arquivo **`.gitmodules`** (versionado).
- O repositório principal registra **qual commit** do submodule deve ser usado.
- Os arquivos do submodule ficam em uma pasta própria, mas com histórico separado.

```
projeto/
├── .gitmodules
└── libs/
    └── biblioteca/     <- submodule (repositório próprio)
```

## Adicionar um submodule

```bash
git submodule add https://github.com/usuario/biblioteca.git libs/biblioteca
git commit -m "Adiciona submodule biblioteca"
```

Isso cria/atualiza o `.gitmodules` e registra o commit atual do submodule.

## Clonar um repositório com submodules

```bash
# opção 1: clonar já baixando os submodules
git clone --recurse-submodules <url>

# opção 2: clonar e depois inicializar
git clone <url>
cd projeto
git submodule update --init --recursive
```

## Atualizar submodules

```bash
# atualiza para o commit registrado no repositório principal
git submodule update

# atualiza para a versão mais recente da branch remota
git submodule update --remote

# inicializa e atualiza (incluindo aninhados)
git submodule update --init --recursive
```

Após atualizar, é preciso **commitar o novo ponteiro** no repositório principal.

## Listar e remover

```bash
# lista os submodules
git submodule status

# remove um submodule
git submodule deinit libs/biblioteca
git rm libs/biblioteca
rm -rf .git/modules/libs/biblioteca
```

## Vantagens e desvantagens

| Vantagens | Desvantagens |
| --- | --- |
| Mantém o histórico separado | Fácil de esquecer de atualizar |
| Reutiliza um projeto em vários lugares | Comandos extras no clone/update |
| Fixa uma versão específica | Fluxo mais complexo para iniciantes |

## Alternativas

- **git subtree**: incorpora o projeto ao histórico do repositório principal.
- **Gerenciador de pacotes** (npm, pip, Maven...): preferível para dependências de código.
- **Monorepo**: tudo em um único repositório.

## Boas práticas

- Use submodules quando precisar de um **repositório externo** com versionamento próprio.
- Prefira gerenciadores de pacotes para dependências comuns.
- Sempre rode `git submodule update --init --recursive` após clonar/puxar.

## Erros comuns

- **Esquecer `git submodule update --init --recursive`** após clonar, ficando com pastas vazias.
- **Alterar o submodule e não commitar o novo ponteiro** no repositório principal.
- **Confundir o commit do submodule com o do projeto principal** (são repositórios separados).
- **Usar submodule para dependências comuns**, quando um gerenciador de pacotes seria melhor.
- **Editar arquivos do submodule sem entender** que o histórico é separado.
- **Não versionar o `.gitmodules`**.

## Casos de uso

| Cenário | Exemplo |
| --- | --- |
| Reutilizar uma biblioteca interna em vários projetos | submodule apontando para o repo da lib |
| Incluir tema/plugin externo versionado | submodule do tema |
| Compartilhar documentação entre repositórios | submodule de docs |
| Fixar uma versão específica de um projeto externo | ponteiro para um commit |
