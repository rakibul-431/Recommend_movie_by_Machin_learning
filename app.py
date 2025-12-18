import streamlit as st
import pandas as pd
import pickle

similarity=pickle.load(open('similarity.pkl','rb'))
movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)

def Recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommendate_movie=[]
    for i in movie_list:
        movie_id=i[0]
        recommendate_movie.append(movies.iloc[i[0]].title)
    return recommendate_movie


st.title("Movie Recomender System")
Selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values,
)
if st.button("Recommend Movie"):
    Recommendation_movie=Recommend(Selected_movie_name)
    for i in Recommendation_movie:
        st.write(i)