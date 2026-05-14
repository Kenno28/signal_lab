


def split_time_series_data(df, test_size=0.2):
    """Splits the time series data into training and testing sets chronologically."""


    # Time split the data
    split_index = int(len(df) * (1 - test_size))
    train = df.iloc[:split_index]
    test = df.iloc[split_index:]

    X_train = train.drop(columns=["target"])
    y_train = train["target"]
    X_test = test.drop(columns=["target"])
    y_test = test["target"]

    return X_train, X_test, y_train, y_test
    
