# Swiggy-s-Restaurant-Recommendation-System-using-Streamlit-

### Problem Statement
The objective is to build a Restaurant Recommendation System based on restaurant data provided in a CSV file.
The system recommends restaurants to users based on:
 * City
 * Rating
 * Cost
 * Cuisine preferences
The application uses similarity measures to generate personalized recommendations.
It also features a simple and interactive Streamlit web interface to display results to users.
### Technologies Used
Python
Pandas
Scikit-learn
Streamlit
Pickle (for model saving/loading)
### Skills Takeaway
- Data Preprocessing
- One-Hot Encoding
- Clustering (K-Means, Cosine Similarity, etc.)
- Streamlit App Development
- Python Programming

## Project Approach
The dataset is provided as a CSV file with the following columns:
['id', 'name', 'city', 'rating', 'rating_count', 'cost', 'cuisine', 'lic_no', 'link', 'address', 'menu']

Categorical Features: name, city, cuisine

Numerical Features: rating, rating_count, cost

1. Data Understanding and Cleaning
Duplicate Removal: Identified and dropped duplicate rows.

Handling Missing Values: Imputed or dropped rows with missing values.

Data Saving: Saved the cleaned data to a new CSV file (cleaned_data.csv).

2. Data Preprocessing
Encoding: Applied One-Hot Encoding to categorical features (name, city, cuisine).

Model Saving: Saved the encoder as a Pickle file (encoder.pkl).

Numerical Data: Ensured all features are numerical after encoding.

Data Saving: Created a preprocessed dataset (encoded_data.csv).

Index Matching: Ensured the indices of cleaned_data.csv and encoded_data.csv match.

3. Recommendation Methodology
Clustering/Similarity:

Used K-Means Clustering or Cosine Similarity to find similar restaurants based on user input.

Computations were performed on the encoded dataset.

Result Mapping:

Mapped the recommendation results back to the non-encoded dataset (cleaned_data.csv) for user-friendly display.

4. Streamlit Application
User Input: Accepted user preferences like city, cuisine, rating, price, etc.

Recommendation Engine: Processed user input, queried the encoded dataset, and generated recommendations.

Output: Displayed recommended restaurants using data from cleaned_data.csv in an easy-to-read
