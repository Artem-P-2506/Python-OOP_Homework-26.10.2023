from Parts.Part import *

class FaceplateOfAspis(Part):
    def __init__(self):
        super().__init__([Wood(), Leather()], 2500)