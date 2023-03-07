import altair as alt
import pandas as pd
import streamlit as st

df = pd.read_csv('data.csv')

df['date'] = pd.to_datetime(df['date'])
df['year_month'] = df['date'].dt.to_period('M')
df['year_month'] = df['year_month'].astype(str).str.replace('-', '').astype(int)
df['day'] = df['date'].dt.day
df['day'] = df['day'].astype(int)

default_ym = 202003
ym_slider = st.slider('Year_Month', min(df['year_month']), max(df['year_month']), value=default_ym)

st.write("## Association between Vaccination Rate and Number of Covid Cases")

