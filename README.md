# News Category Classifier

A ML project that performs multiclass classification to categorize news articles into categories using **TfidfVectorizer** and a **Naive Bayes** model. Built with **scikit-learn** and deployed using **Streamlit**.

---

## Features

- Text classification using **TF-IDF + Multinomial Naive Bayes**
- Visualizations of dataset distribution
- Word clouds for each news category
- Model saved with **joblib**
- Interactive web app built with **Streamlit**

---

## Project Structure

```
news-category-classifier/
│
├── data/
│   └── bbc_news_dataset.csv            # Dataset used for training
│
├── environments/
│   └── environment.yml                 # Conda environment setup
│
├── models/
│   └── news_classifier_model.joblib    # Trained ML model
│
├── .gitignore
├── app.py                              # Streamlit web application
├── main.ipynb                          # Main Jupyter notebook code
└── README.md                           # Project documentation
```

---

## Model Details

**Pipeline used:**

- `TfidfVectorizer(stop_words="english")`
- `MultinomialNB()`

This combination works well for text classification tasks like news categorization.

---

## Setup Instructions


### 1 Create Environment

```bash
conda env create -f environments/environment.yml
conda activate news-category-classifier
```

---

### 2 Train the Model

Make sure the dataset file is present in data/bbc_news_dataset.csv:

Open main.ipynb on Jupyter Notebook and run all cells to train and save the model.

This will generate:

```
models/news_classifier_model.joblib
```

---

### 3 Run the Streamlit App

```bash
streamlit run app.py
```

Then open your browser at:

```
http://localhost:8501
```

---

## Deploy Online (Streamlit Community Cloud)

1. Push the project to GitHub  
2. Visit **https://share.streamlit.io**  
3. Select your repository  
4. Set **Main file path** to:

```
app.py
```
5. Click **Deploy**

---

## Example Usage

Input:

> "The government announced new economic policies today."

Output:

```
Predicted Category: Politics
```

---

## Tech Stack

- Python 3.11  
- scikit-learn  
- pandas & numpy  
- matplotlib & seaborn  
- wordcloud  
- Streamlit  

---

## Author

Made with ❤️ by [Pratyoos](https://github.com/pratyoos)