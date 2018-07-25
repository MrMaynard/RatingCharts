from Imdb import Imdb
import PlotUtils

import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

from scipy import stats

# todo rest api


def buildChart(title, episodes, scale):
    seedColors = [(60, 130, 220), (110, 180, 80), (180, 100, 210)]
	seedColor = random.choice(seedColors)

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
    colors = [PlotUtils.getRandomColor(seedColor[0], seedColor[1], seedColor[2])]
    for i in range(len(episodesBySeason)):
        colors.append(PlotUtils.getRandomColor(colors[i][0], colors[i][1], colors[i][2]))

    # create a trace for each season:
    trace = []
    for season in episodesBySeason:
        seedColor = PlotUtils.getRandomColor(seedColor[0], seedColor[1], seedColor[2])
        trace.append(go.Scatter(
            x=list(map(lambda s: s.rawNumber, season)),
            y=list(map(lambda s: s.rating, season)),
            text=list(map(lambda s: PlotUtils.buildTitle(s), season)),
            name="Season " + str(season[0].season),
            mode='markers',
            marker=dict(
                color=PlotUtils.color2PlotlyString(colors[season[0].season - 1], .9)
            )))

    # create best fit lines:
    for season in episodesBySeason:
        xi = list(map(lambda s: s.rawNumber, season))
        y = list(map(lambda s: s.rating, season))
        slope, intercept, r_value, p_value, std_err = stats.linregress(xi, y)
        line = list(map(lambda x: slope * x + intercept, xi))
        trace.append(go.Scatter(
            x=xi,
            y=line,
            mode='lines',
            name="S" + str(season[0].season) + " best fit",
            marker=dict(
                color=PlotUtils.color2PlotlyString(colors[season[0].season - 1], .8)
            )))

    # customize graph:
    print(scale)
    if scale == True:
        minY = min(map(lambda x: x.rating, episodes))
        maxY = max(map(lambda x: x.rating, episodes))
    else:
        minY = 1
        maxY = 10

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
            range=[minY, maxY],
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )
    fig = go.Figure(data=trace, layout=layout)
    # iplot(fig)
    # plot(fig, filename='output.html')
    return plot(fig, include_plotlyjs=False, output_type='div')

def getEpisodes(site, title):
    id, trueTitle = site.resolveTitle(title)
    episodes = site.getEpisodes(id)
    return (trueTitle, sorted(episodes))

def main():
    # get title:
    title = input("title>").strip()
    print(title)

    # get episodes:
    try:
        trueTitle, episodes = getEpisodes(Imdb(), title)
        # build chart
        try:
            print(buildChart(trueTitle, episodes, False))
        except:
            print("Unable to build chart for \"" + title + "\"")
    except:
        print("Unable to scrape episode data for \"" + title + "\"")



if __name__ == "__main__":
    main()
