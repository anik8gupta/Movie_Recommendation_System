# Get the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data Importing and Preprocessing

r_cols = ['user_id', 'movie_id', 'rating'] # User List with Movies's Star Rattings
ratings = pd.read_csv('u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title'] # IMDB Movie List
movies = pd.read_csv('u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)

# Discovery and Visualization

movieRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')
movieRatings.head()

# Taking One Instance from the dataset for Analysis

starWarsRatings = movieRatings['Star Wars (1977)'] # selecting Movie for Base Recommendation
starWarsRatings.head()

# Calculating Correlation

similarMovies = movieRatings.corrwith(starWarsRatings)
similarMovies = similarMovies.dropna()
df = pd.DataFrame(similarMovies)
df.head(10)

# Analyzing the results

similarMovies.sort_values(ascending=False)

# Data Transformation

movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})
movieStats.head()

# Sorting datasets by a metric

popularMovies = movieStats['rating']['size'] >= 100
movieStats[popularMovies].sort_values([('rating', 'mean')], ascending=False)[:15]

# Joining two Data frames

df = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns=['similarity']))
df.head()

# Analyzing the results

df.sort_values(['similarity'], ascending=False)[:15]












