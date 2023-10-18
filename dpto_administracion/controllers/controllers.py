# -*- coding: utf-8 -*-
# from odoo import http


# class DelegacionUnica(http.Controller):
#     @http.route('/delegacion_unica/delegacion_unica/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/delegacion_unica/delegacion_unica/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('delegacion_unica.listing', {
#             'root': '/delegacion_unica/delegacion_unica',
#             'objects': http.request.env['delegacion_unica.delegacion_unica'].search([]),
#         })

#     @http.route('/delegacion_unica/delegacion_unica/objects/<model("delegacion_unica.delegacion_unica"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('delegacion_unica.object', {
#             'object': obj
#         })
