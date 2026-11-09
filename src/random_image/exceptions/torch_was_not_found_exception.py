class TorchWasNotFoundException(Exception):
    def __init__(self):
        super().__init__(
            "The module `torch` was not found. Please consider installing it by running `pip install torch`."
        )
