[Exoplanets] [Anna Vidal Perez]

[Data Analytics Full-Time Barcelona, April 2019]

# Overview

Exploratory analysis and exoplanet classification of the stellar objects detected by the Kepler Space Telescope and confirmed exoplanets from astronomical literature.

### Ideas and hypothesis

Having a look at the data we could ask the following questions:

* How many of the Kepler detections ended up being confirmed exoplanets?
* What is the ratio of habitable planets of the total of confirmed exoplanets?
* What are the main characteristics of the confirmed exoplanets and their stars?
* Can we prove Kepler's third law of planetary motion (Law of Periods)?  
* Can we use machine learning to classify if a detection is an exploanet or a false positive? And to classify the type of exoplanet?



# Data preparation

The first dataset is the Kepler Exoplanet Search Results from Kaggle and has information about the objects detected by the Kepler Space Observatory. 
* Shape: (9564, 50)
* Size: 3.7 MB
* Complexity: https://exoplanetarchive.ipac.caltech.edu/docs/API_kepcandidate_columns.html

The second dataset is also public and downloaded from the website of Planetary Habitability Laboratory (PHL) from the University of Puerto Rico. It has more than 3000 already confirmed planets and contains interesting information about their possible habitability.
* Shape: (3873, 68)
* Size: 1.6 MB
* Complexity: http://phl.upr.edu/projects/habitable-exoplanets-catalog/data/database  
  
Both datasets are complex since they have astronomical technical information.   

[Kepler Exoplanet Search Results](https://www.kaggle.com/nasa/kepler-exoplanet-search-results)  
[(Planetary Habitability Laboratory) PHL's exoplanets catalogue](http://phl.upr.edu/projects/habitable-exoplanets-catalog/data/database)

# Data Ingestion & Database

Using pandas to read the information from original .CSV and cleaning. After that, reading the clean information from SQL to do the analysis and machine learning.  
  
![Kepler database clean](https://i.ibb.co/Sd6gV2P/Screenshot-2019-04-25-at-09-00-00.png)  
  
Habitability database has too many columns to show in a picture.  
  
# Data Wrangling and Cleaning

1. Checking dtypes, renaming columns for use of MySQL and better understanding, dropping NaN values and information not needed.
2. Visualizing outliers. Outliers won't be removed unless it is needed, since data has already passed a scientific test to be part of the database. In case they interfere a lot with the analysis, only then they will be removed. 

# Data Analysis

1. Hypothesis testing to prove Kepler's third law.   

"The law states that the square of the orbital period of a planet is directly proportional to the cube of the semi-major axis of its orbit."

    Null hypothesis: the law of periods is not met.  
    Alternative hypothesis: the law of periods is met.

Calculated correlation, Pearson's R and R squared.

2. T-test for significance between different types of planets.  
3. Random Forest to classify Kepler objects into exoplanets or false negatives.  

# Model Training and Evaluation

With the Randome forest classifier we got an accuracy of 0.86.  
  
  
![Metric](https://i.ibb.co/fdVNnN4/Screenshot-2019-04-25-at-08-54-54.png)

# Conclusion

* Kepler's third law of periods is valid.
    
* Habitable planets are very rare.

* State your conclusion of your hypothesis testing.

* Not data enough to try to classify habitability of the exoplanet with machine learning.

# What are the next steps?

- Finding out about the radius behaviour of the gas exoplanets.
- More data exploration.




