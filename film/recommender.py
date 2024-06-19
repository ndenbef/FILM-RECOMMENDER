# import pickle
# import ast


# recommend = pickle.load(open('D:/PROGRAMS/WEB/PROJET FINAL/CODE/FILM RECOMMENDER/film/recommender.pkl', 'rb'))
# movies = pickle.load(open('D:/PROGRAMS/WEB/PROJET FINAL/CODE/FILM RECOMMENDER/film/movie_list.pkl', 'rb'))

# def recommender(movie):
#     try:
#         movie_row = movies[movies['movie_id'] == movie]
#         # if movie_row.empty:
#         #     raise ValueError('Movie cannot found in database')
#         # index = movie_row.index[0]
        
#         index = movie_row
        
#         distances = sorted(list(enumerate(recommend[index])), reverse=True, key = lambda x: x[1])
#         for i in distances[1:11]:
#             recommended = [movies.iloc[i[0]]['title']]
#             print(movies.iloc[i[0]]['title'])
            
#         # recommendations = recommend.get_top_n(movies, 10)
#         # recommended_movies = [movies[i] for i in recommendations]
        
#     # return recommended_movies
#         return recommended
#     except:
#       print('Movie not found in database')
        
# # def recommender(movie):
# #     recommendations = recommend.get_top_n(movie_id, 10)
# #         recommended_movies = [movies[i] for i in recommendations]
        
    

# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from .models import FilmSerie

# def movie_recommendation(movie_id):
#     #current_movie = FilmSerie.objects.get(id=movie_id)
#     movies = FilmSerie.objects.exclude(id=movie_id)

#     # create a TF-IDF matrix of the movie descriptions
#     tfidf = TfidfVectorizer(stop_words='english')
#     matrix = tfidf.fit_transform([movie.description for movie in movies])

#     # calculate cosine similarity between the current movie and other movies
#     cosine_similarities = cosine_similarity(matrix, matrix)

#     # # get the top 10 similar movies
#     # similar_movies = movies[list(cosine_similarities[-1][:-1].argsort()[-10:])]
    
#     # get a slice of the 10 movies sorted by similarity
#     movie_slice = cosine_similarities[-1].argsort()[:-11:-1]
    
#     for movie in movie_slice :
#         print(movie)

# # get a QuerySet of the similar movies using slice indexing
#     #similar_movies = movies[movie_slice]
    
#     movie_slice = slice(movie_slice[0], movie_slice[-1] + 1)  # create a slice from the indices
#     print(movie_slice)
#     similar_movies = movies[movie_slice]  # retrieve the actual movies using the slice
    
#     similar movies
    
#     print(similar_movies)

#     return similar_movies

# from urllib import response
# from django.shortcuts import get_object_or_404, render, HttpResponse
from linecache import cache
from django.shortcuts import render, get_object_or_404
from .models import FilmSerie, User

def movie_recommender(movie_id):
    movie = get_object_or_404(FilmSerie, id=movie_id)

    # get all movies except the current one
    other_movies = FilmSerie.objects.exclude(id=movie_id)

    # calculate genre similarity between the current movie and other movies
    description_similarities = {}
    for other_movie in other_movies:
        # calculate Jaccard similarity of the names,genres and description named as tag using sets
        tag = (movie.title + movie.genre + movie.description).lower()
        description_intersection = set(movie.title.split(' ') + movie.genre.split(' ') + movie.description.split(' ')).intersection(set(other_movie.title.split(' ') + other_movie.genre.split(' ') + other_movie.description.split(' ')))
        description_union = set(movie.title.split(' ') + movie.genre.split(' ') + movie.description.split(' ')).union(set(other_movie.title.split(' ') + other_movie.genre.split(' ') + other_movie.description.split(' ')))
        score = len(description_intersection) / len(description_union)
        description_similarities[other_movie] = score
        
    for i in range(0, 5):
        # sort movies in descending order of genre similarity
        recommendations = sorted(description_similarities, key=description_similarities.get, reverse=True)

    return recommendations

def user_movie_recommender(request):
    # movie = get_object_or_404(FilmSerie, id=movie_id)
    
    user=request.user
    
    genre1 = user.genre1
    genre2 = user.genre2
    
    # check if there are cached recommendations for this user
    cache_key = f'user-{user.id}-recommendations'
    recommendations = cache.get(cache_key)
    
    # get all movies except the current one
    movies  = FilmSerie.objects.filter(genre__icontains=genre1).filter(genre__icontains=genre2)


    # calculate genre similarity between the current movie and other movies
    genre_similarities = {}
    recommended_movies = {}
    for movie in movies:
        # calculate Jaccard similarity of the names,genres and description named as tag using sets
        tag = (str(genre1) + str(genre2)).lower()
        genre_intersection = set( movie.genre.split(' ') ).intersection(set(tag))
        genre_union = set( movie.genre.split(' ') ).union(set(tag))
        score = len(genre_intersection) / len(genre_union)
        genre_similarities[movies] = score
        
    # sort movies in descending order of genre similarity
    recommendations = sorted(genre_similarities, key=genre_similarities.get, reverse=True)
    
    # for movie in recommendations:
    #     matching_movie = FilmSerie.objects.filter(title=movie.title).first()[:1].get()

    #     if matching_movie:
    #         # if there is a match, add it to the recommended_movies list
    #         recommended_movies[matching_movie]
    
    recommendations = recommendations[0]

    return recommendations