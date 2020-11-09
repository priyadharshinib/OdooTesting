# -*- coding: utf-8 -*-
# from odoo import http


# class Accountstest(http.Controller):
#     @http.route('/accountstest/accountstest/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/accountstest/accountstest/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('accountstest.listing', {
#             'root': '/accountstest/accountstest',
#             'objects': http.request.env['accountstest.accountstest'].search([]),
#         })

#     @http.route('/accountstest/accountstest/objects/<model("accountstest.accountstest"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('accountstest.object', {
#             'object': obj
#         })
