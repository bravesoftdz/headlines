import feedparser
from flask import Flask


app = Flask(__name__)

RSS_FEEDS = {'arts': 'http://feeds.reuters.com/news/artsculture',
             'business': 'http://feeds.reuters.com/reuters/businessNews'}


@app.route("/")
@app.route("/arts")
def arts():
    return get_news('arts')


@app.route("/business")
def business():
    return get_news('business')


def get_news(publication):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]

    return """ <html>
    <body>
        <h1>Headlines </h1>
        <b>{0}</b> </br>
        <i>{1}</i> </br>
        <p>{2}</p> </br>
    </body>
    </html>
    """.format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))

if __name__ == "__main__":
    app.run(debug=True)
