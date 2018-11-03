# -*- coding: utf-8 -*-
"""
 		lib.py

 		Abstract, general purpose. Can be Unit-tested.
 		Is completely standard. Gives service to all Users.

 		Created: 			3 Nov 2018
 		Last up: 	 		3 Nov 2018
"""
import datetime


#------------------------------------------------ Date - Correct for Utc - With Delta--------------
def correct_date_delta(date, delta_hou=0, delta_min=0, delta_sec=0):
	"""
	Correct Date Delta
	"""
	#print
	#print 'Correct Date'
	
	date_format = "%Y-%m-%d %H:%M:%S"
	
	date_dt = datetime.datetime.strptime(date, date_format) + datetime.timedelta(hours=delta_hou, minutes=delta_min, seconds=delta_sec)
	
	date_s = date_dt.strftime(date_format)
	
	return date_s, date_dt
