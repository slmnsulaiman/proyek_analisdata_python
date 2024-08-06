import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
main_df = pd.read_csv('main_data.csv')

# Pastikan kolom order_purchase_timestamp dalam format datetime
main_df['order_purchase_timestamp'] = pd.to_datetime(main_df['order_purchase_timestamp'])

# Judul Dashboard
st.title("Dashboard E-commerce")

# Sidebar untuk memilih rentang tanggal
st.sidebar.header("Filter Tanggal")
start_date = st.sidebar.date_input("Tanggal Mulai", value=pd.to_datetime(main_df['order_purchase_timestamp'].min()))
end_date = st.sidebar.date_input("Tanggal Akhir", value=pd.to_datetime(main_df['order_purchase_timestamp'].max()))

# Filter data berdasarkan rentang tanggal
filtered_data = main_df[(main_df['order_purchase_timestamp'] >= pd.to_datetime(start_date)) & 
                         (main_df['order_purchase_timestamp'] <= pd.to_datetime(end_date))]

# Pertanyaan Bisnis 1: Distribusi Metode Pembayaran
st.subheader("1. Distribusi Metode Pembayaran")
payment_distribution = filtered_data.groupby('payment_type')['payment_value'].count().reset_index()

# Visualisasi distribusi metode pembayaran
fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.barplot(x='payment_type', y='payment_value', data=payment_distribution, ax=ax1)
ax1.set_title('Jumlah Pembelian Berdasarkan Metode Pembayaran')
ax1.set_xlabel('Metode Pembayaran')
ax1.set_ylabel('Jumlah Transaksi')
ax1.tick_params(axis='x', rotation=45)
st.pyplot(fig1)

# Pertanyaan Bisnis 2: Kategori Produk dengan Pendapatan Tertinggi
st.subheader("2. Kategori Produk dengan Pendapatan Tertinggi")
revenue_per_category = filtered_data.groupby('product_category_name')['price'].sum().reset_index()
top_5_revenue_categories = revenue_per_category.sort_values(by='price', ascending=False).head(5)

# Visualisasi kategori produk dengan pendapatan tertinggi
fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.barplot(x='product_category_name', y='price', data=top_5_revenue_categories, ax=ax2)
ax2.set_title('5 Kategori Produk dengan Total Pendapatan Tertinggi')
ax2.set_xlabel('Kategori Produk')
ax2.set_ylabel('Total Pendapatan')
ax2.tick_params(axis='x', rotation=45)
st.pyplot(fig2)
