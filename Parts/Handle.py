from Parts.Part import *

class Handle(Part):
    def __init__(self):
        super().__init__([Wood(), Leather()], 400)