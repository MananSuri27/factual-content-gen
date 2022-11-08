from newspaper import Article
from googlesearch import search
import re

def scraper(query):
    links = search(query, num_results = 10)

    docs = []


    for link in links:
        try:
            article = Article(link)
            article.download()
            article.parse()
            sentences = re.split('\. |\n', article.text)
            docs += sentences
        except:
            print("blocked", link)

    print("Scraped ",query, " with ", len(docs), " sentences.")
    
    return docs





