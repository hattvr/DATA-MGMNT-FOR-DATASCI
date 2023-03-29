# --- PART 1: READING DATA ---
import json

# 1.1
def read_ratings_data(f):
    """
    Returns a dictionary that has movie as
    key, and the corresponding ratings as value.
    """
    ratings_file = open(f, 'r')

    ratings = {}
    for line in ratings_file.readlines():
        line = line.strip()

        if line:
            movie_info, rating, _ = line.split("|")
            ratings.setdefault(movie_info, []).append(float(rating))

    return ratings

movie_ratings = read_ratings_data("movieRatingSample.txt")
print(json.dumps(movie_ratings, indent=4))

# 1.2
def read_movie_genre(f):
    """
    Retruns a dictionary mapping from movie
    to genre.
    """
    movies_file = open(f, 'r')

    movies = {}
    for line in movies_file.readlines():
        line = line.strip()

        if line:
            genre, _, movie_info = line.split("|")
            movies[movie_info] = genre

    return movies

movie_to_genre = read_movie_genre("genreMovieSample.txt")
print(json.dumps(movie_to_genre, indent=4))

# --- PART 2: PROCESSING DATA ---

# 2.1
def create_genre_dict(d):
    """
    Returns a dictionary in which a genre
    is mapped to all the moves in that genre.
    """
    
    genre_to_movies = {}
    for movie, genre in d.items():
        genre_to_movies.setdefault(genre, []).append(movie)

    return genre_to_movies

genre_to_movies = create_genre_dict(movie_to_genre)
print(json.dumps(genre_to_movies, indent=4))

# 2.2
def calculate_average_rating(d):
    """
    Returns a dictionary in which a movie
    is mapped to its average rating.
    """

    average_ratings = {}
    for movie, ratings in d.items():
        average_ratings[movie] = sum(ratings) / len(ratings)

    return average_ratings

average_ratings = calculate_average_rating(movie_ratings)
print(json.dumps(average_ratings, indent=4))

# --- PART 3: RECOMMENDATION ---

# 3.1
def get_popular_movies(d, n=10):
    """
    Retruns a dictionary of top n movies based
    on the average ratings. If there are fewer than
    n movies, it should return all movies in order
    of top average ratings.
    """

    popular_movies = {}
    for movie, rating in sorted(d.items(), key=lambda x: x[1], reverse=True):
        if len(popular_movies) >= n:
            break

        popular_movies[movie] = rating

    return popular_movies

popular_movies = get_popular_movies(average_ratings, 10)
print(json.dumps(popular_movies, indent=4))

# 3.2
def filter_movies(d, thres_rating=3):
    """
    Returns a dictionary of movies that 
    are euqal to or greater than the threshold.
    """

    filtered_movies = {}
    for movie, rating in d.items():
        if rating >= thres_rating:
            filtered_movies[movie] = rating

    return filtered_movies

filtered_movies = filter_movies(average_ratings, 4)
print(json.dumps(filtered_movies, indent=4))

# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    """
    Retruns a dictionary of movie-to-average 
    rating of movies that make the cut.
    """

    filtered_movies = {
        movie: rating for movie, 
        rating in movie_to_average_rating.items() 
        if movie in genre_to_movies.get(genre, [])
    }

    popular_in_genre = get_popular_movies(filtered_movies, n)

    return popular_in_genre

popular_in_genre = get_popular_in_genre("Adventure", genre_to_movies, average_ratings, 5)
print(json.dumps(popular_in_genre, indent=4))

# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    pass

# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    pass

# --- PART 4: USER FOCUSED ---

# 4.1
def read_user_ratings(f):
    pass

# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    pass

# 4.3
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    pass
