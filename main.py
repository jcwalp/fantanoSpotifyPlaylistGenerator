import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse
import urllib.parse as p
import re
import os
import pickle
import simplejson




#extract playlist id from url
url = 'hhttps://www.youtube.com/playlist?list=PLP4CSgl7K7oo93I49tQa0TLB8qY3u7xuO'
query = parse_qs(urlparse(url).query, keep_blank_values=True)
playlist_id = query["list"][0]
print(playlist_id)
print(f'get all playlist items links from {playlist_id}')
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = "AIzaSyCO1t859-lhM48zXipPrKWW8V2SPPoBkrA")

request = youtube.playlistItems().list(
    part = "snippet",
    playlistId = playlist_id,
    maxResults = 50
)
response = request.execute()

playlist_items = []
video_titles = []
unparsedData = []
while request is not None:
    response = request.execute()
    playlist_items += response["items"]
    request = youtube.playlistItems().list_next(request, response)

for link in playlist_items:
    linkToString = str(link)
    titleUnparsed = str(linkToString[252:])
    unparsedData += titleUnparsed





i = 0
while i < len(unparsedData):
    print(unparsedData[i])
    i += 1
# for item in unparsedData:
#     print(item)
    # for x in item:
    #     if x == ",":
            # item = item[252:x]



##print(f"total: {len(playlist_items)}")
##print([
  ##  f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}&list={playlist_id}&t=0s'
    ##for t in playlist_items
##])