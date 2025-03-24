import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import spacy

# Download NLTK data
nltk.download('vader_lexicon')

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Load Spacy model
nlp = spacy.load('en_core_web_sm')

def analyze_sentiment(text):
    sentiment = sia.polarity_scores(text)
    return sentiment

def process_text(text):
    doc = nlp(text)
    return [(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop) for token in doc]

if __name__ == "__main__":
    sample_text = "The president's policies have greatly improved the economy."
    sentiment = analyze_sentiment(sample_text)
    processed_text = process_text(sample_text)
    print("Sentiment Analysis:", sentiment)
    print("Processed Text:", processed_text)