import math
import sys

#################################################################
def plot(x,y):
	lx = len(x)
	ly = len(y)

	###########################################################
	#Raise input error flags
	if(lx != ly):
		raise InputsizeError,"InputSize of x and y incompatible"
	for i in range(0,lx):	
		if((type(x[i]) == int) or (type(x[i]) == float)):
			pass
		else:
			raise TypeError,"TypeError: x"
	for i in range(0,ly):	
		if((type(y[i]) == int) or (type(y[i]) == float)):
			pass
		else:
			raise TypeError,"TypeError: x"


	###########################################################
	#first find min and max in array so that you can scale in the 
	#beginning itself and get sorted int array

	max_x = max(x)
	min_x = min(x)
	max_y = max(y)
	min_y = min(y) 

	############################################################
	#now scale to get int list

	#scaling factors
	scaled_x,scaled_y = scaling_list(max_y,min_y,max_x,min_x,x,y,ly)


	###########################################################

	#corresponding sorted pairs
	sorted_x,sorted_y = corr_sorted(scaled_x,scaled_y,ly)

	#at end of loop we will get sorted y . x will be sorted but for 
	#same corresponding y may or may not be sorted
	###########################################################

	#totally sorted
	sorted_x,sorted_y =total_sorted(sorted_x,sorted_y,ly)

	###########################################################

	#plotting points
	draw_plot(sorted_x,sorted_y,ly)

##############################################################

def scaling_list(max_y,min_y,max_x,min_x,x,y,ly):
	ay = 30/(max_y - min_y)
	by = (-30*min_y)/(max_y-min_y)
	ax = 80/(max_x - min_x)
	bx = (-80*min_x)/(max_x-min_x)

	scaled_x = []
	scaled_y = []

	for i in range(0,ly): #to get scaled lists
		x_int = int(ax*x[i]+bx)
		y_int = int(ay*y[i]+by)
		scaled_x.append(x_int)
		scaled_y.append(y_int)
	
	return scaled_x,scaled_y
##############################################################

def corr_sorted(scaled_x,scaled_y,ly):

	sorted_y = []
	sorted_x = []

	for j in range(0,ly):	#to sort all corresponding in y list
		for i in range(0,ly):
			if(scaled_y[i]!= -999.0):
				min_y = scaled_y[i]
				min_y_index = i
				break

		for i in range(0,ly):
			if((scaled_y[i]!= -999.0)  and (min_y > scaled_y[i])):
				min_y = scaled_y[i]
				min_y_index = i
		sorted_y.append(min_y)
		sorted_x.append(scaled_x[min_y_index])
		scaled_y[min_y_index] = -999.0 #dummy value
	return sorted_x,sorted_y
###############################################################

def total_sorted(sorted_x,sorted_y,ly):
	index_stop = 0
	for i in range(0,ly):
		if(index_stop == i):
			y_samp = sorted_y[i]
			list1 = [sorted_x[i]]
			index_start = i
			for j in range (i+1,ly):
				if(y_samp == sorted_y[j]):
					list1.append(sorted_x[j])
					if(j == ly-1):
						index_stop = ly
				else:
					index_stop = j
					break
			if(index_start == ly -1):
				index_stop = ly
			list1.sort() 
			sorted_x[index_start:index_stop] = list1
		else:
			pass
	return sorted_x,sorted_y
###############################################################

def draw_plot(sorted_x,sorted_y,ly):
	y_rel = 0
	x_rel = 0
	for i in range(0,ly): # do printing row wise
		sys.stdout.write("\n"*(sorted_y[i]-y_rel))
		if(sorted_y[i] == y_rel):
			sys.stdout.write(" "*(sorted_x[i]-x_rel))
		else:
			sys.stdout.write(" "*sorted_x[i])
		sys.stdout.write("*")
		y_rel = sorted_y[i]
		x_rel = sorted_x[i]
#################################################################

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

	plot(x,y)

#############################################################
