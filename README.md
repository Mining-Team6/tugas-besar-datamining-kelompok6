# tugas-besar-datamining-kelompok6

# Prediksi Keterlambatan Pengiriman Barang 

## Anggota Kelompok & NIM

1. Dewi Kresnawati (714220002)
2. Rania Ayuni Kartini Fitri (714220032)
3. Audyardha Nasywa Andini (714220020)

## Deskripsi Kasus

Proyek ini bertujuan untuk memprediksi apakah suatu pengiriman barang akan mengalami keterlambatan atau tidak berdasarkan data historis. Dengan mengetahui kemungkinan keterlambatan, perusahaan dapat mengambil tindakan proaktif untuk meningkatkan kepuasan pelanggan dan efisiensi operasional.

## Sumber Dataset

Dataset diambil dari [Github]([https://www.kaggle.com/](https://github.com/Abhi1727/FedEx-Logistics-Performance-Analysis/blob/main/SCMS_Delivery_History_Dataset.csv)) dengan judul *SCMS_Delivery_History_Dataset.csv*.  

## Langkah Preprocessing

- Menghapus nilai yang hilang (missing values)
- Drop kolom yang tidak relevan
- Konversi kolom seperti Weight dan Freight Cost ke format numerik (float) dan menangani error dengan errors='coerce'.
- Konversi tanggal & hitung Delivery Delay
- Membuat Kolom baru Delivery Delay (Selisih hari antara Scheduled Delivery Date dan Delivery to Client Date)
- Membuat Target Late: 1 jika pengiriman terlambat dan 0 jika tidak.
- Normalisasi fitur numerik dengan Min-Max Scaler

## Algoritma yang Digunakan

- Decision Tree 
- Random Forest
- HistGradient Boosting Classifier

## Evaluasi & Hasil

Model dievaluasi menggunakan beberapa metrik klasifikasi, yaitu: Akurasi, Precision, Recall, dan F1-score (mengacu pada nilai rata-rata macro). Berikut adalah hasil evaluasi dari ketiga algoritma yang digunakan:

| Algoritma                       | Akurasi | Precision | Recall | F1-score |
|--------------------------------|---------|-----------|--------|----------|
| Decision Tree                  | 91.14%  | 79%       | 72%    | 75%      |
| Random Forest                  | 91.77%  | 88%       | 66%    | 71%      |
| HistGradient Boosting Classifier | 89.54%  | 75%       | 60%    | 63%      |

📌 **Catatan:**
- **Decision Tree** memiliki akurasi tinggi dan performa seimbang antara kelas mayoritas dan minoritas.
- **Random Forest** sedikit lebih akurat, namun memiliki recall yang lebih rendah terhadap kelas minoritas.
- **HistGradient Boosting Classifier** memiliki akurasi yang baik, tetapi menunjukkan kinerja yang lebih rendah pada recall kelas minoritas.

Berdasarkan hasil di atas, **Random Forest** memiliki akurasi tertinggi, tetapi **Decision Tree** memberikan keseimbangan performa yang relatif lebih baik antar kelas.

## Cara Menjalankan

1. Clone repository ini:
   ```bash
   git clone https://github.com/namauser/namarepo.git
