
#from typing import Callable, Any, Iterable, List
from spectra import SpectraPreProccessingStep

class PreProccessPipeline:
    def __init__(self, **steps):
        self.steps = steps
        print(self.steps)

    def add(self, step):
        self.steps.append(step)

    
    def fit(self):
        pass
