"""This page is for searching and viewing the list of awesome resources"""
import logging
import streamlit as st

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

def write():
    """Writes content to the app"""
    # st.sidebar.title("Sources")
    # tags = ast.shared.components.multiselect(
    #     "Select Tag(s)", options=ast.database.TAGS, default=[]
    # )
    st.markdown("""
    # Datasets

## Habitability
The first dataset is from [Planetary Habitability Laboratory (PHL)](http://phl.upr.edu/projects/habitable-exoplanets-catalog/data/database), University of Puerto Rico. 
It has more than 3000 already confirmed planets and contains interesting information about the habitability of the planet. 
It is the dataset used for the exploratory analysis.
* Shape: (3873, 68)
* Size: 1.6 MB
* Complexity: http://phl.upr.edu/projects/habitable-exoplanets-catalog/data/database


## Kepler telescope
The second dataset is the [Kepler Exoplanet Search Results](https://www.kaggle.com/nasa/kepler-exoplanet-search-results) from Kaggle and has information about the objects detected by the Kepler Space Observatory. This dataset will be used for machine learning classificiation.
* Shape: (9564, 50)
* Size: 3.7 MB
* Complexity: https://exoplanetarchive.ipac.caltech.edu/docs/API_kepcandidate_columns.html
""")

    # with st.spinner("Loading resources ..."):
    #     markdown = resources.get_resources_markdown(
    #         tags, author, show_awesome_resources_only
    #     )
    #     resource_section.markdown(markdown)

    # if st.sidebar.checkbox("Show datasets sources"):
    #     st.subheader("Source JSON")
    #     st.write(ast.database.RESOURCES)
    #
    # tags = None


if __name__ == "__main__":
    write()
