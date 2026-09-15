import sys

from core import responder


def main():
    pergunta = " ".join(sys.argv[1:]).strip() or input("Pergunta: ")
    resposta, fontes = responder(pergunta)
    print(resposta)
    print("\nFontes:")
    for f in fontes:
        print(f"- {f}")


if __name__ == "__main__":
    main()
