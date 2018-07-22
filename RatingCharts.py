from Imdb import Imdb
import PlotUtils

from plotly import __version__
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

from numpy import arange,array,ones
from scipy import stats

def main():
    imdb = Imdb()
    seedColor = (60, 130, 220)

    # get title:
    title = input("title>").strip()
    print(title)

    # todo get options:
    scale = True

    # get all episodes for this title:
    id = imdb.title2Id(title)
    episodes = imdb.id2Episodes(id)
    episodes = sorted(episodes)

    # separate into seasons:
    i = 1
    episodesBySeason = []
    for episode in episodes:
        if episode.season not in map(lambda x: x[0].season, episodesBySeason):
            episodesBySeason.append([])
        episode.rawNumber = i
        episodesBySeason[episode.season - 1].append(episode)
        i += 1

    # create color list:
    colors = []
    for season in episodesBySeason:
        colors.append(PlotUtils.getRandomColor(seedColor[0], seedColor[1], seedColor[2]))

    # create a trace for each season:
    trace = []
    for season in episodesBySeason:
        print(season)
        seedColor = PlotUtils.getRandomColor(seedColor[0], seedColor[1], seedColor[2])
        trace.append(go.Scatter(
            x=list(map(lambda s: s.rawNumber, season)),
            y=list(map(lambda s: s.rating, season)),
            mode='markers',
            marker=dict(
                color=PlotUtils.color2PlotlyString(colors[season[0].season - 1], .9)
            )))

    # create best fit lines:
    for season in episodesBySeason:
        xi = list(map(lambda s: s.rawNumber, season))
        y = list(map(lambda s: s.rating, season))
        print(xi)
        print(y)
        slope, intercept, r_value, p_value, std_err = stats.linregress(xi, y)
        line = list(map(lambda x: slope * x + intercept, xi))
        trace.append(go.Scatter(
            x=xi,
            y=line,
            mode='lines',
            marker=dict(
                color=PlotUtils.color2PlotlyString(colors[season[0].season - 1], .8)
            )))

    # customize graph:
    if scale:
        minY = min(map(lambda x: x.rating, episodes))
        maxY = max(map(lambda x: x.rating, episodes))
    else:
        minY = 1
        maxY = 10
    # TODO this better

    # create the plot layout:
    layout = go.Layout(
        title=title,
        xaxis=dict(
            title='Episode',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
        yaxis=dict(
            title='Score',
            range = [minY, maxY],
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )
    fig = go.Figure(data=trace, layout=layout)
    # iplot(fig)
    plot(fig, filename='output.html')


if __name__ == "__main__":
    main()
