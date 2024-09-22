# recommendations.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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
