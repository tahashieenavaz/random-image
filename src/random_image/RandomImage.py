from typing import Optional
import yaml
from importlib.resources import files


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

    def _load_repository_file(self):
        with files("random_image").joinpath(f"repository/{self.category}.yaml").open() as stream:
            image_urls = yaml.safe_load(stream=stream)
            self.image_urls = image_urls

    def _get_random_category(self):
        return 

    def _get_random_image(self):
        # load repositry file 
        # get the random image
        # download it and store it 
        # return the PIL Image
