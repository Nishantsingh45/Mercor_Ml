import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_features(dataset):
    # Extract the descriptions from the dataset
    descriptions = [data['description'] for data in dataset]
    
    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    
    # Compute the TF-IDF features
    features = vectorizer.fit_transform(descriptions)
    
    return vectorizer, features

def compute_similarity(input_text, vectorizer, features):
    # Transform the input text into a vector using the same vectorizer
    input_vector = vectorizer.transform([input_text])
    
    # Compute the cosine similarity between the input vector and dataset vectors
    similarity_scores = cosine_similarity(input_vector, features)
    
    return similarity_scores

def get_ranked_results(similarity_scores, dataset, top_n=5):
    # Get the indices of the most similar items (descending order)
    most_similar_indices = np.argsort(similarity_scores, axis=1)[:, ::-1]
    
    # Get the top-N most similar item indices
    top_indices = most_similar_indices[0][:top_n]
    
    # Get the corresponding details (name and link) for the top-N items
    ranked_results = [{'name': dataset[idx]['name'], 'link': dataset[idx]['link']} for idx in top_indices]
    
    return ranked_results

def clothing_suggestions(request):
    # Parse the request JSON payload
    request_json = request.get_json()
    
    # Extract the input text from the request
    input_text = request_json['input_text']
    
    # Load the dataset from a JSON file
    with open('dataset.json', 'r') as file:
        dataset = json.load(file)
    
    # Extract features from the dataset
    vectorizer, features = extract_features(dataset)
    
    # Compute similarity between input text and dataset
    similarity_scores = compute_similarity(input_text, vectorizer, features)
    
    # Get ranked results
    ranked_results = get_ranked_results(similarity_scores, dataset, top_n=5)
    
    # Create a JSON response with ranked suggestions
    response = {
        "suggestions": ranked_results
    }
    
    # Return the response as JSON
    return response
