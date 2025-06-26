import pickle
import streamlit as st
import requests


OMDB_API_KEY = "3e23cfbe"

def fetch_movie_details(title):
    try:
        url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return {
            "Poster": data.get("Poster", "https://via.placeholder.com/500x750?text=No+Poster"),
            "Year": data.get("Year", "N/A"),
            "Genre": data.get("Genre", "N/A"),
            "Rating": data.get("imdbRating", "N/A"),
            "Plot": data.get("Plot", "N/A"),
            "Title": data.get("Title", title)
        }
    except:
        return {
            "Poster": "https://via.placeholder.com/500x750?text=No+Poster",
            "Year": "N/A",
            "Genre": "N/A",
            "Rating": "N/A",
            "Plot": "N/A",
            "Title": title
        }

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    movie_details = []
    for i in distances[1:21]:
        title = movies.iloc[i[0]].title
        details = fetch_movie_details(title)
        movie_details.append(details)
    return movie_details

st.set_page_config(layout="wide")
st.header('🎬 Movie Recommender System')

movies = pickle.load(open(r"C:\Users\ABC\OneDrive\Desktop\Movie-Recommend\movie_list.pkl", 'rb'))
similarity = pickle.load(open(r'C:\Users\ABC\OneDrive\Desktop\Movie-Recommend\similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    movie_details_list = recommend(selected_movie)

    for row in range(4):
        cols = st.columns(5)
        for i in range(5):
            idx = row * 5 + i
            details = movie_details_list[idx]
            with cols[i]:
                st.image(details['Poster'], use_container_width=True)
                with st.expander(details['Title']):
                    st.markdown(f"**📅 Year:** {details['Year']}")
                    st.markdown(f"**🎭 Genre:** {details['Genre']}")
                    st.markdown(f"**⭐ IMDb Rating:** {details['Rating']}")
                    st.markdown(f"**📝 Plot:** {details['Plot']}")
