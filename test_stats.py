# To run: $ python -m unittest
# -m means 'run module as a script'
import unittest
import numpy as np
import stats as st
import scipy.stats



class StatsTest(unittest.TestCase):
    list_odd = [20, 3, 5, 90, 8, 8, 3]
    list_even = [20, 3, 5, 90, 1, 1]

    def test_mean(self):
        my_value = st.mean(self.list_odd)
        numpy_value = np.mean(self.list_odd)

        self.assertEqual(my_value, numpy_value)
    
    def test_median_odd_elements(self):
        my_value = st.median(self.list_odd)
        numpy_value = np.median(self.list_odd)

        self.assertEqual(my_value, numpy_value)
    
    def test_median_even_elements(self):
        my_value = st.median(self.list_even)
        numpy_value = np.median(self.list_even)
        
        self.assertEqual(my_value, numpy_value)
    
    def test_mode_unique(self):
        l = [2, 3, 4, 5, 4, 6]
        my_value = st.mode(l)

        self.assertEqual(my_value[0], [4])
    
    def test_mode_multiple(self):
        l = [2, 3, 4, 5, 4, 6, 5]
        my_value = st.mode(l)

        self.assertEqual(my_value[0], [4, 5])

    def test_mode_none(self):
        l = [1, 2, 3, 4, 5]
        my_value = st.mode(l)

        self.assertEqual(my_value[0], [])

    def test_variance(self):
        """Assume degree of freedom = 0"""
        l = [1,2,3,4,5,5,4,3,3,1,2]
        my_value = st.variance(l)
        numpy_value = np.var(l)

        self.assertEquals(my_value, numpy_value)
    
    def test_standard_deviation(self):
        """Assume degree of freedom = 0"""
        l = [1,2,3,4,5,5,4,3,3,1,2]
        my_value = st.standard_deviation(l)
        numpy_value = np.std(l)

        self.assertEquals(my_value, numpy_value)