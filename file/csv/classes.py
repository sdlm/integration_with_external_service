import csv

from file.classes import FileGrabber


class CSVGrabber(FileGrabber):

    def load_data(self) -> list:
        with open(self.path) as csv_file:
            return list(csv.reader(csv_file))
