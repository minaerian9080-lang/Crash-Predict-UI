def predict_next_event():

    df = pd.read_csv('data.csv')

    features = df[['endTime', 'ticket', 'startedAt', 'numberOfBets', 'payout', 'hash_result']]
    target = df['ticket']

    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
        layers.Dense(32, activation='relu'),
        layers.Dense(1)
    ])

    model.compile(optimizer='adam', loss='mean_squared_error')

    model.fit(X_train_scaled, y_train, epochs=30, batch_size=64, verbose=0)

    # 🔥 Predict using latest game
    latest_row = features.iloc[-1:].values
    latest_row_scaled = scaler.transform(latest_row)

    predicted_difference = model.predict(latest_row_scaled, verbose=0)[0][0]

    predicted_ticket = df['hash_result'].iloc[-1] + predicted_difference

    return float(predicted_ticket / 100)
