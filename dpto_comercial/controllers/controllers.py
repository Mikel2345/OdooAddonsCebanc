# -*- coding: utf-8 -*-
# from odoo import http


# class DptoComercial(http.Controller):
#     @http.route('/dpto_comercial/dpto_comercial/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dpto_comercial/dpto_comercial/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dpto_comercial.listing', {
#             'root': '/dpto_comercial/dpto_comercial',
#             'objects': http.request.env['dpto_comercial.dpto_comercial'].search([]),
#         })

#     @http.route('/dpto_comercial/dpto_comercial/objects/<model("dpto_comercial.dpto_comercial"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dpto_comercial.object', {
#             'object': obj
#         })
