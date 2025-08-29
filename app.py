# app.py
import streamlit as st
import pandas as pd
from recommender import recommend  

st.set_page_config(page_title="Movie Recommender Sytem",layout="wide")
st.title("Movie Recommender System")
st.write("Select a movie")
movies_df = pd.read_pickle("movies.pkl")
movie_list = movies_df['Title'].values
selected_movie = st.selectbox("Choose a movie:", movie_list)
if st.button("Show Recommendations"):
    recommendations = recommend(selected_movie)
    cols=st.columns(5)
    for idx,rec in enumerate(recommendations):
        with cols[idx]:
            st.image(rec['Poster'],use_container_width=True)
            st.caption(rec['Title'])
        