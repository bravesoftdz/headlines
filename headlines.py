import feedparser
from flask import Flask
from flask import render_template


app = Flask(__name__)

RSS_FEEDS = {'arts': 'http://feeds.reuters.com/news/artsculture',
             'business': 'http://feeds.reuters.com/reuters/businessNews'}


@app.route("/")
@app.route("/<publication>")
def get_news(publication='arts'):
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html", articles=feed['entries'])


if __name__ == "__main__":
    app.run(debug=True)
