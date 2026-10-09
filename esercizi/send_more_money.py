import sys
from itertools import combinations
from pathlib import Path

# Consente a Python di trovare i moduli aipython situati nella cartella principale
sys.path.append(str(Path(__file__).resolve().parent.parent))

from cspConsistency import Search_with_AC_from_CSP
from cspProblem import CSP, Constraint
from searchGeneric import Searcher
from variable import Variable

# 1. Definizione delle variabili principali (lettere)
# S ed M non possono essere 0
S = Variable('S', range(1, 10))
M = Variable('M', range(1, 10))

E = Variable('E', range(10))
N = Variable('N', range(10))
D = Variable('D', range(10))
O = Variable('O', range(10))
R = Variable('R', range(10))
Y = Variable('Y', range(10))

# Variabili ausiliarie di riporto (Carry)
C1 = Variable('C1', [0, 1])
C2 = Variable('C2', [0, 1])
C3 = Variable('C3', [0, 1])
C4 = Variable('C4', [0, 1])

letter_vars = [S, E, N, D, M, O, R, Y]
all_vars = letter_vars + [C1, C2, C3, C4]

# 2. Vincoli di diversità (All-Different sulle lettere)
constraints = []
for v1, v2 in combinations(letter_vars, 2):
    constraints.append(
        Constraint([v1, v2], lambda val1, val2: val1 != val2, string=f"{v1}!={v2}")
    )

# 3. Vincoli aritmetici per colonna (da destra verso sinistra)
# Colonna 1 (unità): D + E = Y + 10 * C1
constraints.append(
    Constraint(
        [D, E, Y, C1],
        lambda d, e, y, c1: d + e == y + 10 * c1,
        string="D + E == Y + 10 * C1"
    )
)

# Colonna 2 (decine): C1 + N + R = E + 10 * C2
constraints.append(
    Constraint(
        [C1, N, R, E, C2],
        lambda c1, n, r, e, c2: c1 + n + r == e + 10 * c2,
        string="C1 + N + R == E + 10 * C2"
    )
)

# Colonna 3 (centinaia): C2 + E + O = N + 10 * C3
constraints.append(
    Constraint(
        [C2, E, O, N, C3],
        lambda c2, e, o, n, c3: c2 + e + o == n + 10 * c3,
        string="C2 + E + O == N + 10 * C3"
    )
)

# Colonna 4 (migliaia): C3 + S + M = O + 10 * C4
constraints.append(
    Constraint(
        [C3, S, M, O, C4],
        lambda c3, s, m, o, c4: c3 + s + m == o + 10 * c4,
        string="C3 + S + M == O + 10 * C4"
    )
)

# Colonna 5 (decine di migliaia): C4 = M
constraints.append(
    Constraint(
        [C4, M],
        lambda c4, m: c4 == m,
        string="C4 == M"
    )
)

# 4. Creazione dell'istanza CSP
csp_send = CSP(title="SEND+MORE=MONEY", variables=all_vars, constraints=constraints)

# 5. Risoluzione tramite Arc Consistency + Domain Splitting
print("=== Risoluzione SEND + MORE = MONEY ===")
searcher = Searcher(Search_with_AC_from_CSP(csp_send))
soluzione = searcher.search()

if soluzione:
    assegnazione = soluzione.end()
    print("Assegnazione trovata:")

    val = {}
    for v in letter_vars:
        v_val = assegnazione[v]
        valore = next(iter(v_val)) if isinstance(v_val, (set, list, tuple)) else v_val
        val[v.name] = valore
        print(f"  {v.name} = {valore}")

    send = 1000 * val['S'] + 100 * val['E'] + 10 * val['N'] + val['D']
    more = 1000 * val['M'] + 100 * val['O'] + 10 * val['R'] + val['E']
    money = 10000 * val['M'] + 1000 * val['O'] + 100 * val['N'] + 10 * val['E'] + val['Y']
    print(f"\nVerifica: {send} + {more} = {money}")
else:
    print("Nessuna soluzione trovata.")