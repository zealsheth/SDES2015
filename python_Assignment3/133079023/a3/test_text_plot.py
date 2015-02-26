from text_plot import *
import unittest

"""Test for plotting graph text_plot"""
x1 = [-7,8.4,1,5,3,2.3,6,-3,12,9,-6,4]
y1 = [3.5,3.6,3.5,5.1,2.8,7.9,7,8,8.8,8,9,1] 
x2 = [2,5,4,8,9]
y2 = [1,6,8,2,3]
x3 = [1,4,6,"s"]
y3 = [3,4.7,5,7]
x4 = [1,0,3]
y4 = [1,7]


class test_my_plot(unittest.TestCase): 
    """Tests the various functions from the module text_plot"""
    def test_TypeError(self):        
        #self.assertRaises(TypeError,my_plot,x1,y1)
        #self.assertRaises(TypeError,my_plot,x2,y2)
        self.assertRaises(TypeError,my_plot,x3,y3)
    def test_ValueError(self):        
        self.assertRaises(ValueError,my_plot,x4,y4)
       
if __name__=="__main__":
    unittest.main()
