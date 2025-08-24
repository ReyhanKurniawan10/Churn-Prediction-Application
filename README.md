# Porto3 - Churn Prediction Application

Porto3 adalah aplikasi web yang dibangun dengan **Streamlit** untuk memprediksi apakah seorang pelanggan akan mengalami churn (berhenti menjadi pelanggan) atau tidak. Aplikasi ini menggunakan model machine learning yang telah dilatih untuk memprediksi churn berdasarkan data pelanggan.

## Deskripsi

Porto3 adalah aplikasi web yang dibangun dengan **Streamlit** untuk memprediksi apakah seorang pelanggan akan mengalami churn (berhenti menjadi pelanggan) atau tidak. Aplikasi ini menggunakan model machine learning yang telah dilatih untuk memprediksi churn berdasarkan data pelanggan yang meliputi:

- **Credit Score**: Skor kredit pelanggan.
- **Geography**: Negara tempat tinggal pelanggan (misalnya: Jerman, Prancis, atau Spanyol).
- **Gender**: Jenis kelamin pelanggan (Laki-laki atau Perempuan).
- **Age**: Usia pelanggan (minimal 18 tahun).
- **Tenure**: Durasi pelanggan menjadi anggota (dalam tahun).
- **Balance**: Saldo rekening pelanggan.
- **NumOfProducts**: Jumlah produk yang dimiliki oleh pelanggan (misalnya: satu produk, dua produk, dll).
- **HasCrCard**: Apakah pelanggan memiliki kartu kredit (Ya atau Tidak).
- **IsActiveMember**: Apakah pelanggan masih aktif sebagai member (Ya atau Tidak).
- **EstimatedSalary**: Estimasi gaji tahunan pelanggan.

Berdasarkan data input ini, aplikasi akan memprediksi apakah pelanggan tersebut berisiko mengalami churn atau tetap menjadi pelanggan berdasarkan model prediksi yang telah dilatih. Model yang digunakan adalah model **classification**.

## Fitur
- **Input Data Pelanggan**: Pengguna dapat memasukkan data pelanggan melalui antarmuka Streamlit.
- **Prediksi Churn**: Berdasarkan data input, aplikasi akan memprediksi apakah pelanggan akan churn atau tidak.
- **Probabilitas Prediksi**: Aplikasi juga menunjukkan probabilitas churn untuk memberikan kejelasan lebih lanjut mengenai hasil prediksi.

## Struktur Proyek
Porto3/
├── Porto_3_Streamlit.py        # Skrip utama untuk aplikasi Streamlit
├── Model Porto 3.joblib        # File model yang digunakan untuk prediksi
├── requirements.txt            # Daftar dependensi yang dibutuhkan
└── README.md                   # File ini
