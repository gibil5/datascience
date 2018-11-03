# -*- coding: utf-8 -*-
"""
	Rider

 	Created: 				27 Oct 2018
 	Last mod: 				27 Oct 2018

"""
from openerp import models, fields, api
import data_model
import os
import lib

class Rider(models.Model):
	"""
	Rider
	"""
	_name = 'datascience.rider'
	_order = 'name asc'
	#_inherit=''



# -------------------------------------------------------------------------------------------------
	# Import
	@api.multi 
	def import_data(self):
		print
		print 'Import'


		self.clear()



		# Init
		base_dir = os.environ['HOME']
		path = base_dir + "/challenge/" + self.file_name



		#p1 = data_model.Rider('1', self.file_name)
		p1 = data_model.Rider('1', path)


		print p1
		

		self.count = len(p1)


		idx = 0 

		for line in p1.data: 
			
			#print line


			date = line['Date'] + ' ' + line['Time']
			
			date_time, dt = lib.correct_date_delta(date, 5, 0, 0)

			#time = dt.time()
			#time = date_time.split()[1]
			time = line['Time']

			print time



			self.rider_line.create({
										'idx': 	idx, 


										'name': 	line['RiderID'], 
										'index':	line['Index'],



										#'date_time': 	line['Date'] + ' ' + line['Time'], 
										'date_time': 	date_time, 

										#'date': 	line['Date'], 
										'date': 	date_time, 

										'time': 	time, 



										'average_gradient': 	line['Average_Gradient'], 
										'max_gradient': 		line['Max_Gradient'], 
										'distance': 			line['Distance'], 

										'highest_point': 			line['Highest_point'], 
										'lowest_point': 			line['Lowest_point'], 
										'measured_time': 			line['Measured_time'], 

										'moving_time': 				line['Moving_time'], 
										'average_heart_rate': 		line['Average_heart_rate'], 
										'max_heart_rate': 			line['Max_heart_rate'], 


										'speed': 			line['Speed'], 
										'power': 			line['Power'], 
										'cadence': 			line['Cadence'], 


										'rider_id': 	self.id, 
			})

			idx = idx + 1




	# Clear
	@api.multi 
	def clear(self):
		print
		print 'Clear'
		self.rider_line.unlink()




# Fields
# -------------------------------------------------------------------------------------------------

	name = fields.Char(
			"Name",
			required=True,
		)


	date_begin = fields.Datetime()


	date_end = fields.Datetime()


	count = fields.Integer()



	# Lines
	rider_line = fields.One2many(
			'datascience.rider_line', 
			'rider_id', 
		)


	# File name 
	#file_name = fields.Char()
	file_name = fields.Selection(
			[
				('dtra.csv', 			'dtra'),
				('data_train.csv', 		'data_train'),
				('data_test.csv', 		'data_test'),
			],
			#selection = pat_vars._id_doc_type_list, 
		)

	# Max
	#max_import = fields.Integer()




#1;78294;"2015-02-09";"05:50:12";0;5;9980.4;128.4;124.6;1375;1375;105.8;114;7.25847272727273;92.4;85.3
