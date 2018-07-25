from flask import Flask, render_template, request

import RatingCharts
from Imdb import Imdb

app = Flask(__name__)

script_js = ''

@app.route('/')
@app.route('/home')
@app.route('/search')
def home():
    return render_template('index.html')


@app.route('/chart')
def chart():
    if request.args.get('search') is None:
        return "Invalid url"
    else:
        search = str(request.args.get('search')).strip()
    
    scale = False
    if request.args.get('scale') is not None:
        if str(request.args.get('scale')) == 'True':
            scale = bool(request.args.get('scale'))

    try:
        true_title, episodes = RatingCharts.getEpisodes(Imdb(), search)
        try:
            chart_div = RatingCharts.buildChart(true_title, episodes, scale)
        except:
            return "Unable to build chart for \"" + search + "\""
    except:
        return "Unable to scrape episode data for \"" + search + "\""
    print(render_template('chart.html', chart_div = chart_div))
    # return '<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>\n' + chart_div
    return render_template('chart.html', chart_div = chart_div)
    

    
