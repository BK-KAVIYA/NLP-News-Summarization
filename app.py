from flask import Flask, render_template, request
import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    url = request.form['url']

    article = Article(url)
    article.download()
    article.parse()

    article.nlp()

    title = article.title
    authors = article.authors
    publish_date = article.publish_date
    summary = article.summary

    analysis = TextBlob(article.text)
    polarity = analysis.polarity
    sentiment = "positive" if analysis.sentiment.polarity > 0 else "negative" if analysis.sentiment.polarity < 0 else "neutral"

    result_html = """
        <p><strong>Title:</strong> {}</p>
        <p><strong>Authors:</strong> {}</p>
        <p><strong>Publication Date:</strong> {}</p>
        <p><strong>Summary:</strong> {}</p>
        <p><strong>Polarity:</strong> {}</p>
        <p><strong>Sentiment:</strong> {}</p>
    """.format(title, authors, publish_date, summary, polarity, sentiment)

    return result_html

if __name__ == '__main__':
    app.run(debug=True)
