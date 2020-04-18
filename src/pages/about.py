"""Home page shown when the user enters the application"""
import streamlit as st

import awesome_streamlit as ast

def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading About ..."):
        # ast.shared.components.title_awesome(" - About")
        st.markdown(
            """Anna Viper""",
            unsafe_allow_html=True,
        )
