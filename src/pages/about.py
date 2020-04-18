"""Home page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading About ..."):
        st.markdown(
            """Anna Viper""",
            unsafe_allow_html=True,
        )
