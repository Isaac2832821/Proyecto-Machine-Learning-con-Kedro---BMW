import pandas as pd


def limpiar_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Limpieza básica para dataset de ventas BMW"""
    df = df.drop_duplicates()
    df = df.dropna()
    return df


def limpiar_classification(df: pd.DataFrame) -> pd.DataFrame:
    """Limpieza básica para dataset de clasificación BMW"""
    df = df.drop_duplicates()
    df = df.dropna()
    return df


def limpiar_used(df: pd.DataFrame) -> pd.DataFrame:
    """Limpieza básica para dataset de autos usados BMW"""
    df = df.drop_duplicates()
    df = df.dropna()
    return df