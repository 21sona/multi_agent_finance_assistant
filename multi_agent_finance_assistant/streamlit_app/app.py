import streamlit as st
import requests

st.title("📈 Morning Market Brief Assistant")

if st.button("Get Brief"):
    response = requests.get("http://localhost:8000/market_brief")
    st.write(response.json()['brief'])
