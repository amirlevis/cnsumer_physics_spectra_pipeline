from abc import ABC, abstractmethod
import numpy as np

class PreProccessingStep:
    pass


class FitPreProccessingStep(PreProccessingStep):

    @abstractmethod
    def fit(self):
        pass


class TransformPreProccessingStep(PreProccessingStep):

    @abstractmethod
    def transform(self):
        pass



class Log(TransformPreProccessingStep):
    '''
    run log operation on all wavelengths. Example:
    Log.transform([[1, 2, 3], [4, 5, 6]]) = 
    [[ 0, 0.69314718, 1.09861229], [1.38629436,1.60943791,1.79175947]]
    '''


    def transform(self, spectra):
        return np.log(spectra)
        


class Diff(TransformPreProccessingStep):
    '''
    simple difference between consecutive wavelengths. Example:
    Diff.transform([[1, 2, 3], [4, 6, 9]]) = [[1, 1], [2, 3]]
    '''

    def transform(self, spectra):
        return np.diff(spectra) 



class SelectWavelengths(TransformPreProccessingStep):
    '''
    reducing the number of WLs. Example:
    SelectWavelengths(from=1, to=3).transform([7, 2, 5, 4, 5], [6, 7, 8, 9, 10])
    = [[2, 5, 4], [7, 8, 9]].	
    (Note that the indexes of the parameters from and to are zero based)
    '''

    def __init__(self, frm, to):
        self.frm = frm
        self.to = to+1


    def transform(self, spectra : np.array):
        if self.to > spectra.shape[1]:
            raise IndexError('spectra to value is out of bound')
        return spectra[:, self.frm:self.to]


class SubtractAvg(TransformPreProccessingStep, FitPreProccessingStep):
    '''
    subtract from each wavelength the mean wavelength value. 
    Example:
    s = SubtractAvg()
    s.fit([[1, 2, 0], [4, 5, 6]]) - learns the average values [2.5, 3.5, 3]
    s.transform([[5, 5, 5]]) = [2.5, 1.5, 2]
	s.transform([7.5, 7.0, 9]) = [5.0, 3.5, 6.0]
    '''

    def __init__(self) -> None:
        self.avg = None

    def transform(self, spectra):
        return np.subtract(spectra, self.avg)

    def fit(self, spectra : np.array):
        self.avg = spectra.mean(axis = 0)
