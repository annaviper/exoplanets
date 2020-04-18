import streamlit as st
import src.pages.home
import src.pages.sources
import src.pages.exploratory
import src.pages.ml
import src.pages.about


PAGES = {
    "Home": src.pages.home,
    "Data sources": src.pages.sources,
    "Exploratory Analysis": src.pages.exploratory,
    "Machine Learning": src.pages.ml,
    "About me": src.pages.about,
}


def main():
    st.sidebar.title("Exoplanets and habitability")

    st.sidebar.title("\n\n\n\n\n\n")

    st.sidebar.subheader("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        page.write()

    st.sidebar.title("\n\n\n\n\n\n\n")
    st.sidebar.info("""[Github repository](https://github.com/annaviper/exoplanets)""")

if __name__ == "__main__":
    main()