from typing import Optional
import yaml
import random
from importlib.resources import files
from functools import cache


class RandomImage:
    def __init__(self, category: Optional[str] = None):
        self._set_category(passed_category=category)
        self._get_random_image()

    def _set_category(self, passed_category: Optional[str]) -> None:
        # TODO: check if the category exists
        if not passed_category:
            self.category = self._get_random_category()
        else:
            self.category = passed_category

    @cache
    def _load_repository_file(self, category: str) -> None:
        with files("random_image").joinpath(f"repository/{category}.yaml").open() as stream:
            image_urls = yaml.safe_load(stream=stream)
            return image_urls
            

    @cache
    def _get_categories(self) -> list[str]:
        repository_directory = files("random_image").joinpath(f"repository")
        yaml_files_generator = repository_directory.glob("*.yaml")
        return list(map(lambda x: x.name, yaml_files_generator))

    def _get_random_category(self):
        return random.choice(self._get_categories())

    def _get_random_image(self):
        # load repositry file 
        # get the random image
        # download it and store it 
        # return the PIL Image
