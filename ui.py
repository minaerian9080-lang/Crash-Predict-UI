import streamlit as st
import streamlit_shadcn_ui as ui
import pandas as pd
import fetch
import hash_multiplier
import train
import train_rnn


def get_model_prediction_crashCNN():

    with st.spinner():
        hash_multiplier.main()
        prediction = train.predict_next_event()

        st.title(prediction)


def get_model_prediction_crashRNN():

    with st.spinner():
        prediction = train_rnn.predict_rnn()

        st.title(prediction)
        

def laod_game_data():

    
    



        












