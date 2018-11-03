# -*- coding: utf-8 -*-
from openerp import http

# class Datascience(http.Controller):
#     @http.route('/datascience/datascience/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/datascience/datascience/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('datascience.listing', {
#             'root': '/datascience/datascience',
#             'objects': http.request.env['datascience.datascience'].search([]),
#         })

#     @http.route('/datascience/datascience/objects/<model("datascience.datascience"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('datascience.object', {
#             'object': obj
#         })