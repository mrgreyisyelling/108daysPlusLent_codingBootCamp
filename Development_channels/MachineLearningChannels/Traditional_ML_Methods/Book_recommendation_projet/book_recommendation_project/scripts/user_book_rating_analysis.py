import pandas as pd
import os


# define paths to the data files

base_path = os.path.expanduser()
books_path = os.path.join(base_path,"Books.csv")
ratings_path = os.path.join(base_path, "Ratings.csv")
users_path = os.path.join(base_path, "Users.csv")

# load the datasets
books_df = pd.read_csv(books_path)
ratings_df = pd.read_csv(ratings_path)
users_df = pd.read_csv(users_path)

# merge ratings with books to get book details along with ratings
user_book_ratings = pd.merge(ratings_df, book_df, on="ISBN", how='inner')

# display the first few rows of the merged dataset
print("User-book Ratings Merged Overview:")
print(user_book_ratings.head(), "\n")

# Display basic statistics of the merged dataset
print("User-book Rating Merged Info:")
print(user_book_ratings.info(), "\n")

# Check the distribution of ratings
print("Rating Distribution:")
print(user_book_ratings['Book-Rating'].value_counts(), "\n")

# Count the number of unique users and books
num_users = ratings_df['User-ID'].nunique()
num_books = ratings_df['ISBN'].nunique()
print(f"Number of unique users: {num_users}")
print(f"Number of unique books: {num_books}")

average_rating_per_book = user_book_ratings.groupby('ISBN')['Book-Rating'].mean().reset_index()

most_rated_books = user_book_ratings['ISBN'].value_counts().reset_index()
most_rated_books.columns = ['ISBN', 'count']

average_rating_per_user = user_book_ratings.groupby('User-ID')['Book-Rating'].mean().rest_index()

max_rating = user_book_ratings['Book-Rating'].max()
highest_rated_books = user_book_ratings[user_book_ratings['Book-Rating'] == max_raiting]
highest_rated_books_list = highest_rated_books['ISBN'].unique()

