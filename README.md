# ml-project
Movie Recommendation System


A content-based movie recommendation system built with Python, Pandas, Scikit-learn, and Streamlit.  
It recommend movies similar to the selected one by user based on TF-IDF vector and cosine similarity of movie metadata such as overview, genre, director, and  top 3 cast.

Dataset:The dataset io used is IMDB+TOP1000_movies.csv from Kaggle
Link for Dataset:https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows

## 🚀 Features
- Interactive **Streamlit web app**.
- Select any movie from the IMDb Top 1000 dataset.
- Get **Top 5 similar movie recommendations** instantly.
- Displays **movie posters + titles** for better UX.
- Uses **TF-IDF Vectorization** and **Cosine Similarity** for recommendations.

  ##  Installation & Usage

### Prerequisites
- Python 3.7 or above

### Install Dependencies
```bash pip install -r requirements.txt ```

  
### How to run the application

### 1. Run The app locally
  -  in app.py run this code ```streamlit run app.py```  
### 3. Click The link
  - https://ml-project-hquutzbpjb2ubwipflsrkd.streamlit.app/


### Current Limitations:
- Heavily reliant on metadata quality (overviews, actor names, genres, etc.).
- Does not use collaborative filtering or personalization.
- picture quality is low 
### Potential Upgrades:

- Combine with collaborative filtering for more personalized recommendations.
- Add richer metadata (like plot keywords, user ratings, or runtime).
- Implement caching or precomputed similarity matrices for faster responses.
- Enable user feedback integration to improve recommendation relevance.


