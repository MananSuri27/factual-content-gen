import json
from scraper import scraper
from model import rankDocs


def generatePoints(keywords, h2, n):
    docs = scraper(keywords)

    points = {}


    for h in h2:
        p = rankDocs(h, docs, n)
        points[h] = p

    with open("outputs/"+keywords+".json", "w") as outfile:
        json.dump(points, outfile, indent=6)

keywords = "elon musk twitter takeover"

h2 = ["What is the Twitter deal?",
 "Financials of the Deal", 
 "Timeline of the take-over",
  "What is Elon's vision for Twitter",
   "Why was the takeover controversial?"]

n = 5

generatePoints(keywords,h2,n)
