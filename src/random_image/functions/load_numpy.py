from random_image.exceptions import NumpyWasNotFoundException


def load_numpy():
    try:
        import numpy

        return numpy
    except ModuleNotFoundError:
        raise NumpyWasNotFoundException
