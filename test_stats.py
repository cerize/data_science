# To run: $ python -m unittest
# -m means 'run module as a script'
import unittest
import numpy as np
import stats as st

class StatsTest(unittest.TestCase):
    list_odd = [20, 3, 5, 90, 8, 8, 4]
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