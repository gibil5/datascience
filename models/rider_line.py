# -*- coding: utf-8 -*-

"""
	Rider Line

 	Created: 				27 Oct 2018
 	Last mod: 				27 Oct 2018
"""

from openerp import models, fields, api
#from openerp import models, fields

class RiderLine(models.Model):
	"""
	Rider
	"""
	_name = 'datascience.rider_line'

	_order = 'name asc'

	#_inherit=''




# -------------------------------------------------- Handles --------------------------------------

	rider_id = fields.Many2one(
			'datascience.rider', 
			ondelete='cascade', 
		)



# -------------------------------------------------------------------------------------------------

	idx = fields.Integer()





# -------------------------------------------------------------------------------------------------
	# RiderID
	name = fields.Char(
			"Name",
		)

	index = fields.Integer(
			"Index",
		)

	date = fields.Date()

	date_time = fields.Datetime()

	time = fields.Datetime()



	average_gradient = fields.Float()

	max_gradient = fields.Float()

	distance = fields.Float()



	highest_point = fields.Float()

	lowest_point = fields.Float()

	measured_time = fields.Float()




	moving_time = fields.Float()

	average_heart_rate = fields.Float()

	max_heart_rate = fields.Float()




	speed = fields.Float()

	power = fields.Float()

	cadence = fields.Float()



#1;78294;"2015-02-09";"05:50:12";0;5;9980.4;128.4;124.6;1375;1375;105.8;114;7.25847272727273;92.4;85.3
