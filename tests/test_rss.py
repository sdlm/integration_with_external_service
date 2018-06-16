import json
import unittest
from unittest.mock import patch, MagicMock

from rss.classes import RSSGrabber

REDDIT_RSS_ENDPOINT = 'https://www.reddit.com/r/news/.rss'
HABRAHABR_RSS_ENDPOINT = 'https://habrahabr.ru/rss/hubs/all/'


class RSSGrabberTest(unittest.TestCase):

    def test_load_data(self):
        grabber = RSSGrabber(url=REDDIT_RSS_ENDPOINT)
        data = grabber.load_data()
        self.assertTrue(isinstance(data, dict))

    def test_load_data_without_request_external_service(self):
        with open('reddit.json') as json_file:
            reddit_data = json.load(json_file)

        with open('habrahabr.json') as json_file:
            habrahabr_data = json.load(json_file)

        patched_request_igel = patch(
            target='rss.classes.RSSGrabber.load_data',
            new=MagicMock(
                side_effect=[
                    reddit_data,
                    habrahabr_data
                ]
            )
        )
        with patched_request_igel:
            for url in [REDDIT_RSS_ENDPOINT, HABRAHABR_RSS_ENDPOINT]:
                grabber = RSSGrabber(url=url)
                data = grabber.load_data()
                self.assertTrue(isinstance(data, dict))
