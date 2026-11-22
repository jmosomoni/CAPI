"""Point d'entrée : python main.py [chemin/vers/backlog.json]"""
import sys

from capi.console import main

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (KeyboardInterrupt, EOFError):
        print("\nPartie interrompue.")
        sys.exit(1)
