import requests
from bs4 import BeautifulSoup
import json
from pprint3x import pprint
from datetime import datetime



class Midjourney:
	def __init__(self):
		self.url = "https://www.midjourney.com/showcase/recent/"

	def _get_timestamp_from_string(self, date: str) -> int:
		date_string = date
		date_format = "%Y-%m-%d %H:%M:%S.%f"
		timestamp = datetime.strptime(date_string, date_format).timestamp()
		return int(timestamp)

	def getContent(self):
		imageUrls = []
		resp = requests.get(self.url)
		soup = BeautifulSoup(resp.text, 'html.parser')
		body = soup.find("script", {"id":"__NEXT_DATA__"})
		bodyText = body.text
		bodyJson = json.loads(bodyText)
		props = bodyJson["props"]
		pageProps = props["pageProps"]
		jobs = pageProps["jobs"]
		pubTime = job["enqueue_time"]
		posts = []
		for job in jobs:
			event = job["event"]
			imageUrl = event["seedImageURL"]
			textPrompt = event["textPrompt"]
			posts.append({'title': None,
				'link': imageUrl,
				'description': textPrompt[0],
				'imageUrl': imageUrl,
				'source': 'Midjourney',
				'tags': [],
				'publishingTime': self._get_timestamp_from_string(pubTime)})
		return posts
