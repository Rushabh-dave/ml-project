import numpy as np
import pandas as pd

import re
import joblib
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import  ENGLISH_STOP_WORDS
stop_words = ENGLISH_STOP_WORDS
movies = pd.read_csv('imdb_top_1000.csv')
movies = movies[['Series_Title','Poster_Link', 'Genre','Overview', 'Director', 'Star1', 'Star2', 'Star3']]
features = ['Genre', 'Overview', 'Director','Star1','Star2','Star3']
for feature in features:
    movies[feature] = movies[feature].fillna(' ').astype(str).str.lower().str.strip()
for feature in ['Director','Star1','Star2','Star3']:
    movies[feature] = movies[feature].str.replace(' ','',regex=True)
movies['tags'] = movies['Overview']+ ' ' + movies['Genre']+ ' ' + movies['Director']+ ' ' + movies['Star1']+ ' ' + movies['Star2']+ ' '  +movies['Star3']
movies = movies[['Series_Title','Poster_Link','tags']]
movies= movies.rename(columns={'Series_Title':'Title','Poster_Link':'Poster'})
new_df=movies[['Title','Poster','tags']]
ps=PorterStemmer()
def stem(text):
    text = text.lower()
    text = re.sub('[^a-zA-Z]', ' ', text)   # keep only letters
    words = text.split()
    words = [ps.stem(w) for w in words if w not in stop_words]
    return " ".join(words)
new_df['tags'] = new_df['tags'].apply(stem)
tfidf = TfidfVectorizer(max_features=10000, stop_words='english')
vectors = tfidf.fit_transform(new_df['tags']).toarray()
from sklearn.metrics.pairwise import cosine_similarity
similarity=cosine_similarity(vectors)
def recommend(movie):
    movie_index=new_df[new_df['Title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommendations = []
    for i in movies_list:
        movie_data = {
            "Title": new_df.iloc[i[0]].Title,
            "Poster": new_df.iloc[i[0]].Poster
        }
        recommendations.append(movie_data)
    
    return recommendations


   
        












