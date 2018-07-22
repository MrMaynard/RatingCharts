from Episode import Episode
from RatingSite import RatingSite
import WebUtils


class Imdb(RatingSite):

    season_prefix = "http://www.imdb.com"
    season_postfix = "episodes?season="

    episode_prefix = "https://www.imdb.com"
    episode_postfix = ""

    search_prefix = "http://www.imdb.com/find?ref_=nv_sr_fn&q="
    search_postfix = "&s=all"

    ratingTag = "star__rating\">"
    titleTag = "title=\""

    def resolveTitle(self, title):
        searchUrl = Imdb.search_prefix + title.strip().replace(" ", "%20") + Imdb.search_postfix
        content = WebUtils.getContent(searchUrl)
        resultsStart = content[content.find("result_text"):]
        idStart = resultsStart[resultsStart.find("/title/"):]
        id = idStart[:idStart.find("?ref")]
        trueTitle = idStart[idStart.find(">") + 1:idStart.find("<")]
        return (id, trueTitle)

    def getEpisodes(self, id):
        episodesUrl = Imdb.season_prefix + id + Imdb.season_postfix
        episodes = []
        season = 1
        foundSomething = True
        while foundSomething:
            i = 0
            content = WebUtils.getContent(episodesUrl + str(season))
            foundSomething = False
            workingContent = content[content.find("numberofEpisodes"):]
            while "episodeNumber" in workingContent:
                workingContent = workingContent[workingContent.find("a href=\"/title/") + 8:]
                episode = workingContent[:workingContent.find("?ref")]
                workingContent = workingContent[workingContent.find("?ref"):]
                if episode not in map(lambda e: e.id, episodes):
                    # get title:
                    workingContent = workingContent[workingContent.find(Imdb.titleTag) + len(Imdb.titleTag):]
                    title = workingContent[:workingContent.find("\"")]

                    #get rating:
                    workingContent = workingContent[workingContent.find(Imdb.ratingTag) + len(Imdb.ratingTag):]
                    rating = float(workingContent[:workingContent.find("<")])

                    #append to list:
                    episodes.append(Episode(episode, title, season, i, rating))
                    foundSomething = True
                    i += 1
            season += 1
        return episodes
