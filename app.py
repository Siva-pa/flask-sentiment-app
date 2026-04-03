from flask import Flask, request, render_template
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK data
nltk.download('stopwords')
nltk.download('wordnet')

app = Flask(__name__)

# Load trained model and vectorizer
model = joblib.load("sentiment_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Negative keywords for highlighting
NEGATIVE_KEYWORDS = [
    "bad", "poor", "break", "broken", "waste",
    "cheap", "worst", "damage", "damaged",
    "durable", "not worth", "very bad"
]

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    words = text.split()
    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]
    return ' '.join(words)

def highlight_keywords(review):
    highlighted = review
    for word in NEGATIVE_KEYWORDS:
        highlighted = re.sub(
            rf"\b({word})\b",
            r"<span class='highlight'>\1</span>",
            highlighted,
            flags=re.IGNORECASE
        )
    return highlighted

@app.route("/", methods=["GET", "POST"])
def home():
    sentiment = None
    confidence = None
    highlighted_review = None

    if request.method == "POST":
        review = request.form["review"]

        cleaned = clean_text(review)
        vector = tfidf.transform([cleaned])

        prediction = model.predict(vector)[0]
        probabilities = model.predict_proba(vector)[0]

        sentiment = "Positive" if prediction == 1 else "Negative"
        confidence = round(max(probabilities) * 100, 2)

        highlighted_review = highlight_keywords(review)

    return render_template(
        "index.html",
        sentiment=sentiment,
        confidence=confidence,
        review=highlighted_review
    )

if __name__ == "__main__":
    app.run(debug=True)