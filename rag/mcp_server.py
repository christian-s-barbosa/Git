from mcp.server.mcpserver import MCPServer

from core import buscar, responder

mcp = MCPServer("git-rag")


@mcp.tool()
def buscar_git(query: str, nivel: str = "", categoria: str = "") -> str:
    """Busca trechos relevantes na base de conhecimento de Git.

    Args:
        query: a busca em linguagem natural (ex.: "como desfazer o último commit").
        nivel: filtra por nível (basico, intermediario, avancado) - opcional.
        categoria: filtra por categoria (Git, GitHub) - opcional.
    """
    trechos = buscar(query, nivel=nivel or None, categoria=categoria or None)
    if not trechos:
        return "Nenhum trecho encontrado."
    return "\n\n".join(f"### {t['meta']['arquivo']}\n{t['texto']}" for t in trechos)


@mcp.tool()
def responder_git(query: str, nivel: str = "", categoria: str = "") -> str:
    """Responde uma pergunta sobre Git usando a base (RAG) e o DeepSeek.

    Args:
        query: a pergunta sobre Git.
        nivel: filtra por nível (basico, intermediario, avancado) - opcional.
        categoria: filtra por categoria (Git, GitHub) - opcional.
    """
    resposta, fontes = responder(query, nivel=nivel or None, categoria=categoria or None)
    return f"{resposta}\n\nFontes:\n" + "\n".join(f"- {f}" for f in fontes)


if __name__ == "__main__":
    mcp.run()
