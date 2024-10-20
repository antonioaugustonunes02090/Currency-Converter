import streamlit as st
from api import get_currencies, get_last_bid

st.title("Currency-Converter")
cur1 = st.selectbox('Select the currency',get_currencies(),key='1')
if st.button('Get the conversion',key='11'):
    st.write(f'R${get_last_bid(cur1)}')
cur2 = st.selectbox('Select the currency',get_currencies(),key='2')
if st.button('Get the conversion',key='12'):
    st.write(f'R${get_last_bid(cur2)}')
cur3 = st.selectbox('Select the currency',get_currencies(),key='3')
if st.button('Get the conversion',key='13'):
    st.write(f'R${get_last_bid(cur3)}')
