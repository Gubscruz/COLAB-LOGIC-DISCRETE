from flloat.parser.ltlf import LTLfParser

def F(formula):
    parser = LTLfParser()
    formula = f"F ({formula})"
    parsed_formula = parser(formula)
    dfa = parsed_formula.to_automaton()
    graph = dfa.to_graphviz()
    print(graph)

F("(fi | psi) <-> (rho U fi)")