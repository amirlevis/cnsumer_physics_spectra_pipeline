from spectra.SpectraPreProccessingStep import PreProccessingStep, TransformPreProccessingStep, FitPreProccessingStep
import numpy as np

class Pipeline:
    '''
    A chain of any number of preprocessing steps that are called sequentially. 
    The output of one step in the pipeline is the input of the next one.
    Call proccess(spectra) on object to run the pipeline
    '''
    def __init__(self, steps : list):
        

        if not all(isinstance(x, PreProccessingStep) for x in steps):
            raise TypeError(f'steps list must contains only type of {PreProccessingStep}')

        self.fitted = False
        self.steps = steps

    def add(self, step):
        '''
        add step to steps pipeline
        '''

        if self.fitted:
            raise PipelineFittedError('Pipeline already ran a fit step cant add new preproccess steps')


        if not isinstance(step, PreProccessingStep):
            raise TypeError(f'step must be only type of {PreProccessingStep}')
        self.steps.append(step)


    def proccess(self, spectra):
       
        if len(self.steps) == 0:
            print('No more steps to proccess')
            return 
       
        step = self.steps.pop()

        if isinstance(step, FitPreProccessingStep):
            step.fit(spectra)
            self.fitted = True

        spectra = step.transform(spectra)
        self.proccess(spectra)
       
        return spectra

   


class PipelineFittedError(Exception):
    ''' Excpetion is raised when pipeline already ran a fit step'''
 