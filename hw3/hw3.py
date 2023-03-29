# --- PART 1: READING DATA ---

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
print(movie_ratings)

# 1.2
def read_movie_genre(f):
    """
    Returns a dictionary mapping from movie
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
print(movie_to_genre)

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
print(genre_to_movies)

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
print(average_ratings)

# --- PART 3: RECOMMENDATION ---

# 3.1
def get_popular_movies(d, n=10):
    """
    Returns a dictionary of top n movies based
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
print(popular_movies)

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
print(filtered_movies)

# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    """
    Returns a dictionary of movie-to-average 
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
print(popular_in_genre)

# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    """
    Returns the average rating of the movies
    in the given genre.
    """

    genre_movies = {
        movie: rating for movie,
        rating in movie_to_average_rating.items()
        if movie in genre_to_movies.get(genre, [])
    }

    return sum(genre_movies.values()) / len(genre_movies)

genre_ratings = get_genre_rating("Adventure", genre_to_movies, average_ratings)
print(genre_ratings)

# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    """
    Returns the top n rated genres as 
    a dictionary of genre-to-average rating.
    """

    genre_ratings = {}
    for genre, _ in genre_to_movies.items():
        genre_ratings[genre] = get_genre_rating(genre, genre_to_movies, movie_to_average_rating)

    genre_popularity = get_popular_movies(genre_ratings, n)

    return genre_popularity

popularity_by_genre = genre_popularity(genre_to_movies, average_ratings, 5)
print(popularity_by_genre)

# --- PART 4: USER FOCUSED ---

# 4.1
def read_user_ratings(f):
    """
    Returns a user-to-movies dictionary that
    maps user ID to the movies they have rated.

    Value field should contain a list of tuples in
    the format (movie, rating)
    """

    movies_file = open(f, 'r')

    user_ratings = {}
    for line in movies_file.readlines():
        line = line.strip()

        if line:
            movie_info, rating, user_id = line.split("|")
            user_ratings.setdefault(user_id, []).append((movie_info, float(rating)))

    return user_ratings

user_ratings = read_user_ratings("movieRatingSample.txt")
print(user_ratings)

# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    """
    Returns the top genre that a user likes
    based on the user's ratings.
    """

    user_movies = user_to_movies.get(user_id, [])

    user_genre = {}
    for movie, _ in user_movies:
        genre = movie_to_genre.get(movie, None)
        if genre:
            user_genre.setdefault(genre, []).append(movie)
    
    favorite_genre = max(user_genre, key=lambda x: len(user_genre[x]))

    return favorite_genre

user_genre = get_user_genre("1", user_ratings, movie_to_genre)
print(user_genre)

# 4.3
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    """
    Returns a dictionary of movie-to-average
    ratings of the 3 most popular movies from
    the user's favorite genre, that the user
    has not rated.
    """

    favorite_genre = get_user_genre(user_id, user_to_movies, movie_to_genre)
    genre_movies = genre_to_movies.get(favorite_genre, [])
    user_movies = [movie for movie, _ in user_to_movies.get(user_id, [])]

    recommended_movies = {}
    for movie in genre_movies:
        if movie not in user_movies:
            recommended_movies[movie] = movie_to_average_rating.get(movie, 0)

    recommended_movies = get_popular_movies(recommended_movies, 3)

    return recommended_movies

recommended_movies = recommend_movies("1", user_ratings, movie_to_genre, average_ratings)
print(recommended_movies)