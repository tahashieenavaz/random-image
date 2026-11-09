import random


def one_of[OneOfCollectionItem](collection: list[OneOfCollectionItem]) -> OneOfCollectionItem:
    return random.choice(collection)
