
---

# Movie Recommendation System

This project implements a movie recommendation system using data analysis, data cleaning, feature engineering, and collaborative filtering. The recommendation system is built using Python and leverages Flask and Streamlit for the user interface.

## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   ```

2. Navigate to the project directory:

   ```bash
   cd movie-recommendation-system
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - **For Windows:**
     ```bash
     .\venv\Scripts\activate
     ```
   - **For macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

5. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Download the necessary data files:

   - Download the `MOVIE RECOMMENDER NOTEBOOK.ipynb` file.
   - Create a folder named `models` and save the `movies_list.pkl` and `similarity.pkl` pickle files inside it.
   - Download the contents of the `data` folder and place them in the project directory.

7. Obtain a Movies data API key:

   - Visit [https://www.themoviedb.org/](https://www.themoviedb.org/) and sign in or create an account.
   - Generate an API key in the developer settings.
   - Replace the placeholder API key in the code with your own key.

## Running the Streamlit App

Run the Streamlit app using the following command:

```bash
streamlit run streamlit.py
```

Visit [http://localhost:8501](http://localhost:8501) in your web browser to access the Streamlit Movie Recommender System.

## Running the Flask App

Run the Flask app using the following command:

```bash
python flask_app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your web browser to access the Flask Movie Recommender System.

## Project Structure

- `MOVIE RECOMMENDER NOTEBOOK.ipynb`: Jupyter Notebook containing data analysis, cleaning, feature engineering, and recommendation system trials.
- `models/`: Folder containing pickle files (`movies_list.pkl` and `similarity.pkl`) generated from the notebook.
- `data/`: Folder containing CSV files used for data analysis.
- `requirements.txt`: List of project dependencies.
- `streamlit.py`: Streamlit implementation of the movie recommendation system.
- `flask_app.py`: Flask implementation of the movie recommendation system.

Feel free to explore and modify the code to suit your preferences!

---
.