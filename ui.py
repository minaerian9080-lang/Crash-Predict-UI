import streamlit as st
import pandas as pd
import fetch
import hash_multiplier
import train
import train_rnn

# --- Functions for predictions ---
def get_model_prediction_crashCNN():
    with st.spinner("Predicting with Crash CNN..."):
        hash_multiplier.main()
        prediction = train.predict_next_event()
        st.subheader(f"Prediction (Crash CNN): {prediction}")

def get_model_prediction_crashRNN():
    with st.spinner("Predicting with Crash RNN..."):
        prediction = train_rnn.predict_rnn()
        st.subheader(f"Prediction (Crash RNN): {prediction}")

# --- Function to display last game data ---
def load_game_data():
    data = fetch.main()  # safe fetch; returns dummy if failed

    payout = data.get("payout", 0)
    ticket = data.get("ticket", 0)
    numberOfBets = data.get("numberOfBets", 0)
    startedAt = data.get("startedAt", "N/A")
    serverSeed = data.get("serverSeed", "N/A")
    game_id = data.get("id", "N/A")
    endTime = data.get("endTime", "N/A")

    st.subheader("Last Game Data")
    st.metric("Total Payout", payout)
    st.metric("Game Multiplier", ticket/100 if isinstance(ticket, (int, float)) else ticket)
    st.metric("Number of Bets", numberOfBets)
    st.text(f"Game ID: {game_id}")
    st.text(f"Server Seed: {serverSeed}")
    st.text(f"Started At: {startedAt}")
    st.text(f"End Time: {endTime}")

# --- Streamlit UI ---
st.title("Crash Predictor - Safe Version")

# Sidebar: select model
selected_model = st.sidebar.selectbox("Choose Model", ["Crash CNN", "Crash RNN"])

# Button: predict next game
if st.button("Predict Next Game"):
    load_game_data()
    
