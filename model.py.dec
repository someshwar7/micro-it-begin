# Step 1: Import Libraries
import nltk
import string
import random
import pandas as pd
from nltk.corpus import movie_reviews, stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

# Step 2: Download NLTK Resources
nltk.download('movie_reviews')
nltk.download('stopwords')

# Step 3: Load and Prepare Dataset
documents = [(movie_reviews.raw(fileid), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

# Convert to DataFrame
df = pd.DataFrame(documents, columns=['text', 'label'])

# Step 4: Preprocess Text
def preprocess_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    tokens = text.split()
    stop_words = stopwords.words('english')
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

df['clean_text'] = df['text'].apply(preprocess_text)

# Step 5: Split Data
X = df['clean_text']
y = df['label']

vectorizer = TfidfVectorizer(max_features=5000)
X_vect = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.2, random_state=42)

# Step 6: Train Model
model = MultinomialNB()
model.fit(X_train, y_train)

# Step 7: Evaluate Model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 8: Test on New Input
def predict_sentiment(text):
    cleaned = preprocess_text(text)
    vect = vectorizer.transform([cleaned])
    return model.predict(vect)[0]

# Example
print("\nTest Prediction:")
print("Sentiment:", predict_sentiment("This movie was absolutely wonderful and touching."))
print("Sentiment:", predict_sentiment("I hated everything about this movie."))
