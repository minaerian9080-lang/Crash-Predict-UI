def predict_next_event():

    df = pd.read_csv('data.csv')

    if len(df) < 20:
        return {
            "average": 0,
            "prob_2x": 0,
            "risk": "Not enough data",
            "suggested_exit": 0
        }

    last_20 = df['ticket'].iloc[-20:] / 100

    average = round(last_20.mean(), 3)
    prob_2x = round((last_20 >= 2).mean() * 100, 2)

    # Risk logic
    if prob_2x > 60:
        risk = "Low"
        suggested_exit = 1.8
    elif prob_2x > 40:
        risk = "Medium"
        suggested_exit = 1.5
    else:
        risk = "High"
        suggested_exit = 1.2

    return {
        "average": average,
        "prob_2x": prob_2x,
        "risk": risk,
        "suggested_exit": suggested_exit
    }
