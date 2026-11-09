class TorchVisionWasNotFoundException(Exception):
    def __init__(self):
        super().__init__(
            "The module `torchvision` was not found. Please consider installing it by running `pip install torch`."
        )
