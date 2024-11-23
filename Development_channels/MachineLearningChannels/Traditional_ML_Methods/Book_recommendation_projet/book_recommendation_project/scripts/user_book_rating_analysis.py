import pandas as pd
import os


# define paths to the data files

base_path = os.path.expanduser("/home/mike/Documents/Development_space/Self_Training_with_the_AI/Development_channels/MachineLearningChannels/Traditional_ML_Methods/Book_recommendation_projet/book_recommendation_project/raw_data/")
books_path = os.path.join(base_path,"Books.csv")
ratings_path = os.path.join(base_path, "Ratings.csv")
users_path = os.path.join(base_path, "Users.csv")

# load the datasets
books_df = pd.read_csv(books_path)
ratings_df = pd.read_csv(ratings_path)
users_df = pd.read_csv(users_path)


# Display some basic statistics
print("Books DataFrame Info:")
print(books_df.info(), "\n")

print("Books DataFrame Overview:")
print(books_df.head(10), "\n")
print("Books DataFrame Shape:", books_df.shape, "\n")

print("Ratings DataFrame Info:")
print(ratings_df.info(), "\n")

print("Ratings DataFrame Overview:")
print(ratings_df.head(10), "\n")
print("Ratings DataFrame Shape:", ratings_df.shape, "\n")

# Determine the number of null ratings
null_ratings_count = ratings_df['Book-Rating'].isnull().sum()
print("Number of null ratings in Ratings DataFrame:", null_ratings_count, "\n")

print("Users DataFrame Info:")
print(users_df.info(), "\n")

print("Users DataFrame Overview:")
print(users_df.head(10), "\n")
print("Users DataFrame Shape:", users_df.shape, "\n")


# merge ratings with books to get book details along with ratings
user_book_ratings = pd.merge(ratings_df, books_df, on="ISBN", how='inner')
explicit_ratings = user_book_ratings[user_book_ratings['Book-Rating'] != 0]

# display the first few rows of the merged dataset
print("User-book Ratings Merged Overview:")
print(explicit_ratings.head(), "\n")

# Display basic statistics of the merged dataset
print("User-book Rating Merged Info:")
print(explicit_ratings.info(), "\n")

# Check the distribution of ratings
print("Rating Distribution:")
print(explicit_ratings['Book-Rating'].value_counts(), "\n")

# Count the number of unique users and books
num_users = explicit_ratings['User-ID'].nunique()
num_books = explicit_ratings['ISBN'].nunique()
num_explicit_ratings = explicit_ratings.shape[0]
print(f"Number of unique users: {num_users}","\n")
print(f"Number of unique books: {num_books}","\n")
print(f"Number of explicit ratings: {num_explicit_ratings}","\n")

average_rating_per_book = explicit_ratings.groupby('ISBN')['Book-Rating'].mean().reset_index()
print(" ")
print("Average Rating Per Book")
print(average_rating_per_book.head(10),"\n")

print(" ")
print("Most Rated Books")
most_rated_books = explicit_ratings['ISBN'].value_counts().reset_index()
most_rated_books.columns = ['ISBN', 'count']
print(most_rated_books.head(10),"\n")


print(" ")
print("Average Rating Per user")
average_rating_per_user = explicit_ratings.groupby('User-ID')['Book-Rating'].mean().reset_index()
print(average_rating_per_user.head(10),"\n")

max_rating = explicit_ratings['Book-Rating'].max()-3
highest_rated_books = explicit_ratings[explicit_ratings['Book-Rating'] >= max_rating]
most_highest_rated_books = highest_rated_books['ISBN'].value_counts().reset_index()
 
print(" ")
print("Most Highest Rated Books")
print(most_highest_rated_books.head(10),"\n")

print("How many users have at least one of the highest rated books in their set?")
users_with_highest_rated_books = highest_rated_books['User-ID'].nunique()
print(users_with_highest_rated_books,"\n")
print(users_with_highest_rated_books/num_users*100,"% of users have at least one of the highest rated books in their set","\n")

print("If someone has the most highest rated book in their set, what are the most common other books in their set?")
users_with_most_highest_rated_book = highest_rated_books[highest_rated_books['ISBN'] == most_highest_rated_books['ISBN'][0]]['User-ID'].unique()
book_collection_of_people_with_highest_rated_book = highest_rated_books['User-ID'].isin(users_with_most_highest_rated_book)
remainder_of_collection = book_collection_of_people_with_highest_rated_book[book_collection_of_people_with_highest_rated_book['ISBN'] != most_highest_rated_books['ISBN'][0]]['ISBN'].value_counts().reset_index()
number_of_users_with_firstandsecond_high = highest_rated_books[highest_rated_books['ISBN'] == remainder_of_collection['ISBN'][0]]['User-ID'].nunique()


