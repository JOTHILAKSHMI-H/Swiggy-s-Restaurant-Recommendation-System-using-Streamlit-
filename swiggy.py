import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

#load cleaned and encoded data 
encoded_data = pd.read_csv('final_encoded_data.csv') #Encoded numerical data

cleaned_data = pd.read_csv('cleaned_data.csv') #full restaurants data

# encoded_data = pd.read_csv('final_encoded_data.csv', encoding='ISO-8859-1', low_memory= True)#Encoded numerical data

# cleaned_data = pd.read_csv('cleaned_data.csv', on_bad_lines='skip')#full restaurants data


# function for recommendation
def recommend_restaurants(user_input, encoded_data, cleaned_data):
    
# Initialize user input with all features set to 0
    encoded_user_input = {}

# Iterate each column in encoded_df (except 'id')
    for col in encoded_data.columns:
      if col != 'id':
         encoded_user_input[col] = 0  
         
    city_col = f"city_{user_input['city']}" #city_Delhi
    if city_col in encoded_data.columns:
     encoded_user_input[city_col] = 1 # Set selected city to 1
 
    cuisine_col = f"cuisine_{user_input['cuisine']}"
    if cuisine_col in encoded_data.columns:
     encoded_user_input[cuisine_col] = 1 # set selected cuisine to 1
     
    encoded_user_input['rating'] = float(user_input['rating'])
    encoded_user_input['cost'] = float(user_input['cost'])
    encoded_user_input['rating_count'] = (user_input['rating_count'])
 #convert to dataframe
    input_df = pd.DataFrame([encoded_user_input]) 
 
 # Ensure encoded_df only contains numerical values before similarity calculation
    encoded_numeric_df =  encoded_data.drop(columns = ['id']).apply(pd.to_numeric, errors = 'coerce')   
 
    input_df.fillna(0, inplace= True)
    encoded_numeric_df.fillna(0, inplace = True)
 #compute the similarities
    similarities = cosine_similarity(input_df, encoded_numeric_df)[0] 
 
 # Get top matches
    top_indices = similarities.argsort()[::-1][:100]  # argsort() sorts the similarity scores but returns the indices
    matched_ids = encoded_data.iloc[top_indices]['id'].values
 
 #  full details from cleaned_df
    recommend_restaurants = cleaned_data[cleaned_data['id'].isin(matched_ids)]

    # Filter restaurants by the user's preferred city
    filtered_restaurants = cleaned_data[cleaned_data['city'].str.contains(user_input['city'], case=False, na=False)]

# Check if there are any results
    if filtered_restaurants.empty:
      return f"No restaurants found in {user_input['city']}."
   
    recommend_restaurants = filtered_restaurants.sort_values(by=["rating"], ascending=[False]).head(10)
    return recommend_restaurants
  
  

          
#streamlit page
  
  
st.title("🥘🥣RESTAURANT RECOMMENDATION SYSTEM")
st.sidebar.subheader('Restaurants For You')
city = st.sidebar.selectbox('Select City', cleaned_data['city'].unique())
cuisine = st.sidebar.selectbox('Select Cuisine', cleaned_data['cuisine'].unique())
rating = st.sidebar.selectbox("Select Rating", sorted(cleaned_data['rating'].unique(), reverse= True))
rating_count = st.sidebar.selectbox("Select Rating Count", cleaned_data['rating_count'].unique())
cost = st.sidebar.selectbox("Select cost", cleaned_data['cost'].unique())


if st.button('Get Recommendations'):
     user_input = {'city' : city, 'cuisine': cuisine, 'rating':rating, 'rating_count': rating_count, 'cost': cost}
     recommendations = recommend_restaurants(user_input, encoded_data, cleaned_data)
    
     if recommendations.empty:
         st.warning("No Matching Restaurants found")
     else:
         st.subheader("Top Recommended Restaurants:")
         st.dataframe(recommendations)