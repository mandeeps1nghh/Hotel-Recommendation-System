import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Initialize session state
if 'user' not in st.session_state:
    st.session_state['user'] = None

# Custom CSS for styling
def apply_css():
    st.markdown(
        """
        <style>
        /* Set the background color for the entire app */
        .reportview-container {
            background: #f0f0f5;  /* Light gray background */
        }
        
        /* Style the sidebar */
        .sidebar .sidebar-content {
            background: #ffffff;  /* White background for sidebar */
            border-radius: 10px;  /* Rounded corners */
            padding: 10px;  /* Padding inside the sidebar */
        }
        
        /* Style headers */
        h2 {
            color: #333333;  /* Dark gray color for headers */
        }
        
        /* Style buttons */
        .stButton > button {
            background-color: #4CAF50;  /* Green background for buttons */
            color: white;  /* White text color */
            border: none;  /* Remove border */
            border-radius: 5px;  /* Rounded corners */
            padding: 10px 20px;  /* Padding inside the button */
            cursor: pointer;  /* Pointer cursor on hover */
        }
        
        /* Change button color on hover */
        .stButton > button:hover {
            background-color: #45a049;  /* Darker green on hover */
        }
        
        /* Style the dataframe */
        .dataframe {
            border-collapse: collapse;  /* Collapse borders */
            width: 100%;  /* Full width */
        }
        
        .dataframe th, .dataframe td {
            border: 1px solid #dddddd;  /* Light gray border */
            text-align: left;  /* Left align text */
            padding: 8px;  /* Padding inside cells */
        }
        
        .dataframe th {
            background-color: #f2f2f2;  /* Light gray background for headers */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def clean_text(text):
    return str(text).lower().strip()

def get_recommendations(hotel_name, df, hotel_vectors, feature='Rating'):
    hotel_index = df[df['Hotel Name'] == hotel_name].index[0]
    hotel_vector = hotel_vectors[hotel_index].reshape(1, -1)
    cosine_similarities = cosine_similarity(hotel_vector, hotel_vectors)
    similar_indices = cosine_similarities.argsort()[0][::-1]
    similar_indices = similar_indices[similar_indices != hotel_index]
    similar_hotels = df.iloc[similar_indices].copy()
    
    selected_city = df.loc[hotel_index, 'Place']
    similar_hotels = similar_hotels[similar_hotels['Place'] == selected_city]
    
    if feature == 'Total Reviews':
        similar_hotels['Total Reviews'] = similar_hotels['Total Reviews'].str.replace(',', '').str.split().str[0].astype(float)
    
    return similar_hotels.sort_values(by=feature, ascending=False).head(min(10, len(similar_hotels)))

def main_app():
    apply_css()  # Apply CSS styles

    # Use Streamlit's title function
    st.title("Hotel Recommendation System")
    st.header("Find Your Perfect Hotel")

    df = pd.read_csv(r'C:\Users\jasre\Downloads\kafkaa\pro\hotel_details.csv')
    df['clean_name'] = df['Hotel Name'].apply(clean_text)
    df['clean_description'] = df['description'].apply(clean_text)
    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
    df['Condition'] = df['Condition'].astype(str)

    places = sorted(df['Place'].astype(str).unique())
    selected_place = st.sidebar.selectbox("Filter by place", ['All'] + list(places))

    conditions = sorted(df['Condition'].astype(str).unique())
    selected_condition = st.sidebar.selectbox("Filter by condition", ['All'] + list(conditions))

    filtered_df = df.copy()
    if selected_place != 'All':
        filtered_df = filtered_df[filtered_df['Place'].astype(str) == selected_place]
    if selected_condition != 'All':
        filtered_df = filtered_df[filtered_df['Condition'].astype(str) == selected_condition]

    filtered_df = filtered_df.reset_index(drop=True)

    vectorizer = TfidfVectorizer(analyzer='word', lowercase=False, stop_words='english')
    text_for_vectorization = filtered_df['clean_name'].fillna('') + ' ' + filtered_df['clean_description'].fillna('')
    text_for_vectorization = text_for_vectorization.replace('', 'no_description')

    try:
        X = vectorizer.fit_transform(text_for_vectorization)
        hotel_vectors = X.toarray()

        col1, col2 = st.columns(2)
        with col1:
            hotel = st.selectbox('Select a hotel you liked:', filtered_df['Hotel Name'].tolist())
        
        with col2:
            feat = st.selectbox("Sort recommendations by:", ['Rating', 'Total Reviews'])
            if st.button('Get Recommendations'):
                if hotel:
                    st.success(f'Recommending hotels similar to {hotel}')
                    recommendations = get_recommendations(hotel, filtered_df, hotel_vectors, feat)
                    st.dataframe(recommendations[['Hotel Name', 'Place', 'Condition', 'Rating', 'Total Reviews']], width=700, height=300)
                else:
                    st.warning("Please select a hotel.")

        st.sidebar.metric("Total Hotels", len(filtered_df))
        average_rating = filtered_df['Rating'].mean()
        st.sidebar.metric("Average Rating", f"{average_rating:.2f}")

    except ValueError as e:
        st.error(f"An error occurred: {str(e)}")
        st.warning("No valid text found for creating recommendations. Please try different filter options.")

def app():
    main_app()  # Directly call main_app

if __name__ == "__main__":
    main_app()