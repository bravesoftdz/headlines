import feedparser
from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

RSS_FEEDS = {'arts': 'http://feeds.reuters.com/news/artsculture',
             'business': 'http://feeds.reuters.com/reuters/businessNews',
             'word': 'http://feeds.reuters.com/Reuters/worldNews',
             'bbc': 'http://feeds.bbci.co.uk/news/rss.xml'}


@app.route("/")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication = 'arts'

    else:
        publication = query.lower()

    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html", articles=feed['entries'])

if __name__ == "__main__":
    app.run(debug=True)
