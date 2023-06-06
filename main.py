import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances, manhattan_distances, pairwise_distances

# Step 1: Load and preprocess the dataset
df = pd.read_csv('output.csv')

# Step 2: Feature Extraction
text_data = df['short_description'].fillna('')  # Fill missing values with empty string
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(text_data)

# Step 3: Similarity Computation
cosine_sim = cosine_similarity(tfidf_matrix)
euclidean_dist = euclidean_distances(tfidf_matrix)
manhattan_dist = manhattan_distances(tfidf_matrix)
jaccard_sim = pairwise_distances(tfidf_matrix, metric='jaccard')

# Step 4: Build the Model
def find_similar_data(query_data, similarity_metric):
    # Compute similarity scores for the query_data
    query_vector = tfidf_vectorizer.transform([query_data])
    similarity_scores = similarity_metric(query_vector, tfidf_matrix)
    
    # Get the indices of the most similar data points
    most_similar_indices = similarity_scores.argsort()[::-1][:5]  # Change the value as per your requirement
    
    # Return the most similar data points
    return df.iloc[most_similar_indices]

# Step 5: Usage and Evaluation
query_data = "Your query data"

similar_data_cosine = find_similar_data(query_data, cosine_sim)
similar_data_euclidean = find_similar_data(query_data, euclidean_dist)
similar_data_manhattan = find_similar_data(query_data, manhattan_dist)
similar_data_jaccard = find_similar_data(query_data, jaccard_sim)

# Print the similar data
print("Similar data (Cosine similarity):\n", similar_data_cosine)
print("Similar data (Euclidean distance):\n", similar_data_euclidean)
print("Similar data (Manhattan distance):\n", similar_data_manhattan)
print("Similar data (Jaccard similarity):\n", similar_data_jaccard)
