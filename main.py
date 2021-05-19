from spectra.SpectraPreProccessingStep import Log, SelectWavelengths 
from spectra.PreproccessStepList import StepsList
from spectra.PreProccessPipeline import Pipeline
import numpy as np

if __name__ == '__main__':
    print('moshe cohen')

    p = Pipeline([Log(), SelectWavelengths(120, 150)])
    spectra = np.array([[7, 2, 5, 4, 5], [6, 7, 8, 9, 10]])

    p.proccess(spectra)


    #spectra = np.array([[7, 2, 5, 4, 5],[6, 7, 8, 9, 10]], dtype='float')
    #print(spectra)
    #print(spectra.dtype)

    