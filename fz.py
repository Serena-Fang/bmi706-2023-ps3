import altair as alt
import pandas as pd
import streamlit as st

def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/Jinrui93/706Final/main/data.csv?token=GHSAT0AAAAAAB6HXXFMX337YJ7QKB7FWQHSZAG3FJA")

    return df

df = load_data()

st.write("## Association between Vaccination Rate and Number of Covid Cases")