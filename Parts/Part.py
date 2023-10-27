from Materials.Feather import *
from Materials.Leather import *
from Materials.Metal import *
from Materials.Stone import *
from Materials.Thread import *
from Materials.Wood import *

class Part:
    def __init__(self, material, weight):
        self._material = material
        self._weight = weight

    def getMaterial(self):
        return self._material

    def getWeight(self):
        return self._weight