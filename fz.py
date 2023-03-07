import altair as alt
import pandas as pd
import streamlit as st

df = pd.read_csv('data.csv')
df1 = pd.read_csv('data_month.csv')

# df['date'] = pd.to_datetime(df['date'])
# df['year_month'] = df['date'].dt.to_period('M')
# df['year_month'] = df['year_month'].astype(str).str.replace('-', '').astype(int)
# df['day'] = df['date'].dt.day
# df['day'] = df['day'].astype(int)

default_ym = 202003
ym_slider = st.slider('Year_Month', min(df1['new_date']), max(df1['new_date']), value=default_ym)

st.write("## Association between Vaccination Rate and Number of Covid Cases")

# state_filtered = df[df['state'] == state_selectbox]

df5 = df1[df1['new_date'] == ym_slider]

scatter = alt.Chart(df5).mark_circle().encode(
    x=alt.X('percent_insured:Q', scale=alt.Scale(domain=[75, 100]), title = 'Percent Insured'),
    y=alt.Y('cases_k:Q', title = 'Number of Cases (thousands)'),
    tooltip=['state','percent_insured','cases_k']
).properties(
    title='Vaccination Rate and COVID-19 Cases'
).interactive()

scatter_line = scatter + scatter.transform_regression('percent_insured','cases_k').mark_line()

st.altair_chart(scatter_line, use_container_width=True)

scatter1 = alt.Chart(df5).mark_circle().encode(
    x=alt.X('percent_insured:Q', scale=alt.Scale(domain=[75, 100]), title = 'Percent Insured'),
    y=alt.Y('deaths_k:Q', title = 'Number of Deaths (thousands)'),
    tooltip=['state','percent_insured','deaths_k']
).properties(
    title='Vaccination Rate and COVID-19 Deaths'
).interactive()

st.altair_chart(scatter1, use_container_width=True)