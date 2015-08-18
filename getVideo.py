#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyBl7nxzkjSusSb-bqnQXHHkIEZ4LJNOyTg"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

keyword=[u'Max Steel', u'13 Ghosts', u'6 Years', u'Ejecta']


def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=options.q,
        part="id,snippet",
        maxResults=options.max_results
        ).execute()

    videos = []
    channels = []
    playlists = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_result["snippet"]["title"],
            search_result["id"]["videoId"]))
        elif search_result["id"]["kind"] == "youtube#channel":
            channels.append("%s (%s)" % (search_result["snippet"]["title"],
            search_result["id"]["channelId"]))
        elif search_result["id"]["kind"] == "youtube#playlist":
            playlists.append("%s (%s)" % (search_result["snippet"]["title"],
            search_result["id"]["playlistId"]))
    
    with open(listfile,'a') as f:
        f.write()

    print "Videos:\n", "\n".join(videos), "\n"
    print "Channels:\n", "\n".join(channels), "\n"
    print "Playlists:\n", "\n".join(playlists), "\n"


def search_byterm(keyword):
    for word in keyword:
        key='\"'+str(word)+'\"'
        search_term=key+'"movie review" "vlog"'
        argparser.add_argument("--q", help="Search term", default=search_term)
        argparser.add_argument("--max-results", help="Max results", default=50)
        argparser.add_argument("--order", help="Order", default='Date')
        args = argparser.parse_args()

        try:
        youtube_search(args)
        except HttpError, e:
        print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)