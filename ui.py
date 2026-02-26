import streamlit as st
import fetch
import train

st.set_page_config(page_title="Crash Analysis System", layout="centered")

st.title("Crash Game Analysis System")

# -------------------------------
# Display Last Game Data
# -------------------------------

def load_game_data():
    data = fetch.main()

    st.subheader("Last Game Data")

    st.metric("Total Payout", data.get("payout", "N/A"))
    st.metric("Game Multiplier", data.get("ticket", "N/A"))
    st.metric("Number of Bets", data.get("numberOfBets", "N/A"))

    st.text(f"Game ID: {data.get('game_id', 'N/A')}")
    st.text(f"Server Seed: {data.get('serverSeed', 'N/A')}")
    st.text(f"Started At: {data.get('startedAt', 'N/A')}")
    st.text(f"End Time: {data.get('endTime', 'N/A')}")

# -------------------------------
# Analysis Button
# -------------------------------

if st.button("Analyze Next Game"):

    load_game_data()

    result = train.predict_next_event()

    st.subheader("Crash Analysis (Last 20 Games)")

    st.metric("Average Multiplier", result["average"])
    st.metric("Probability >= 2x", f'{result["prob_2x"]}%')
    st.metric("Suggested Safe Exit", result["suggested_exit"])

    st.write(f"### Risk Level: {result['risk']}")

else:
    load_game_data()
