"""
data_loader.py

Module ini digunakan untuk memuat dataset pengiriman dari direktori data/,
baik dari folder raw maupun processed, untuk keperluan prediksi keterlambatan pengiriman barang.
"""

import pandas as pd
import os

# Path direktori relatif
RAW_DATA_PATH = "data/raw/"
PROCESSED_DATA_PATH = "data/processed/"

def load_csv(filename, processed=False):
    """
    Memuat file CSV dari folder data.

    Parameters:
        filename (str): Nama file (contoh: 'shipment_data.csv')
        processed (bool): Jika True, load dari folder processed, jika False dari raw.

    Returns:
        pd.DataFrame: Dataframe dari file CSV
    """
    folder = PROCESSED_DATA_PATH if processed else RAW_DATA_PATH
    file_path = os.path.join(folder, filename)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File tidak ditemukan: {file_path}")

    df = pd.read_csv(file_path)
    return df

def validate_columns(df, required_columns):
    """
    Memeriksa apakah dataframe memiliki semua kolom yang dibutuhkan.

    Parameters:
        df (pd.DataFrame): Dataframe yang akan dicek
        required_columns (list): Daftar kolom yang wajib ada

    Raises:
        ValueError: Jika ada kolom yang hilang
    """
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Kolom berikut hilang dari dataset: {missing_cols}")

def preview_data(df, rows=5):
    """
    Menampilkan pratinjau awal dari dataframe.

    Parameters:
        df (pd.DataFrame): Dataframe yang akan ditampilkan
        rows (int): Jumlah baris untuk ditampilkan
    """
    print(df.head(rows))

def data_summary(df):
    """
    Menampilkan ringkasan statistik dasar dan info dataframe.

    Parameters:
        df (pd.DataFrame): Dataframe yang akan diringkas
    """
    print("Informasi DataFrame:")
    print(df.info())
    print("\nStatistik Deskriptif:")
    print(df.describe(include='all'))


# Contoh pemanggilan langsung (hapus saat produksi)
if __name__ == "__main__":
    try:
        df = load_csv("shipment_data.csv", processed=False)
        validate_columns(df, ["shipment_id", "delivery_date", "estimated_delivery_date", "late"])
        preview_data(df)
        data_summary(df)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
