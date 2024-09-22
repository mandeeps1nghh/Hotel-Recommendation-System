# Hotel Recommendation System

## Overview
The **Hotel Recommendation System** is a web application built using **Streamlit** that allows users to find hotels based on their preferences. The application provides recommendations based on user-selected hotels, filtered by city and condition. It utilizes text processing and cosine similarity to suggest similar hotels.

## Features
- **Filter hotels** by place and condition.
- **Get recommendations** for hotels similar to the selected hotel.
- **Display hotel details** in a user-friendly interface.
- **Custom styling** for a better user experience.

## Technologies Used
- **Python**
- **Streamlit**
- **Pandas**
- **Scikit-learn** (for text processing and similarity calculations)

## Installation

### Prerequisites
Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository
```bash
git clone https://github.com/yourusername/hotel-recommendation-system.git
cd hotel-recommendation-system
```

### Install Required Packages
It is recommended to use a virtual environment. You can install the required packages using pip:

```bash
pip install streamlit pandas scikit-learn
```

## Usage

1. **Prepare the Data**: Ensure you have a CSV file named `hotel_details.csv` with the following columns:
   - `Hotel Name`
   - `description`
   - `Rating`
   - `Condition`
   - `Place`

   Place this file in the directory specified in the code (e.g., `C:\Users\jasre\Downloads\kafkaa\pro\hotel_details.csv`).

2. **Run the Application**:
   Open your terminal, navigate to the directory containing `app.py`, and run the following command:

   ```bash
   streamlit run app.py
   ```

3. **Access the App**: After running the command, your default web browser should open with the Streamlit app. If it doesn't, you can manually navigate to `http://localhost:8501`.

## How to Use
- Use the sidebar to filter hotels by place and condition.
- Select a hotel you liked from the dropdown menu.
- Choose how to sort the recommendations (by Rating or Total Reviews).
- Click the "Get Recommendations" button to see similar hotels.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

### Steps to Contribute
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## Acknowledgments
- Thanks to the Streamlit community for their support and resources.
- Special thanks to the contributors of the libraries used in this project.

### Instructions for Use
1. **Create a File**: Save the above content in a file named `README.md` in the root directory of your project.
2. **Customize**: Update any sections as necessary, especially the repository link and any specific details about your project.

This `README.md` provides a comprehensive overview of your project, making it easier for others (or yourself in the future) to understand how to set up and use the application. If you have any specific requests or need further modifications, feel free to ask!
