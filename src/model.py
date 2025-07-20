# src/model.py

"""
model.py

Modul ini digunakan untuk melatih dan mengevaluasi model Machine Learning
dalam konteks prediksi keterlambatan pengiriman barang.
"""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

def split_data(df, target_column, test_size=0.2, random_state=42):
    """
    Memisahkan fitur dan target, lalu membagi data menjadi data latih dan data uji.

    Parameters:
        df (pd.DataFrame): Dataset lengkap
        target_column (str): Nama kolom target (misal: 'Late_delivery')
        test_size (float): Proporsi data uji
        random_state (int): Seed random

    Returns:
        X_train, X_test, y_train, y_test
    """
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def train_model(X, y):
    """
    Melatih model klasifikasi (default: Random Forest) dan membagi data otomatis.

    Parameters:
        X: Fitur (dataframe)
        y: Target (series)

    Returns:
        model terlatih, y_test, y_pred
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    return model, y_test, y_pred

def evaluate_model(model, X_test, y_test):
    """
    Mengevaluasi performa model pada data uji.

    Parameters:
        model: Model terlatih
        X_test: Fitur data uji
        y_test: Target data uji

    Returns:
        None (print hasil evaluasi)
    """
    y_pred = model.predict(X_test)
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
