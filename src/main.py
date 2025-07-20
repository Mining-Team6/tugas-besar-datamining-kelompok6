# src/main.py

"""
Main pipeline for Data Mining project: Prediksi Keterlambatan Pengiriman Barang.
Langkah-langkah:
1. Load raw data
2. Preprocessing sederhana
3. Train model
4. Evaluasi model
"""

from data_loader import load_csv
from model import train_model, evaluate_model
from utils import print_classification_report, plot_confusion_matrix

def main():
    # 1. Load data
    try:
        df = load_csv("SCMS_Delivery_History_Dataset.csv", processed=False)  # Sesuaikan nama file mentah
    except FileNotFoundError:
        print("Dataset tidak ditemukan.")
        return

    # 2. Preprocessing sederhana
    df = df.dropna()

    if "Late_delivery" not in df.columns:
        print("Kolom target 'Late_delivery' tidak ditemukan dalam dataset.")
        return

    X = df.drop("Late_delivery", axis=1)
    y = df["Late_delivery"]

    # 3. Train & predict
    model, y_test, y_pred = train_model(X, y)

    # 4. Evaluasi
    print_classification_report(y_test, y_pred)
    plot_confusion_matrix(y_test, y_pred)

# Pemanggilan utama
if __name__ == "__main__":
    main()
