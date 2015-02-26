import math
import sys

class my_plot():

	def __init__(self,x,y,rows=30,cols=80):

	
		self.lx = len(x)
		self.ly = len(y)
		self.rows = rows
		self.cols = cols
		self.x = x
		self.y = y

		###########################################################
		#Raise input error flags
		if(self.lx != self.ly):
			raise ValueError,"InputSize of x and y incompatible"
		for i in range(0,self.lx):	
			if((type(self.x[i]) == int) or (type(self.x[i]) == float)):
				pass
			else:
				raise TypeError,"TypeError: x"
		for i in range(0,self.ly):	
			if((type(self.y[i]) == int) or (type(self.y[i]) == float)):
				pass
			else:
				raise TypeError,"TypeError: x"


		###########################################################
		#first find min and max in array so that you can scale in the 
		#beginning itself and get sorted int array

		self.max_x = max(self.x)
		self.min_x = min(self.x)
		self.max_y = max(self.y)
		self.min_y = min(self.y) 

		############################################################

	def plot_XY(self):
		#now scale to get int list

		#scaling factors
		self.scaling_list()


		###########################################################

		#corresponding sorted pairs
		self.corr_sorted()

		#at end of loop we will get sorted y . x will be sorted but for 
		#same corresponding y may or may not be sorted
		###########################################################

		#totally sorted
		self.total_sorted()

		###########################################################

		#plotting points
		self.draw_plot()

	##############################################################

	def scaling_list(self):
		#size of canvas defined by number of rows and columns	
		
		ay = self.rows/(self.max_y - self.min_y)
		by = (-self.rows*self.min_y)/(self.max_y- self.min_y)
		ax = self.cols/(self.max_x - self.min_x)
		bx = (-self.cols*self.min_x)/(self.max_x-self.min_x)

		self.scaled_x = []
		self.scaled_y = []

		for i in range(0,self.ly): #to get scaled lists
			x_int = int(ax*self.x[i]+bx)
			y_int = int(ay*self.y[i]+by)
			self.scaled_x.append(x_int)
			self.scaled_y.append(y_int)
	
	##############################################################

	def corr_sorted(self):

		self.sorted_y = []
		self.sorted_x = []

		for j in range(0,self.ly):	#to sort all corresponding in y list
			for i in range(0,self.ly):
				if(self.scaled_y[i]!= -999.0):
					min_y = self.scaled_y[i]
					min_y_index = i
					break

			for i in range(0,self.ly):
				if((self.scaled_y[i]!= -999.0)  and (min_y > self.scaled_y[i])):
					min_y = self.scaled_y[i]
					min_y_index = i
			self.sorted_y.append(min_y)
			self.sorted_x.append(self.scaled_x[min_y_index])
			self.scaled_y[min_y_index] = -999.0 #dummy value

	################################################################

	def total_sorted(self):
		index_stop = 0
		for i in range(0,self.ly):
			if(index_stop == i):
				y_samp = self.sorted_y[i]
				list1 = [self.sorted_x[i]]
				index_start = i
				for j in range(i+1,self.ly):
					if(y_samp == self.sorted_y[j]):
						list1.append(self.sorted_x[j])
						if(j == self.ly-1):
							index_stop = self.ly
					else:
						index_stop = j
						break
				if(index_start == self.ly -1):
					index_stop = self.ly
				list1.sort() 
				self.sorted_x[index_start:index_stop] = list1
			else:
				pass
	
	###############################################################

	def draw_plot(self):
		y_rel = 0
		x_rel = 0
		for i in range(0,self.ly): # do printing row wise
			sys.stdout.write("\n"*(self.sorted_y[i]-y_rel))
			if(self.sorted_y[i] == y_rel):
				sys.stdout.write(" "*(self.sorted_x[i]-x_rel))
			else:
				sys.stdout.write(" "*self.sorted_x[i])
			sys.stdout.write("*")
			y_rel = self.sorted_y[i]
			x_rel = self.sorted_x[i]
	#################################################################

##################################################################################

def plot(x,y,rows=30,cols=80):
	a = my_plot(x,y,rows,cols)
	a.plot_XY()
##################################################################################

if __name__ == "__main__":
	#we will make sine wave plot using x,y list
	#x is list of l points+1 point(for 2*pi)
	x = []
	y = []
	#no. of points in plot
	l = 50+1



	for i in range(0,l):
		x_sine_input = i*2*(math.pi)/(l-1)
		x.append(x_sine_input)
		y_sine_output = math.sin(x_sine_input)
		y.append(y_sine_output)

	a = my_plot(x,y,30,80)
	a.plot_XY()


#############################################################
