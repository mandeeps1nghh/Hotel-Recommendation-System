# Hotel Recommendation System

## Overview
The Hotel Recommendation System is a web application built using Python and Streamlit that helps users find hotels based on their preferences. The application utilizes machine learning techniques to recommend similar hotels based on user-selected options and displays nearby attractions.

## Features
- **Hotel Filtering**: Users can filter hotels by place and condition.
- **Recommendations**: Get hotel recommendations based on user-selected hotels.
- **Nearby Attractions**: View nearby attractions based on the selected hotel location.
- **User-Friendly Interface**: Built with Streamlit for an interactive web application experience.

## Technologies Used
- **Python**: The programming language used for the application.
- **Pandas**: For data manipulation and analysis.
- **Requests**: For making HTTP requests to fetch data from APIs.
- **Scikit-learn**: For machine learning functionalities, including text vectorization and similarity calculations.
- **Streamlit**: For building the web application interface.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Dataset
The application uses a CSV file named `output.csv` that contains hotel information with the following columns:
- `Hotel Name`
- `Place`
- `description`
- `Condition`
- `Rating`
- `Total Reviews`
- `lat`
- `lng`

## Usage

1. Ensure you have the required CSV file (`output.csv`) in the project directory.
2. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
3. Open your web browser and go to `http://localhost:8501` to access the application.

## Code Structure
- **app.py**: The main application file that handles user interactions and displays hotel recommendations.
- **recommendations.py**: Contains functions for cleaning text and generating hotel recommendations based on user input.
- **attractions.py**: Fetches nearby attractions based on the selected hotel's latitude and longitude.

## Contributing
We welcome contributions to this project! If you have suggestions for improvements, new features, or bug fixes, please feel free to open an issue or submit a pull request. 

### How to Contribute
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request detailing your changes.

Your contributions help make this project better for everyone!


````

### Instructions for Use
1. **Create a new file** named `README.md` in your project directory.
2. **Copy and paste** the above content into the file.
3. **Modify** any sections as necessary to fit your specific project details, such as the repository URL and any additional features or acknowledgments.

