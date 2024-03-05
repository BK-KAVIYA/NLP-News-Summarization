import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')


url = 'https://www.dailymirror.lk/top-story/Parliament-Central-Bank-set-to-discuss-salary-hike/155-278107'

article = Article(url)
article.download()
article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Author: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')

analysis = TextBlob(article.text)
print(analysis.polarity)
print(f'Sentiment:{"positive" if analysis.sentiment.polarity > 0 else "negative" if analysis.sentiment.polarity < 0 else "neutral"}')


