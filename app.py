import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
trades = pd.read_csv("data/historical_data.csv")
fg = pd.read_csv("data/fear_greed_index.csv")

# Convert date
trades['Timestamp IST'] = pd.to_datetime(trades['Timestamp IST'], dayfirst=True, errors='coerce')
trades['date'] = trades['Timestamp IST'].dt.date
fg['date'] = pd.to_datetime(fg['date']).dt.date

# Merge
merged = pd.merge(trades, fg, on='date')

st.title("📊 Trader Sentiment Dashboard")

# PnL vs Sentiment
pnl = merged.groupby('classification')['Closed PnL'].mean().reset_index()

fig, ax = plt.subplots()
sns.barplot(x='classification', y='Closed PnL', data=pnl, ax=ax)
st.pyplot(fig)

# Trade Frequency
freq = merged.groupby('classification').size().reset_index(name='trade_count')

fig2, ax2 = plt.subplots()
sns.barplot(x='classification', y='trade_count', data=freq, ax=ax2)
st.pyplot(fig2)