

```markdown
# Hotel Recommendation System

## Overview
This project aims to build a hotel recommendation system using Python and various libraries such as Pandas, Streamlit, and Scikit-learn. The system utilizes hotel data along with city information to provide recommendations based on user preferences.

## Project Structure
- **Datasets**:
  - **Hotel Data**: Contains information about hotels including names, locations, ratings, and reviews.
  - **City Data**: Contains geographical information about cities, including latitude and longitude.

## Data Sources
- Hotel Data: [Source of your hotel data, e.g., a CSV file or API]
- City Data: [Source of your city data, e.g., a CSV file or API]

## Features
1. **Hotel Recommendation**: Users can receive hotel suggestions based on their preferences.
2. **Nearby Attractions**: Future enhancements will include recommendations for nearby attractions based on the hotel location.
3. **Hotel Comparison**: Users will be able to compare different hotels based on ratings and reviews.

## Data Processing
The merging of hotel and city datasets is performed based on the last word of the "Place" column in the hotel data. The process is implemented using Pandas.

### Steps to Merge Datasets
1. **Extract the Last Word**: The last word from the "Place" column in the hotel dataset is extracted to identify the corresponding city.
2. **Merge the Datasets**: The hotel dataset is merged with the city dataset on the extracted city names.

### Sample Code
The following code snippet illustrates the merging process:

```python
import pandas as pd

# Load hotel and city data into DataFrames
hotel_df = pd.read_csv('hotel_data.csv')
city_df = pd.read_csv('city_data.csv')

# Extract last word from the Place column
hotel_df['City'] = hotel_df['Place'].str.split().str[-1]

# Merge the DataFrames
merged_df = hotel_df.merge(city_df, how='left', left_on='City', right_on='city')

# Select relevant columns for final output
final_df = merged_df[['Hotel Name', 'Place', 'Description', 'Condition', 'Rating', 'Total Reviews', 'lat', 'lng']]
```

## Requirements
- Python 3.x
- Pandas
- Streamlit
- Scikit-learn

## Installation
1. Clone the repository:
   ```
   git clone [repository-url]
   cd [repository-directory]
   ```
2. Install the required packages:
   ```
   pip install pandas streamlit scikit-learn
   ```

## Running the Application
To run the hotel recommendation system, use the following command:
```
streamlit run [your_app_file.py]
```

## Future Enhancements
- Implement a user interface for input preferences.
- Add functionality for user reviews and ratings.
- Integrate a geolocation API for real-time attraction data.


```

