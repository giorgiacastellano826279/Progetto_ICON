from cspConsistency import Search_with_AC_from_CSP
from cspProblem import CSP, Constraint
from searchGeneric import Searcher
from variable import Variable

# Esempio: Clausola (A or not B) and (not A or C) and (B or C)
# 1. Definizione delle variabili proposizionali con dominio {True, False}
A = Variable('A', [True, False])
B = Variable('B', [True, False])
C = Variable('C', [True, False])

# 2. Definizione delle clausole come vincoli
# Clausola 1: A or not B
c1 = Constraint([A, B], lambda a, b: a or (not b), string="A or not B")

# Clausola 2: not A or C
c2 = Constraint([A, C], lambda a, c: (not a) or c, string="not A or C")

# Clausola 3: B or C
c3 = Constraint([B, C], lambda b, c: b or c, string="B or C")

# 3. Creazione del problema SAT come CSP
sat_csp = CSP(title="Test SAT Formula", variables=[A, B, C], constraints=[c1, c2, c3])

# 4. Risoluzione tramite Arc Consistency + Domain Splitting (analogo a DPLL)
print("=== Risoluzione SAT con aipython ===")
searcher = Searcher(Search_with_AC_from_CSP(sat_csp))
soluzione = searcher.search()

if soluzione:
    assegnazione = soluzione.end()
    print("Formula SODDISFACIBILE (SAT)!")
    print("Modello trovato:")
    for var in [A, B, C]:
        val = assegnazione[var]
        valore = next(iter(val)) if isinstance(val, (set, list, tuple)) else val
        print(f"  {var.name} = {valore}")
else:
    print("Formula INSODDISFACIBILE (UNSAT)!")