from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator


def build_model():
    edges = [
        ("traveltime", "studytime"),
        ("traveltime", "absences_cat"),
        ("studytime", "G3_cat"),
        ("absences_cat", "G3_cat"),
        ("failures", "G3_cat"),
        ("Dalc", "health"),
        ("health", "G3_cat"),
    ]
    return BayesianNetwork(edges)


def fit_model(model, df):
    model.fit(df, estimator=MaximumLikelihoodEstimator)
    return model