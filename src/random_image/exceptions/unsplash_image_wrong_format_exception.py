class UnsplashImageWrongFormatException(Exception):
    def __init__(self):
        super().__init__(
            "The UnsplashImage urls must start with `images.unsplash.com`."
        )
