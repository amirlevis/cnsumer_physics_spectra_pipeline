from unittest import TestCase
from spectra.SpectraPreProccessingStep import Log, Diff, SelectWavelengths, SubtractAvg
import numpy as np

class TestPreProccessStep(TestCase):


    def test_preProccess_log(self):
       
        spectra = np.array([[1, 2, 3],[4, 5, 6]], dtype='float64')
        step = Log()
        log = step.transform(spectra)
        
        result = np.array([[0, 0.69314718, 1.09861229], [1.38629436,1.60943791,1.79175947]], dtype='float64')
        is_equal = np.allclose(log,result)
        self.assertEqual(is_equal , True)
    
    def test_preProccess_diff(self):
        spectra = ([[1, 2, 3], [4, 6, 9]])

        step = Diff()
        diff = step.transform(spectra)
        expected_result = [[1, 1], [2, 3]]
        is_equal = np.array_equal(diff,expected_result)

        self.assertEqual(is_equal, True)

    def test_preProccess_select_wave_length(self):
       spectra = np.array([[7, 2, 5, 4, 5], [6, 7, 8, 9, 10]])
       step = SelectWavelengths(frm=1, to=3)
       new_spectra = step.transform(spectra)

       expected_result = [[2, 5, 4], [7, 8, 9]]

       is_equal = np.array_equal(new_spectra,expected_result)
       self.assertEqual(is_equal, True)


    def test_preProccess_subtractAvg(self):
        spectra = np.array([[1, 2, 0], [4, 5, 6]])
        step = SubtractAvg()
        step.fit(spectra)

        sub = step.transform (np.array([[5, 5, 5]]))
        expected_result = np.array([2.5, 1.5, 2])
        is_equal = np.allclose(sub,expected_result)
        self.assertEqual(is_equal, True)


        expected_result = [5.0, 3.5, 6.0]
        sub = step.transform (np.array([[7.5, 7.0, 9]]))
        is_equal = np.allclose(sub,expected_result)
        self.assertEqual(is_equal, True)
         


