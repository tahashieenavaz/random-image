from random_image.exceptions import TorchWasNotFoundException


def load_torch():
    try:
        import torch

        return torch
    except ModuleNotFoundError:
        raise TorchWasNotFoundException
