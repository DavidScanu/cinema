import requests
import streamlit as st

# --- Setting page layout ---
st.set_page_config(
    page_title="Test connectino to backend",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.header("Test connection to backend", divider="rainbow")
st.write("This is a connection test to the FasAPI backend!")
st.json(requests.get("http://backend_server:8000/").json())
st.write("Autoreload works!!!")