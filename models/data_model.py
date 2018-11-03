import csv

class Rider:


	def __init__(self, name, fname):
		self.name = name
		self.fname = fname
		#self.count = 0

		# Read 
		with open(fname, mode='r') as csv_file:
		    csv_reader = csv.DictReader(csv_file, delimiter=';')
		    self.data = []
		    for row in csv_reader:
		    	if row['RiderID'] in [self.name]: 
			    	self.data.append(row)





	def __repr__(self):
		#return 'Rider(*{!r})'.format(self.name) 
		#return 'Rider(*{!r})'.format(self.name + ', ' + self.fname + ', ' + str(self.count)) 
		return 'Rider(*{!r})'.format(self.name + ', ' + self.fname) 


	def __len__(self): 
		return len(self.data)


	#def __add__(self, other):
	#	return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))


	#def __call__(self):
	#	pass



#p1 = Rider('1', 'dtra.csv')
#p2 = Rider('2', 'dtra.csv')
#p3 = Rider('1', 'data_train.csv')
