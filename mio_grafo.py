from searchMPP import SearcherMPP
from searchProblem import Arc, Search_problem_from_explicit_graph

# 1. Definiamo i nodi del problema
citta = {'Bari', 'Bitonto', 'Molfetta', 'Bisceglie', 'Trani', 'Andria'}

# 2. Definiamo gli archi diretti e i rispettivi costi (es. distanze in km)
collegamenti = [
    Arc('Bari', 'Bitonto', cost=18),
    Arc('Bari', 'Molfetta', cost=25),
    Arc('Bitonto', 'Andria', cost=40),
    Arc('Molfetta', 'Bisceglie', cost=10),
    Arc('Bisceglie', 'Trani', cost=9),
    Arc('Trani', 'Andria', cost=13),
]

# 3. Definiamo una stima euristica h(n) per ciascun nodo verso l'obiettivo ('Andria')
# (es. stima in linea d'aria; per il goal è sempre 0)
stima_verso_andria = {
    'Bari': 50,
    'Bitonto': 35,
    'Molfetta': 28,
    'Bisceglie': 20,
    'Trani': 12,
    'Andria': 0,
}

# 4. Creiamo l'istanza del problema: partenza da Bari, destinazione Andria
problema_viaggio = Search_problem_from_explicit_graph(
    title="Viaggio verso Andria",
    nodes=citta,
    arcs=collegamenti,
    start='Bari',
    goals={'Andria'},
    hmap=stima_verso_andria
)

# 5. Risoluzione con A* (SearcherMPP con potatura dei cammini multipli)
print("=== Risoluzione con A* (SearcherMPP) ===")
risolutore = SearcherMPP(problema_viaggio)
percorso = risolutore.search()
print("Cammino finale:", percorso)