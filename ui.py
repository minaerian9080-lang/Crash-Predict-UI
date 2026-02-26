import streamlit as st
import train
import train_rnn
import pandas as pd

st.title("Crash Predictor - RNN Simulation")

# اختيار النموذج
selected_model = st.sidebar.selectbox("Choose Model", ["Average Model", "RNN Model"])

if st.button("Predict Next Game"):

    # التنبؤ حسب النموذج
    if selected_model == "Average Model":
        predicted_multiplier = train.predict_next_event()
    else:
        predicted_multiplier = train_rnn.predict_rnn()

    st.subheader("Predicted Multiplier of Next Game")
    st.metric("Prediction", predicted_multiplier)

    # عرض آخر لعبة
    try:
        df = pd.read_csv('data.csv')
        last_game = df.iloc[-1]
        st.subheader("Last Game Data")
        st.metric("Total Payout", last_game.get("payout", "N/A"))
        st.metric("Game Multiplier", last_game.get("ticket", "N/A"))
        st.metric("Number of Bets", last_game.get("numberOfBets", "N/A"))
        st.text(f"Game ID: {last_game.get('id', 'N/A')}")
        st.text(f"Server Seed: {last_game.get('serverSeed', 'N/A')}")
        st.text(f"Started At: {last_game.get('startedAt', 'N/A')}")
        st.text(f"End Time: {last_game.get('endTime', 'N/A')}")
    except Exception as e:
        st.write("No previous game data found.")
