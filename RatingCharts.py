from Imdb import Imdb
import ColorUtils

from plotly import __version__
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

def main():
    imdb = Imdb()

    title = input("title>").strip()
    print(title)
    id = imdb.title2Id(title)
    episodes = imdb.id2Episodes(id)

    episodes = sorted(episodes)
    print(episodes)

    xValues = []
    yValues = []
    for i, episode in enumerate(episodes):
        xValues.append(i)
        yValues.append(float(episode.rating.strip()))


    trace = go.Scatter(x=xValues, y=yValues, mode = 'markers')
    data = [trace]
    layout = go.Layout(
        title=title,
        width=1250, height=700,
        xaxis=dict(
            title='Episode',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color=ColorUtils.getRandomColor()
            )
        ),
        yaxis=dict(
            title='Score',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )
    fig = go.Figure(data=data, layout=layout)

    plot(fig, filename='output.html')


if __name__ == "__main__":
    main()
