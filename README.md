# Movie-Recommender-System
This is a **content-based movie recommender system** built using the [TMDb (The Movie Database)]([https://www.themoviedb.org/](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)) dataset. It recommends movies based on similarity in features such as genres, cast, crew, keywords, and more.
## 📂 Dataset
The project uses the following two files from the TMDb dataset:
tmdb_5000_movies.xls
tmdb_5000_credits.xls
## 🧠 Project Features
1. Preprocessing of data including parsing JSON columns
2. Feature engineering with genres, cast, crew, keywords
3. Text vectorization using **CountVectorizer**
4. Cosine similarity to measure movie closeness
5. Recommendation function based on similarity score
6. Deployment-ready using **Streamlit**
## 💻 Tech Stack
1. **Python**
2. **Pandas, NumPy**
3. **Scikit-learn**
4. **NLTK**
5. **Streamlit** for web interface
6. **Pickle** for model serialization
📦 Pickle Files
The following files are used to store the processed data and similarity matrix:
movies_dict.pkl
similarity.pkl
👉 Download similarity.pkl from this link:
[(similarity.pkl)]file(https://drive.google.com/file/d/14aktXoqToQfCrd1LXo_Jja0BPLztdtTZ/view?usp=drive_link)
