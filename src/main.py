from src.data_utils import load_student_data, select_features
from src.preprocessing import preprocess_bn_data
from src.bn_model import build_model, fit_model
from src.inference import create_inference, query
from src.causal import get_state_names, causal_query


def main():
    df = load_student_data("data/student-mat.csv")
    df = select_features(df)
    df = preprocess_bn_data(df)

    model = build_model()
    model = fit_model(model, df)

    infer = create_inference(model)

    # observational
    query(infer, "G3_cat", {"studytime": "4"})
    query(infer, "G3_cat", {"studytime": "1"})

    # causal
    state_map = get_state_names(df)

    causal_query(model, "studytime", "4", state_map)
    causal_query(model, "studytime", "1", state_map)


if __name__ == "__main__":
    main()