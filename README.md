[Exoplanets] [Anna Vidal Perez]

[Data Analytics Full-Time Barcelona, April 2019]

# Overview

Exploratory analysis and explonet classification of the stellar objects detected by the Kepler Space Telescope and confirmed exoplanets from astronomical literature.

### Ideas and hypothesis

Having a look at the data we could ask the following questions:

* How many of the Kepler detections ended up being confirmed exoplanets?
* What is the ratio of habitable planets of the total of confirmed exoplanets?
* What are the main characteristics of the confirmed exoplanets and their stars?
* Can we prove Kepler's third law of planetary motion (Law of Periods)?
"The law states that the square of the orbital period of a planet is directly proportional to the cube of the semi-major axis of its orbit."

    Null hypothesis: the law of periods is not met.  
    Alternative hypothesis: the law of periods is met.

* Can we use machine learning to classify confirmed exoplanets? And to classify the type of exoplanet?



# Data preparation

The first dataset is the Kepler Exoplanet Search Results from Kaggle and has information about the 10000 objects detected by the Kepler Space Observatory. 
* Shape: (9564, 50)
* Size: 3.7 MB
* Complexity: https://exoplanetarchive.ipac.caltech.edu/docs/API_kepcandidate_columns.html

The second dataset is also public and downloaded from the website of Planetary Habitability Laboratory (PHL). It has more than 3000 already confirmed planets and contains interesting information about their possible habitability.
* Shape: (3873, 68)
* Size: 1.6 MB
* Complexity: http://phl.upr.edu/projects/habitable-exoplanets-catalog/data/database

Both datasets are complex since they have astronomical technical information. 

[Kepler Exoplanet Search Results](https://www.kaggle.com/nasa/kepler-exoplanet-search-results)  
[(Planetary Habitability Laboratory) PHL's exoplanets catalogue](http://phl.upr.edu/projects/habitable-exoplanets-catalog/data/database)

# Data Ingestion & Database


# Data Wrangling and Cleaning

1. Checking dtypes, renaming columns for use of MySQL and better understanding, dropping NaN values and information not needed.
2. Visualizing outliers. Outliers won't be removed unless it is needed, since data has already passed a scientific test to be part of the database. In case needed, only then they will be removed. 

# Data Analysis

~~* Overview the general steps you will go through to analyze your data in order to test your hypothesis.
* Document each step of your data exploration and analysis.
~~* Print charts to demonstrate the effect of your work. Charts make your presentation look good too.
* If you use ML in your final project, also describe your feature selection process.

# Model Training and Evaluation

~~* Train your ML model, produce results, and evaluate.
* This is an iterative process. Try your best to improve your model performance by:
~~* Try different models and select one that is the simplest yet produce the best result.
* Try advanced techniques and see if they improve the result.

# Conclusion

~~* Summarize your data analysis result.
* State your conclusion of your hypothesis testing.
~~* Interpret your findings in terms of the human-understandable question you try to answer.

# What are the next steps?




