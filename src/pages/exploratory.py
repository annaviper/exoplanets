import streamlit as st
import pandas as pd


def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading Home ..."):
        st.write(
            # """Exoplanets & habitability"""
        )

        @st.cache
        def load_data(URL, nrows):
            data = pd.read_csv(URL, nrows=nrows)
            def lowercase(x): return str(x).lower()
            data.rename(lowercase, axis='columns', inplace=True)
            return data

        # Create a text element and let the reader know the data is loading.
        data_load_state = st.text('Loading data...')
        URL = 'datasets/phl_processed.csv'
        data = load_data(URL, 5)
        data_load_state.text('Loading data...done')

        # Data
        st.text('This is a sample of the data')
        st.write(data.head())

        st.line_chart(data)

