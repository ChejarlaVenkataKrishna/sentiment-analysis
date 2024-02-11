from textblob import TextBlob


def analyze_sentiment(text):
    analysis = TextBlob(text)
    
    # Check the polarity of the sentiment
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'
# Example text for sentiment analysis
text = input("enter sentiment:-")
# Analyzing sentiment
sentiment = analyze_sentiment(text)
print("Sentiment of the text is:", sentiment)
