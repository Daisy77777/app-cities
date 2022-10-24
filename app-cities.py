import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('World cities')

df = pd.read_csv('worldcities.csv')

# add a slider
pop_slider = st.sidebar.slider('Choose Population', 0.0, 40.0, 3.6)

# create a multi select
capital_filter = st.sidebar.multiselect(
     'Capital Selector',
     ['primary', 'admin', 'nan', 'minor'],  # options
     ['primary'])  # defaults

#capital_filter is a list of use choices

# filter by population
df = df[df.population >= pop_slider]

#filter by capital
df = df[df.capital.isin(capital_filter)]

form = st.sidebar.form("country_form")
country_filter = form.text_input('Country Name (enter ALL to reset)', 'ALL')
form.form_submit_button("Apply")

if country_filter!='ALL':
    df = df[df.country == country_filter]

# show on map
st.map(df)

# show df
st.write(df)

# show the pop lot
fig, ax = plt.subplots(figsize=(20, 5))
pop_sum = df.groupby('country')['population'].sum()
pop_sum.plot.bar(ax=ax)
st.pyplot(fig)
