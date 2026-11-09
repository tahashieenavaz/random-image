import requests
from random_image.exceptions import UnsplashImageWrongFormatException


class UnsplashImage:
    def __init__(self, url: str):
        self.url = url

    def _check_url(self):
        if self.url.startswith("https://images.unshplash.com"):
            return
        raise UnsplashImageWrongFormatException

    def download(self):
        pass
