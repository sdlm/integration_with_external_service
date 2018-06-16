from abstract_classes import Grabber


# noinspection PyAbstractClass
class FileGrabber(Grabber):
    path: str

    def __init__(self, path: str):
        self.path = path
