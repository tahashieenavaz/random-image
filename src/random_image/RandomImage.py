import yaml
import random
import datetime
import requests
from PIL import Image
from importlib.resources import files
from functools import cache
from typing import Optional
from random_image.exceptions import NumpyWasNotFoundException


class RandomImage:
    def __init__(self, category: Optional[str] = None):
        self.filename = self._generate_downloaded_file_name()
        self._set_category(passed_category=category)
        self._get_random_image()

    def _set_category(self, passed_category: Optional[str]) -> None:
        # TODO: check if the category exists
        if not passed_category:
            self.category = self._get_random_category()
        else:
            self.category = passed_category

    @cache
    def _load_repository_file(self, category: str) -> list[str]:
        with (
            files("random_image")
            .joinpath(f"repository/{category}.yaml")
            .open() as stream
        ):
            image_urls = yaml.safe_load(stream=stream)
            return image_urls

    @cache
    def _get_categories(self) -> list[str]:
        repository_directory = files("random_image").joinpath(f"repository")
        yaml_files_generator = repository_directory.glob("*.yaml")
        return list(map(lambda x: x.name.replace(".yaml", ""), yaml_files_generator))

    def _get_random_category(self):
        return random.choice(self._get_categories())

    def _generate_downloaded_file_name(self):
        return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.jpg")

    def _save_file(self, name: str, url: str):
        response = requests.get(url)
        with open(name, "wb") as handler:
            handler.write(response.content)

    def _get_random_image(self):
        url_repository = self._load_repository_file(self.category)
        random_image_url = random.choice(url_repository)
        self._save_file(self.filename, random_image_url)

    def pil(self):
        return Image.open(self.filename)

    def numpy(self):
        try:
            import numpy
        except ModuleNotFoundError:
            raise NumpyWasNotFoundException

        return numpy.asarray(self.pil())
