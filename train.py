import pandas as pd


def predict_next_event():
    """
    Analyze last 20 games and return:
    - average multiplier
    - probability of >= 2x
    - risk level
    - suggested safe exit
    """

    try:
        df = pd.read_csv("data.csv")
    except Exception as e:
        return {
            "average": 0,
            "prob_2x": 0,
            "risk": "Data file not found",
            "suggested_exit": 0
        }

    # Make sure ticket column exists
    if "ticket" not in df.columns:
        return {
            "average": 0,
            "prob_2x": 0,
            "risk": "Invalid data format",
            "suggested_exit": 0
        }

    # Need at least 20 games
    if len(df) < 20:
        return {
            "average": 0,
            "prob_2x": 0,
            "risk": "Not enough data",
            "suggested_exit": 0
        }

    # Convert ticket to multiplier (divide
