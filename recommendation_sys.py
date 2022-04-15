# -*- coding: utf-8 -*-
"""recommendation-sys.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15JLiDh3OwUo-Z6bpuckokCvcV6W7wQ8E
"""

!pip install sklearn

#import libraries
import numpy as mp
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

#load the data
from google.colab import files
uploaded = files.upload()

#store the data
df = pd.read_csv('IMDB-Movie-Data.csv')

df['Movie_id'] = range(0,1000) 
# show the first 2 rows in csv
df.head(2)

df.shape # gets the count of rows and cols in the dateset

# list of important items
columns = ['Actors', 'Director', 'Genre', 'Title']

# show the columns
df[columns].head(3)

# check for null values in the data provided
df[columns].isnull().values.any()

# function to combine values of important columns into a single string
def get_important_features(data):
  important_features = []
  for i in range(0,data.shape[0]):
    important_features.append(data['Actors'][i]+' '+data['Director'][i]+' '+data['Genre'][i]+' '+data['Title'][i])

  return important_features

df['important_features'] = get_important_features(df)

df.head(3)

# convert the text to a matrixof token counts
cm = CountVectorizer().fit_transform(df['important_features'])

# get the consine similarity matrix from the count matrix
cs = cosine_similarity(cm)
print(cs)

# get the shape of the consine similarity matrix
cs.shape

title = 'The Amazing Spider-Man'

# get the id of the movie
movie_id = df[df.Title == title]['Movie_id'].values[0]

# print(movie_id)

# create a list of enumerations for the similarity score
score = list(enumerate(cs[movie_id]))
# scroe looks like: [(movie_id, score), (1, 0.0625)
print(score)

# sort the score list
sorted_score = sorted(score,key= lambda x:x[1], reverse=True)
sorted_score = sorted_score[1:]

print(sorted_score)

# print the recommended movies that are similar to what the user likes
j=0 
print(f"The top 7 movies recommended to {title} are: \n")
for item in sorted_score:
  movie_title = df[df.Movie_id == item[0]]['Title'].values[0]
  print(j+1,movie_title)
  j+=1
  if j>6:
    break