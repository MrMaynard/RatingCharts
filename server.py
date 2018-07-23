from flask import Flask
from flask import request

import RatingCharts
from Imdb import Imdb

app = Flask(__name__)

script_js = '<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>'

@app.route('/chart')
def chart():
    if request.args.get('search') is None:
        return "Invalid url"
    else:
        search = str(request.args.get('search')).strip()

    scale = False
    if request.args.get('scale') is not None:
        scale = bool(str(request.args.get('scale')).strip())

    try:
        true_title, episodes = RatingCharts.getEpisodes(Imdb(), search)
        try:
            chart_div = RatingCharts.buildChart(true_title, episodes, scale)
        except:
            return "Unable to build chart for \"" + search + "\""
    except:
        return "Unable to scrape episode data for \"" + search + "\""
    return script_js + "\n" + chart_div
    

    
