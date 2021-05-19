
#from typing import Callable, Any, Iterable, List
from spectra.SpectraPreProccessingStep import PreProccessingStep
from spectra.PreproccessStepList import StepsList

class Pipeline:
    '''
    A chain of any number of preprocessing steps that are called sequentially. 
    The output of one step in the pipeline is the input of the next one.
    Call proccess() on object to run the pipeline
    '''
    def __init__(self, steps : list):
        

        if not all(isinstance(x, PreProccessingStep) for x in steps):
            raise TypeError(f'steps list must contains only type of {PreProccessingStep}')

        self.fitted = False
        self.steps = steps
        print(self.steps)

    def add(self, step):
        '''
        add step to steps pipeline
        '''
        if not isinstance(step, PreProccessingStep):
            raise TypeError(f'step must be only type of {PreProccessingStep}')
        self.steps.append(step)


    def proccess(self, spectra):

        while self.steps:
            step = self.steps.pop()


    



    

    
    
