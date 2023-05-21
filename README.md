# Mercor_Ml
# Clothing Recommendation System

The Clothing Recommendation System is a machine learning-based solution that provides ranked suggestions for similar clothing items based on their descriptions. It allows users to input a text description of a clothing item and returns a JSON response with ranked links to similar items from different websites.

## Project Overview

The project follows the following steps to provide clothing recommendations:

1. Data Collection and Preprocessing:
   - Web scraping tools are used to gather a dataset of clothing item descriptions.
   - The collected data is preprocessed by cleaning the text and removing unwanted characters, converting to lowercase, tokenizing, and removing stopwords.

2. Feature Extraction:
   - A method is developed to extract useful features from the preprocessed descriptions.
   - This step helps to represent the clothing items in a format suitable for similarity comparison.

3. Similarity Measurement:
   - The system computes the similarity between the input text description and the descriptions in the dataset.
   - It utilizes techniques such as cosine similarity, Levenshtein distance, or word embeddings to measure the similarity.

4. Ranking and Result Generation:
   - The system ranks the clothing items based on their similarity to the input description.
   - It returns a JSON response with the top-N most similar items, including their names, descriptions, and links.

## Project Structure

The project consists of the following components:

- `extract.py`: The main Python code file that extracts the data from the web.
- `dataset.json`: A JSON file containing a dataset of clothing items with their name, description, and link.
- `Meas_rank.py`: A Python file which implements the main function where whatever we provide a string with text about clothes it will give us a list of websites (I have included just 2 ).
- `README.md`: This README file.
- `Meas_rank_gcp.py`: This file is similar to last one only difference is that the clothing_suggestions function is the entry point for the Google Cloud Function.
-  It parses the input text from the request JSON payload,
-  loads the dataset from a JSON file, and then extracts features, computes similarity, and gets ranked results as before.
-   The function then creates a JSON response with the ranked suggestions and returns
## Prerequisites

- Python 3.10 or higher
- The required Python packages specified in `requirements.txt`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/clothing-recommendation-system.git```
   
 2.Navigate to the project directory:
     ```bash
     cd clothing-recommendation-system```
3.Create a virtual environment (optional but recommended):
       ```bash
        python -m venv venv
       source venv/bin/activate```

4.Install the required dependencies:
      ```bash
         pip install -r requirements.txt```
      
