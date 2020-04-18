import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading Home ..."):
        # st.title("""Exoplanets and habitability""")
        st.markdown("""
# Overview

This is the final project for the Data Analytics bootcamp I did in early 2019. 
The project is divided in two: the first part is the exploratory analysis of confirmed exoplanets. 
The second is the classification of Kepler's detections into confirmed exoplanets or false positives with machine learning.

### Questions

* How many of Kepler's telescope detections end up being confirmed exoplanets?
* Of those confirmed exoplanets, what is the ratio of habitable planets?
* What are the main characteristics of the confirmed exoplanets and their stars?
* Can we prove Kepler's third law of planetary motion (Law of Periods)?
* Can we use machine learning to classify if a detection is an exoplanet or a false positive? 
And to classify the type of exoplanet?
""")