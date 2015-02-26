from text_plot import *
def plot_test():
   	"""Test for plotting graph text_plot"""
	x1 = [-7,8.4,1,5,3,2.3,6,-3,12,9,-6,4]
	y1 = [3.5,3.6,3.5,5.1,2.8,7.9,7,8,8.8,8,9,1] 
   	x2 = [2,5,4,8,9]
    	y2 = [1,6,8,2,3]
  	assert len(x1) == len(y1)
	assert len(x2) == len(y2)
	lx1 = len(x1)
	lx2 = len(x2)
	for i in range(0,lx1):
		assert (type(x1[i]) == int or type(x1[i]) == float)
		assert (type(y1[i]) == int or type(y1[i]) == float)
	for i in range(0,lx2):
		assert (type(x2[i]) == int or type(x2[i]) == float)
		assert (type(y2[i]) == int or type(y2[i]) == float)

    
if __name__=="__main__":
    plot_test()
