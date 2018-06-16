from typing import Union

import feedparser

from ..abstract_classes import Grabber


class RSSGrabber(Grabber):
    url: str

    def __init__(self, url: str):
        self.url = url

    def load_data(self) -> Union[dict, list]:
        return feedparser.parse(self.url)
