import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

def predict_rnn(sequence_length=10):
    try:
        # تحميل البيانات
        df = pd.read_csv('data.csv')
        if df.empty or len(df) < sequence_length:
            return 1.0

        # استخدم مضاعفات اللعبة السابقة
        multipliers = df['ticket'].values.reshape(-1,1)
        scaler = MinMaxScaler(feature_range=(0,1))
        scaled = scaler.fit_transform(multipliers)

        # إنشاء تسلسل
        X, y = [], []
        for i in range(sequence_length, len(scaled)):
            X.append(scaled[i-sequence_length:i, 0])
            y.append(scaled[i, 0])
        X, y = np.array(X), np.array(y)
        X = X.reshape((X.shape[0], X.shape[1], 1))

        # بناء نموذج RNN
        model = Sequential()
        model.add(LSTM(50, input_shape=(X.shape[1], 1)))
        model.add(Dense(1))
        model.compile(optimizer='adam', loss='mse')

        # تدريب سريع (للاختبار) - يمكنك زيادة epochs لاحقًا
        model.fit(X, y, epochs=10, batch_size=16, verbose=0)

        # توقع الجولة القادمة
        last_sequence = scaled[-sequence_length:].reshape(1, sequence_length, 1)
        prediction = model.predict(last_sequence, verbose=0)
        predicted_multiplier = scaler.inverse_transform(prediction)[0][0]

        return round(max(predicted_multiplier, 1.0), 2)
    except Exception as e:
        print("RNN Prediction error:", e)
        return 1.0
