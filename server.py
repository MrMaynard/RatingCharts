from flask import Flask, render_template, request

import RatingCharts
from Imdb import Imdb

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/search')
@app.route('/chart')
def home():
    if request.args.get('search') is None:
        search = None
    else:
        search = str(request.args.get('search')).strip()
    
    scale = False
    if request.args.get('scale') is not None:
        if str(request.args.get('scale')) == 'True':
            scale = bool(request.args.get('scale'))

    if search is not None:
        try:
            true_title, episodes = RatingCharts.getEpisodes(Imdb(), search)
            try:
                chart_div = RatingCharts.buildChart(true_title, episodes, scale)
            except:
                return "Unable to build chart for \"" + search + "\""
        except:
            return "Unable to scrape episode data for \"" + search + "\""
        return render_template('index.html', chart_div = chart_div, title = true_title)
    else:
        return render_template('index.html', chart_div = "", title = "Visualize TV Ratings")
    

    
