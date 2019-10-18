Exoplanets and its habitability, by Anna Vidal Perez

Data Analytics Full-Time Barcelona, April 2019


# Overview

Exploratory analysis of Kepler's telescope detections, the habitability of confirmed exoplanets and their characteristics. Classification of Kepler's detections into exoplanets or false positives with machine learning.

### Ideas and hypothesis

Having a look at the data we could ask the following questions:

* How many of Kepler's telescope detections end up being confirmed exoplanets?
* What is the ratio of habitable planets of the total of confirmed exoplanets?
* What are the main characteristics of the confirmed exoplanets and their stars?
* Can we prove Kepler's third law of planetary motion (Law of Periods)?  
* Can we use machine learning to classify if a detection is an exploanet or a false positive? And to classify the type of exoplanet?
   
  
# Data preparation
  
The first dataset is the 'Kepler Exoplanet Search Results' from Kaggle and has information about the objects detected by the Kepler Space Observatory. 
* Shape: (9564, 50)
* Size: 3.7 MB
* Complexity: https://exoplanetarchive.ipac.caltech.edu/docs/API_kepcandidate_columns.html
    
The second dataset is also public and downloaded from the website of Planetary Habitability Laboratory (PHL) from the University of Puerto Rico. It has more than 3000 already confirmed planets and contains interesting information about their possible habitability.
* Shape: (3873, 68)
* Size: 1.6 MB
* Complexity: http://phl.upr.edu/projects/habitable-exoplanets-catalog/data/database  
   
Links to datasets:  
[Kepler Exoplanet Search Results](https://www.kaggle.com/nasa/kepler-exoplanet-search-results)  
[(Planetary Habitability Laboratory) PHL's exoplanets catalogue](http://phl.upr.edu/projects/habitable-exoplanets-catalog/data/database)
   
# Data Ingestion & Database
  
* Using Pandas to read the information from original .CSV and cleaning. 
* Reading the clean information from SQL to do the analysis and machine learning.  
  
![Kepler database clean](https://i.ibb.co/Sd6gV2P/Screenshot-2019-04-25-at-09-00-00.png)  
   
![Habitability](https://i.ibb.co/M7t4D1L/Screenshot-2019-04-25-at-09-09-28.png)    
   

# Data Wrangling and Cleaning

* Checking dtypes, renaming columns to use in MySQL and better understanding, dropping NaN values and information not needed.
  
* Visualizing outliers. Outliers won't be removed unless it is needed, since data has already gone through a scientific test to be part of the database. In case they interfere a lot with the analysis, only then they will be removed. 
  
    
# Data Analysis

1. Hypothesis testing to prove Kepler's third law of planetary motion. The law states:   

"The square of the orbital period of a planet is directly proportional to the cube of the semi-major axis of its orbit."

    Null hypothesis: the law of periods is not met.  
    Alternative hypothesis: the law of periods is met.

Calculated correlation, Pearson's R and R squared.

2. T-test for significance between different types of planets.  
3. Random Forest to classify Kepler objects into exoplanets or false negatives.  

# Model Training and Evaluation

With the Random Forest Classifier we got an accuracy of 0.90.
With KNN and Logistic Regression we got an accuracy of 0.79.

# Conclusion

* Kepler's third law of periods is valid.
    
* Habitable planets are very rare.

* We can classify a Kepler's telescope detection into exoplanet or false positive 86% of the time.

* Not data enough to try to classify habitability of the exoplanet.

# What are the next steps?

- Finding out about the radius behaviour of the gas exoplanets.
- More data exploration.
