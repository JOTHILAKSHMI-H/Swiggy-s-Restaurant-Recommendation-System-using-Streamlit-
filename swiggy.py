import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
import urllib.parse


#load cleaned and encoded data 
encoded_data = pd.read_csv('final_encoded_data.csv') #Encoded numerical data

cleaned_data = pd.read_csv('cleaned_data.csv') #full restaurants clean data


# function for recommendation
def recommend_restaurants(user_input, encoded_data, cleaned_data):
    
   # Initialize user input with all features set to 0
    encoded_user_input = {}

   # Iterate each column in encoded_df (except 'id')
    for col in encoded_data.columns:
      if col != 'id':
         encoded_user_input[col] = 0  
         
   # for city column     
    city_name = user_input['city'].split(',')[0].strip()
    city_col = f"city_{city_name}"
    if city_col in encoded_data.columns:
        encoded_user_input[city_col] = 1
    
   # for cuisine column 
    cuisine_col_1 = f"cuisine_1_{user_input['cuisine']}"
    cuisine_col_2 = f"cuisine_2_{user_input['cuisine']}"
    if cuisine_col_1 in encoded_data.columns:
        encoded_user_input[cuisine_col_1] = 1
    elif cuisine_col_2 in encoded_data.columns:
        encoded_user_input[cuisine_col_2] = 1
        
   # numeric features 
    encoded_user_input['rating'] = float(user_input['rating'])
    encoded_user_input['cost'] = float(user_input['cost'])
    encoded_user_input['rating_count'] = (user_input['rating_count'])
    
   #convert to dataframe
    input_df = pd.DataFrame([encoded_user_input]) 
 
   # Ensure encoded_df only contains numerical values before similarity calculation
 
    encoded_numeric_df =  encoded_data.drop(columns = ['id']).apply(pd.to_numeric, errors = 'coerce')   
    input_df.fillna(0, inplace= True)
    encoded_numeric_df.fillna(0, inplace = True)
    
   # Normalize both datasets (same scaler)
    scaler = MinMaxScaler()
    scaler.fit(encoded_numeric_df)  # Fit only on data, not input
    encoded_scaled = scaler.transform(encoded_numeric_df)
    input_scaled = scaler.transform(input_df)
    
   #compute the similarities
    similarities = cosine_similarity(input_scaled, encoded_scaled)[0] 
 
   # Get top matches
    top_indices = similarities.argsort()[::-1][:10]  # argsort() sorts the similarity scores but returns the indices
    matched_ids = encoded_data.iloc[top_indices]['id'].values
 
    recommend_restaurants = cleaned_data[cleaned_data['id'].isin(matched_ids)]
    recommend_restaurants = recommend_restaurants.sort_values(by=["rating"], ascending=False)
    
    return recommend_restaurants
  

          
#streamlit page
  
  
st.title("🥘🥣RESTAURANT RECOMMENDATION SYSTEM")
st.sidebar.subheader('🧭Restaurants For You👇')
city = st.sidebar.selectbox(' 📍Select City', cleaned_data['city'].unique())
cuisine = st.sidebar.selectbox('🍽️Select Cuisine', cleaned_data['cuisine'].unique())
rating = st.sidebar.selectbox("⭐Select Rating", sorted(cleaned_data['rating'].unique(), reverse= True))
rating_count = st.sidebar.selectbox("🗳️Select Rating Count", cleaned_data['rating_count'].unique())
cost = st.sidebar.selectbox("💰Select cost", cleaned_data['cost'].unique())


if st.button('✨Get Recommendations'):
     user_input = {'city' : city, 'cuisine': cuisine, 'rating':rating, 'rating_count': rating_count, 'cost': cost}
     recommendations= recommend_restaurants(user_input, encoded_data, cleaned_data)
     
     if isinstance(recommendations, str):
         st.warning(recommendations)
     elif recommendations.empty:
         st.warning("No Matching Restaurants found")
     else:
         st.subheader("Top Recommended Restaurants:")
         #st.dataframe(recommendations)
         for _, row in recommendations.iterrows():
            with st.container():
               st.markdown(f"### 🍴 {row['name']}")
               st.markdown(f"📍 **City:** {row['city']}  |  🍽️ **Cuisine:** {row['cuisine']}")
               st.markdown(f"⭐ **Rating:** {row['rating']} ({row['rating_count']} reviews)")
               st.markdown(f"💰 **Cost for Two:** {row['cost']}")
               st.markdown(f"📬 **Address:** {row['address']}")
    
               address_link = "https://www.google.com/maps/search/" + urllib.parse.quote(row['address'])
               st.markdown(f"📌 [Open in Google Maps]({address_link})")
    
               st.markdown(f"[🔗 View Online]({row['link']})")
               st.markdown("---")
  
     if recommendations.empty:
         st.warning("No Matching Restaurants found")
     else:
         st.subheader("Top Recommended Restaurants:")
         st.dataframe(recommendations)
