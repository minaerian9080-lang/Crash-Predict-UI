import streamlit as st
import fetch

# Streamlit UI
st.title("Crash Predictor - Dummy Data Example")

# Select Model
selected_model = st.sidebar.selectbox("Choose Model", ["Crash CNN", "Crash RNN"])

# Function to display last game data
def load_game_data():
    x = fetch.main()  # Get game data
    
    st.subheader("Last Game Data")
    st.metric("Total Payout", x.get("payout", "N/A"))
    st.metric("Game Multiplier", x.get("ticket", "N/A")/100 if isinstance(x.get("ticket"), (int,float)) else x.get("ticket", "N/A"))
    st.metric("Number of Bets", x.get("numberOfBets", "N/A"))
    
    st.text(f"Game ID: {x.get('game_id', 'N/A')}")
    st.text(f"Server Seed: {x.get('serverSeed', 'N/A')}")
    st.text(f"Started At: {x.get('startedAt', 'N/A')}")
    st.text(f"End Time: {x.get('endTime', 'N/A')}")

# Function to simulate predictions
def get_model_prediction(model_name):
    st.subheader(f"Prediction ({model_name})")
    # Dummy prediction
    prediction = 2.5 if model_name == "Crash CNN" else 2.7
    st.metric("Predicted Multiplier", prediction)

# Predict Button
if st.button("Predict Next Game"):
    load_game_data()
    get_model_prediction(selected_model)
else:
    load_game_data()
