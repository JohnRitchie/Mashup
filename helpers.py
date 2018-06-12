import feedparser
import urllib.parse


def lookup(geo):
    """Looks up articles for geo."""

    # check cache for geo
    if geo in lookup.cache:
        return lookup.cache[geo]

    # get feed from Google
    feed = feedparser.parse("https://news.google.com/news/rss/local/section/geo/{}".format(urllib.parse.quote(geo, safe="")))

    # if no items in feed, get feed from Onion
    if not feed["items"]:
        feed = feedparser.parse("http://www.theonion.com/feeds/rss")

    # cache results
    lookup.cache[geo] = [{"link": item["link"], "title": item["title"]} for item in feed["items"]]

    # return results
    return lookup.cache[geo]

# initialize cache
lookup.cache = {}

# make dict via json
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d