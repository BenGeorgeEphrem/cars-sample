import streamlit as st
import pandas as pd
import altair as alt
data = pd.read_csv('auto-clean.csv')
st.title('Car Range')
low = st.number_input("Enter min range",1990,134000)
high = st.number_input("Enter max range",1990,134000)
st.dataframe(data[data['price-OMR'].between(low,high)])
