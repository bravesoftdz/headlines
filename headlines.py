import feedparser
from flask import Flask
from flask import render_template
from flask import request
import json
import requests


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
    weather = get_weather("Sydney")
    return render_template("home.html", articles=feed['entries'], weather=weather)

def get_weather(query):
    api_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=2349e3c5627da54e4bb2685a1bc24806&units=metric'
    # query = urllib.quote(query)
    url = api_url.format(query)
    print(url)
    data = requests.get(url)
    parsed = json.loads(data.text)
    weather = None

    if parsed.get("weather"):
        weather = {"description": parsed["weather"][0]["description"],
                   "temperature": parsed["main"]["temp"],
                   "city": parsed["name"]}

    return weather


if __name__ == "__main__":
    app.run(debug=True)
