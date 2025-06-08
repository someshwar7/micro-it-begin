Here's the full **README** text combining both projects, formatted cleanly for you to save as a single `README.md` file:

---

# Projects: File Encryption/Decryption Tool & Sentiment Analysis (IMDB)

---

## Project 1: File Encryption/Decryption Tool 🔐

### Description

A Python command-line tool to encrypt and decrypt files securely using symmetric encryption (Fernet). It transforms files into an unreadable format unless decrypted with the correct key, protecting sensitive data.

### Features

* Generate and save encryption keys securely
* Encrypt any file type
* Decrypt encrypted files using the key
* Easy-to-use command-line interface
* Based on Python’s `cryptography` package

### Installation

```bash
pip install cryptography
```

### Usage

1. Run the script:

   ```bash
   python model2.py
   ```
2. Choose from the menu:

   * Generate a key
   * Encrypt a file
   * Decrypt a file
3. Follow prompts to specify file names.

### Important Notes

* Keep your key (`secret.key`) safe; losing it means you cannot decrypt files.
* Do not share the key and encrypted file together.
* Supports all file formats (PDF, images, text, etc.).

---

## Project 2: Sentiment Analysis (IMDB Dataset) 💬

### Description

This project uses machine learning to classify movie reviews from the IMDB dataset as positive or negative. It applies NLP preprocessing, TF-IDF vectorization, and Logistic Regression to analyze sentiment.

### Features

* Text preprocessing with NLTK
* TF-IDF vectorization for feature extraction
* Logistic Regression classifier
* Metrics: accuracy, precision, recall, and f1-score
* Predict sentiment on custom user input

### Installation

```bash
pip install nltk scikit-learn
```

### Usage

1. Run the script:

   ```bash
   python sentiment_model.py
   ```
2. View evaluation metrics after training.
3. Enter custom reviews to get sentiment predictions.

### Sample Output

```
Accuracy: 0.8425

Classification Report:
               precision    recall  f1-score   support

         neg       0.86      0.85      0.86       218
         pos       0.83      0.83      0.83       182

    accuracy                           0.84       400
```

---

## Author

**Someshwar V**
Department of Artificial Intelligence and Data Science

---

You can copy this as your `README.md` for both projects in one place. Let me know if you want me to generate the actual `.md` file!
