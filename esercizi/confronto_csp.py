import sys
import time
from pathlib import Path

# Aggiunge la cartella radice a sys.path per trovare i moduli di aipython
sys.path.append(str(Path(__file__).resolve().parent.parent))

from cspConsistency import Search_with_AC_from_CSP
from cspExamples import csp1, csp2
from cspSearch import Search_from_CSP
from searchGeneric import AStarSearcher, Searcher


def benchmark_solver(nome, funzione_risolutiva):
    inizio = time.perf_counter()
    soluzione = funzione_risolutiva()
    durata = time.perf_counter() - inizio
    esito = "Sì" if soluzione is not None else "No"
    print(f"  [{nome:<32}] Risolto: {esito} | Tempo: {durata:.6f} s")


problemi = [
    ("Grafo Semplice (csp1)", csp1),
    ("Grafo Complesso con cicli (csp2)", csp2),
]

for nome_prob, prob in problemi:
    print("\n==========================================")
    print(f"Benchmark su: {nome_prob}")
    print("==========================================")

    # 1. Ricerca con cspSearch + A*
    def test_astar(p=prob):
        s = AStarSearcher(Search_from_CSP(p))
        return s.search()

    benchmark_solver("cspSearch (A*)", test_astar)

    # 2. Backtracking DFS su spazio stati CSP
    def test_dfs(p=prob):
        s = Searcher(Search_from_CSP(p))
        return s.search()

    benchmark_solver("cspSearch (Backtracking DFS)", test_dfs)

    # 3. GAC + Domain Splitting
    def test_gac(p=prob):
        s = Searcher(Search_with_AC_from_CSP(p))
        return s.search()

    benchmark_solver("cspConsistency (GAC + Split)", test_gac)