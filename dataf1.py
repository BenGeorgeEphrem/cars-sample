import streamlit as st
import pandas as pd
import altair as alt
data = pd.read_csv('auto-clean.csv')
st.title('Car Price ')
car=st.selectbox("Select the car",data['make'].unique())
st.text(car)
ptype = st.radio("select chart",['line','dot'])
if ptype =='dot':
  al = alt.Chart(data[data['make']==car],height=280,width=300).mark_circle().encode(
      x = "horsepower",
      y ="price-OMR",
      tooltip = ["horsepower","price-OMR"]
  ).interactive()
else:
  al = alt.Chart(data[data['make']==car],height=280,width=300).mark_line().encode(
      x = "horsepower",
      y ="price-OMR",
      tooltip = ["horsepower","price-OMR"]
  ).interactive()
st.altair_chart(al)
