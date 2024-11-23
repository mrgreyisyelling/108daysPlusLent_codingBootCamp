import pandas as pd
import os

# Define paths to the data files
base_path = os.path.expanduser("/home/mike/Documents/Development_space/Self_Training_with_the_AI/Development_channels/MachineLearningChannels/Traditional_ML_Methods/Book_recommendation_projet/book_recommendation_project/raw_data/")
books_path = os.path.join(base_path, "Books.csv")
ratings_path = os.path.join(base_path, "Ratings.csv")
users_path = os.path.join(base_path, "Users.csv")

# Load the datasets
books_df = pd.read_csv(books_path)
ratings_df = pd.read_csv(ratings_path)
users_df = pd.read_csv(users_path)

# Display the first few rows of each dataset to get an overview

# Display some basic statistics
print("Books DataFrame Info:")
print(books_df.info(), "\n")

print("Books DataFrame Overview:")
print(books_df.head(), "\n")

print("Ratings DataFrame Info:")
print(ratings_df.info(), "\n")

print("Ratings DataFrame Overview:")
print(ratings_df.head(), "\n")

print("Users DataFrame Info:")
print(users_df.info(), "\n")

print("Users DataFrame Overview:")
print(users_df.head(), "\n")
