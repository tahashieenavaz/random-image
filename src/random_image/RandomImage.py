from typing import Optional


class RandomImage:
    def __init__(self, category: Optional[str] = None):
        self._set_category(passed_category=category)

    def _set_category(self, passed_category: Optional[str]) -> None:
        if not passed_category:
            self.category = self._get_random_category()
        else:
            self.category = passed_category
