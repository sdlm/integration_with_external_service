import json

from ..classes import FileGrabber


class JSONGrabber(FileGrabber):

    def load_data(self) -> dict:
        with open(self.path) as json_file:
            return json.load(json_file)
