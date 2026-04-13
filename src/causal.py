from copy import deepcopy
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


def get_state_names(df):
    return {col: sorted(df[col].unique()) for col in df.columns}


def intervene(model, variable, fixed_state, state_map):
    m = deepcopy(model)

    # remove incoming edges
    parents = list(m.get_parents(variable))
    for p in parents:
        m.remove_edge(p, variable)

    m.remove_cpds(variable)

    states = state_map[variable]
    probs = [[1.0 if s == fixed_state else 0.0] for s in states]

    new_cpd = TabularCPD(
        variable=variable,
        variable_card=len(states),
        values=probs,
        state_names={variable: states},
    )

    m.add_cpds(new_cpd)
    return m


def causal_query(model, variable, target, state_map):
    m = intervene(model, variable, target, state_map)
    infer = VariableElimination(m)

    q = infer.query(variables=["G3_cat"])
    print(f"\nCausal Query: P(G3_cat | do({variable}={target}))")
    print(q)

    return q