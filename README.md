Exoplanets and its habitability, by Anna Vidal Perez

# Overview

Exploratory analysis of Kepler's telescope detections, the habitability of confirmed exoplanets and their characteristics. Classification of Kepler's detections into exoplanets or false positives with machine learning.

### Ideas and hypothesis

Having a look at the data we could ask the following questions:

* How many of Kepler's telescope detections end up being confirmed exoplanets?
* What is the ratio of habitable planets of the total of confirmed exoplanets?
* What are the main characteristics of the confirmed exoplanets and their stars?
* Can we prove Kepler's third law of planetary motion (Law of Periods)?  
* Can we use machine learning to classify if a detection is an exploanet or a false positive? And to classify the type of exoplanet?
   
# Datasets
  
The first dataset is the [Kepler Exoplanet Search Results](https://www.kaggle.com/nasa/kepler-exoplanet-search-results)   from Kaggle and has information about the objects detected by the Kepler Space Observatory. 
* Shape: (9564, 50)
* Size: 3.7 MB
* Complexity: https://exoplanetarchive.ipac.caltech.edu/docs/API_kepcandidate_columns.html
    
The second dataset is also public and downloaded from [Planetary Habitability Laboratory (PHL)](http://phl.upr.edu/projects/habitable-exoplanets-catalog/data/database), University of Puerto Rico. It has more than 3000 already confirmed planets and contains interesting information about their possible habitability.
* Shape: (3873, 68)
* Size: 1.6 MB
* Complexity: http://phl.upr.edu/projects/habitable-exoplanets-catalog/data/database  
    
# Data Analysis

1. Hypothesis testing to prove Kepler's third law of planetary motion. The law states:   

"The square of the orbital period of a planet is directly proportional to the cube of the semi-major axis of its orbit."

    Null hypothesis: the law of periods is not met.  
    Alternative hypothesis: the law of periods is met.

Calculated correlation, Pearson's R and R squared.

2. T-test for significance between different types of planets.  

# Machine Learning

Random forest, KNN and logistic regression to classify Kepler objects into exoplanets or false negatives.

Accuracy scores:  
- KNN: 0.81
- Logistic regression: 0.80
- Random Forest: 0.89
- Random Forest with number of parameters = 100: 0.90
  

# Conclusions

* Kepler's third law of periods is valid.
    
* Habitable planets are very rare.

* We can classify a Kepler's telescope detection into exoplanet or false positive 0.81% of the time.

* Not data enough to classify the habitability of the exoplanet.

# Slides

https://docs.google.com/presentation/d/12wC4PkwdBHOSofVmU3FqU4M3JNu8dGowPsvZTVexUAQ/edit?usp=sharing