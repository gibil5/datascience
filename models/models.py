# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class datascience(models.Model):
#     _name = 'datascience.datascience'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100