import sys
from pathlib import Path

# Consente a Python di trovare i moduli aipython situati nella cartella principale
sys.path.append(str(Path(__file__).resolve().parent.parent))

from searchExample import simp_delivery_graph
from searchMPP import SearcherMPP

# Inizializza il risolutore sul grafo di test
searcher = SearcherMPP(simp_delivery_graph)

# Trova il cammino verso il goal
path = searcher.search()

print("Cammino trovato:", path)