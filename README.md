# Whisky Recommender 

The app can be accessed here: https://share.streamlit.io/kennygtanaka/whisky_recommender/main/test.py

## Data Sources 

Meta-Critc Whisky Database - https://whiskyanalysis.com/index.php/database/

## Summary 
This whisky recommender uses cosine similarity to weight different features of each whisky such as type, location and taste. After a user inputs their favorite whisky, the recommender outputs a list of whisky that are similar to it. 

## Method 

The recommender was created using cosine similarity. 
Taste was given a weight of 7x more than other variables. 
Streamlit, a web development tool was used to create an app to have the recommender run. 

## Input 

The name of favorite whisky is input. If there isn't a direct match, the name needs to be a subset of one of the whiskies in the database. 

## Output 

The name, cost, class, country and type of similar whiskies are given. 
