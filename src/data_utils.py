import pandas as pd

def load_student_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path, sep=";")


def select_features(df: pd.DataFrame) -> pd.DataFrame:
    cols = [
        "traveltime",
        "studytime",
        "absences",
        "failures",
        "Dalc",
        "health",
        "G3",
    ]
    return df[cols].copy()