import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from attractions import get_attractions_for_hotel


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
    st.title("Hotel Recommendation System")
    st.header("Find Your Perfect Hotel")

    # Load the CSV file
    df = pd.read_csv(r'C:\Users\jasre\Downloads\kafkaa\pro\output.csv')
    
    # Clean and prepare the DataFrame
    df['clean_name'] = df['Hotel Name'].apply(clean_text)
    df['clean_description'] = df['description'].fillna('').apply(clean_text)
    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')

    # Handle missing lat/lng values
    df['lat'].fillna(0, inplace=True)  # Fill missing lat values with 0
    df['lng'].fillna(0, inplace=True)  # Fill missing lng values with 0

    places = sorted(df['Place'].astype(str).unique())
    selected_place = st.sidebar.selectbox("Filter by place", ['All'] + list(places))

    # Use 'Condition' for filtering
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

        # Button to show nearby attractions
        if st.button('Show Nearby Attractions'):
            hotel_data = filtered_df[filtered_df['Hotel Name'] == hotel]
            if not hotel_data.empty:
                attractions_df = get_attractions_for_hotel(hotel_data.iloc[0])
                st.dataframe(attractions_df)

        st.sidebar.metric("Total Hotels", len(filtered_df))
        average_rating = filtered_df['Rating'].mean()
        st.sidebar.metric("Average Rating", f"{average_rating:.2f}")

    except ValueError as e:
        st.error(f"An error occurred: {str(e)}")
        st.warning("No valid text found for creating recommendations. Please try different filter options.")


def app():
    main_app()

if __name__ == "__main__":
    main_app()
