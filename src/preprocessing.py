def bin_absences(x):
    if x <= 2:
        return "low"
    elif x <= 6:
        return "medium"
    else:
        return "high"


def bin_g3(x):
    if x <= 9:
        return "low"
    elif x <= 13:
        return "medium"
    else:
        return "high"


def preprocess_bn_data(df):
    df = df.copy()

    df["absences_cat"] = df["absences"].apply(bin_absences)
    df["G3_cat"] = df["G3"].apply(bin_g3)

    df_model = df[
        ["traveltime", "studytime", "absences_cat", "failures", "Dalc", "health", "G3_cat"]
    ].copy()

    # convert to string
    for col in df_model.columns:
        df_model[col] = df_model[col].astype(str)

    return df_model