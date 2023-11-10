# Comparing Similarity Scores
# Emma 
# 8 November 2023

# Calculate similarity scores netweem two people
# Create two lists that represent the movies that people like

ubials_favourite_movies = [
    "The Matrix",
    "Avengers: Infinity War",
    "The Empire Strikes Back",
    "Infernal Affairs",
    "Rogue One"
]

bens_favourite_movies = [
    "Thomas and Friends Big World Big Adventure",
    "Infernal Affairs",
    "Rogue One",
    "Spire-man: Into the Spider-verse",
    "Guardians of the Galaxy: Volume 3"
]

# Initialize the similarity score

similarity_score = 0

# Iterate through all movies in first list
for movie in ubials_favourite_movies:
    if movie in bens_favourite_movies:
        similarity_score += 1

# Display the results
print(f"Ubial and Ben have a similarity score of: {similarity_score}")
