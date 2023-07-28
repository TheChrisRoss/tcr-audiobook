import os


def test_and_create_path(path):
    if os.path.isdir(path) == True:
        return True
    os.makedirs(path)


def distinctInOrder(seq: list):  # Order preserving
    """ Modified version of Dave Kirby solution """
    seen = set()
    return [x for x in seq if x not in seen and not seen.add(x)]
