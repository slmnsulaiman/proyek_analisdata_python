# E Commerce Dashboard

Dashboard ini dibuat untuk menganalisis data E-commerce, memberikan wawasan tentang distribusi metode pembayaran dan kategori produk dengan pendapatan tertinggi.

## Fitur

- Visualisasi distribusi metode pembayaran yang digunakan oleh pelanggan.
- Analisis kategori produk dengan total pendapatan tertinggi.

## Prasyarat

Sebelum menjalankan dashboard, pastikan Anda memiliki Python 3.x dan pustaka yang diperlukan.

## Setup Environment - Anaconda

```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal

```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app

```
streamlit run dashboard/dashboard.py

```
