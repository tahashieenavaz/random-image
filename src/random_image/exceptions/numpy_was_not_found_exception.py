class NumpyWasNotFoundException(Exception):
    def __init__(self):
        super().__init__(
            "The module `numpy` was not found. Please consider installing it by running `pip install numpy`."
        )
