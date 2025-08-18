# Swiggy-s-Restaurant-Recommendation-System-using-Streamlit-

This project is a Restaurant Recommendation System built using Python and Streamlit. It recommends restaurants to users based on their preferences for city, rating, cost, and cuisine. The system leverages similarity measures to generate personalized recommendations and presents them through an interactive web interface.

# Technologies Used

- Language: Python

- Libraries:

     - Pandas

     - Scikit-learn

     - Streamlit

     - Pickle

- Methodology: One-Hot Encoding, Cosine Similarity
  
#  Key Features 

- Personalized Recommendations: Recommends restaurants based on user-defined criteria.

- Interactive Web App: A user-friendly interface built with Streamlit.

- Data Processing Pipeline:

     - Handles missing values and duplicate records.

     - Applies One-Hot Encoding to categorical data.

- Similarity-Based Recommendation: Utilizes K-Means Clustering or Cosine Similarity to find similar restaurants.

# Project Workflow

The project follows a structured workflow to ensure a robust and functional recommendation system.

1. Data Understanding and Cleaning:

  - The raw data is loaded from a CSV file.

  - Duplicates and missing values are handled to create a clean dataset.

2. Data Preprocessing:

  - Categorical features like name, city, and cuisine are converted into a numerical format using One-Hot Encoding.

  - The encoded data is saved for use in the recommendation algorithm.

3. Recommendation Methodology:

   - The core of the system uses a clustering or similarity algorithm to find restaurants that are similar to the user's input.

   - The results are mapped back to the original, non-encoded data for easy display.

4. Streamlit Web Application:

   - The Streamlit app takes user input for city, cuisine, rating, and cost.

   - It processes this input, runs the recommendation logic, and displays the recommended restaurants.

#  How to Run the App
Follow these simple steps to get the app running on your local machine.

1. Clone the Repository:

git clone https://github.com/Swiggy-s-Restaurant-Recommendation-System-using-Streamlit.git
cd Swiggy-s-Restaurant-Recommendation-System-using-Streamlit

2. Install Dependencies:

Make sure you have Python installed.

Install the required libraries from requirements.txt.
pip install -r requirements.txt

3. Run the Streamlit App:

From the project directory, execute the following command:

streamlit run swiggy.py
The application will automatically open in your web browser.

