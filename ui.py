import streamlit as st
import pandas as pd
import fetch
import hash_multiplier
import train
import train_rnn

# Functions for prediction
def get_model_prediction_crashCNN():
    with st.spinner("Predicting with Crash CNN..."):
        hash_multiplier.main()
        prediction = train.predict_next_event()
        st.subheader(f"Prediction (Crash CNN): {prediction}")

def get_model_prediction_crashRNN():
    with st.spinner("Predicting with Crash RNN..."):
        prediction = train_rnn.predict_rnn()
        st.subheader(f"Prediction (Crash RNN): {prediction}")

# Function to display last game data
def load_game_data():
    x = fetch.main()
    payout = x.get("payout", "N/A")
    target = x.get("ticket", "N/A")
    numberOfBets = x.get("numberOfBets", "N/A")
    
    st.subheader("Last Game Data")
    st.metric("Total Payout", payout)
    st.metric("Game Multiplier", target/100 if isinstance(target, (int, float)) else target)
    st.metric("Number of Bets", numberOfBets)

# Streamlit UI
st.title("Crash Predictor - Simplified Version")

# Select model
selected_model = st.sidebar.selectbox("Choose Model", ["Crash CNN", "Crash RNN"])

# Predict button
if st.button("Predict Next Game"):
    load_game_data()
    if selected_model == "Crash CNN":
        get_model_prediction_crashCNN()
    else:
        get_model_prediction_crashRNN()
else:
    load_game_data()
