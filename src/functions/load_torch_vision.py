from random_image.exceptions import TorchVisionWasNotFoundException


def load_torch_vision():
    try:
        import torchvision

        return torchvision
    except ModuleNotFoundError:
        raise TorchVisionWasNotFoundException
