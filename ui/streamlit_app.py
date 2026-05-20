import streamlit as st
import requests

st.set_page_config(layout="wide")

st.title("Incident Response Agent")

query = st.text_area("Incident Description")

col1, col2 = st.columns([1, 2])

if st.button("Investigate"):

    res = requests.post(
        "http://localhost:8000/investigate",
        json={"query": query}
    )

    data = res.json()

    with col1:
        st.subheader("Controls")
        st.write("Incident submitted")

    with col2:
        st.subheader("AI Analysis")
        st.write(data["analysis"])