import yfinance as yf
import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Titolo dell'app
st.title('Analisi della Stagionalità del Titolo Azionario')

# Input per il ticker
ticker = st.text_input('Inserisci il simbolo del titolo (es. MSFT per Microsoft)', 'MSFT')

# Scaricamento dei dati da Yahoo Finance
df = yf.download(ticker, start='2010-01-01', end=pd.Timestamp.today().strftime('%Y-%m-%d'))

# Visualizzazione dei dati scaricati
st.subheader('Dati Storici')
st.write(df.tail(100))

# Aggregazione giornaliera
df_daily = df['Close']

# Rimuovi 29 febbraio per gestire anni bisestili
df_daily = df_daily[~((df_daily.index.month == 2) & (df_daily.index.day == 29))]

# Riempimento dei dati mancanti con interpolazione lineare
df_daily = df_daily.asfreq('D').interpolate()

# Decomposizione STL
decomposition = sm.tsa.seasonal_decompose(df_daily, model='multiplicative', period=365)

# Visualizzazione delle componenti
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(10, 8))

ax1.plot(df_daily, label='Originale')
ax1.legend(loc='upper left')
ax1.set_title('Dati Originali')

ax2.plot(decomposition.trend, label='Trend')
ax2.legend(loc='upper left')
ax2.set_title('Componente Trend')

ax3.plot(decomposition.seasonal, label='Stagionale')
ax3.legend(loc='upper left')
ax3.set_title('Componente Stagionale')

ax4.plot(decomposition.resid, label='Residuo')
ax4.legend(loc='upper left')
ax4.set_title('Componente Residuale')

plt.tight_layout()
st.pyplot(fig)

# Grafico delle componenti stagionali basate su diversi intervalli temporali
st.subheader('Componente Stagionale per Diversi Periodi')

# Creazione dell'indice giornaliero per il grafico
current_year = pd.Timestamp.today().year
if pd.Timestamp(current_year, 2, 29).is_leap_year:
    days = np.arange(1, 367)
else:
    days = np.arange(1, 366)

# Calcolo delle componenti stagionali per diversi intervalli di tempo
five_years_seasonal = df_daily[-365*5:].groupby(df_daily[-365*5:].index.dayofyear).mean()
ten_years_seasonal = df_daily[-365*10:].groupby(df_daily[-365*10:].index.dayofyear).mean()
last_year_seasonal = df_daily[-365:].groupby(df_daily[-365:].index.dayofyear).mean()

# Calcolo del valore di chiusura per l'anno corrente fino alla data attuale
current_year_close = df[df.index.year == df.index[-1].year]
current_year_close = current_year_close[current_year_close.index <= df.index[-1]]

# Creazione dell'indice giornaliero per il grafico
days = np.arange(1, 366)

# Allineamento delle serie stagionali all'anno corrente
current_year_start_day = df.index[-1].dayofyear
shifted_five_years_seasonal = np.roll(five_years_seasonal.values, -current_year_start_day + 1)
shifted_ten_years_seasonal = np.roll(ten_years_seasonal.values, -current_year_start_day + 1)
shifted_last_year_seasonal = np.roll(last_year_seasonal.values, -current_year_start_day + 1)

# Creazione del grafico
plt.figure(figsize=(10, 6))
plt.plot(days, shifted_five_years_seasonal[:365], label='Stagionalità 5 anni')
plt.plot(days, shifted_ten_years_seasonal[:365], label='Stagionalità 10 anni')
plt.plot(days, shifted_last_year_seasonal[:365], label='Ultimo anno')
plt.plot(current_year_close.index.dayofyear, current_year_close['Close'], label='Anno Corrente', linestyle='--', color='red')
plt.title('Componente Stagionale')
plt.xlabel('Mesi')
plt.ylabel('Valore')
plt.xticks(np.linspace(1, 365, num=12), ['Gen', 'Feb', 'Mar', 'Apr', 'Mag', 'Giu', 'Lug', 'Ago', 'Set', 'Ott', 'Nov', 'Dic'])
plt.legend()
st.pyplot(plt)
