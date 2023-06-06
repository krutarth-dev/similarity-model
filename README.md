# similarity-model

The goal of the project is to find the most similar data to a given query data using different similarity algorithms. The project follows these steps:

## 1. Load and preprocess the dataset: 
The dataset is loaded from a CSV file using pandas. Missing values in the 'short_description' column are filled with an empty string.

## 2. Feature Extraction:
The 'short_description' column is used as the text data for feature extraction. The TfidfVectorizer from scikit-learn is used to convert the text data into a TF-IDF matrix representation. This matrix captures the importance of each word in each document.

## 3. Similarity Computation:
Four similarity algorithms are applied to the TF-IDF matrix: cosine similarity, Euclidean distance, Manhattan distance, and Jaccard similarity. These algorithms measure the similarity or distance between pairs of documents in the dataset.

## 4. Building the Model:
The function `find_similar_data` takes a query data and a similarity metric as inputs. It computes the similarity scores between the query data and all documents in the dataset using the specified metric. It then returns the top 5 most similar documents based on the similarity scores.

## 5. Usage and Evaluation: 
The code demonstrates the usage of the `find_similar_data` function by providing a sample query data. It calls the function for each similarity metric and prints the resulting similar data.

The project allows you to easily find the most similar data to a given query data by utilizing different similarity algorithms. You can extend and customize the project according to your specific requirements, such as using a different dataset or adding more similarity metrics.

