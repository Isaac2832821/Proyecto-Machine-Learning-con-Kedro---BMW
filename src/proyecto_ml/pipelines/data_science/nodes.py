import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def split_data(df: pd.DataFrame, target_column: str, test_size: float, random_state: int):
    # Separar X e y
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Detectar columnas categóricas
    cat_cols = X.select_dtypes(include=["object"]).columns

    # One-hot encoding
    X = pd.get_dummies(X, columns=cat_cols, drop_first=True)

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.Series, model: dict):
    if model["type"] == "logistic_regression":
        clf = LogisticRegression(max_iter=model["max_iter"])
    else:
        raise ValueError(f"Modelo {model['type']} no soportado")

    clf.fit(X_train, y_train)
    return clf


def evaluate_model(model, X_test: pd.DataFrame, y_test: pd.Series):
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    return acc