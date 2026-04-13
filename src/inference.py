from pgmpy.inference import VariableElimination


def create_inference(model):
    return VariableElimination(model)


def query(infer, variable, evidence):
    q = infer.query(variables=[variable], evidence=evidence)
    print(f"\nQuery: P({variable} | {evidence})")
    print(q)
    return q