# -*- coding: utf-8 -*-
# from odoo import http


# class ResPartner(http.Controller):
#     @http.route('/res_partner/res_partner', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/res_partner/res_partner/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('res_partner.listing', {
#             'root': '/res_partner/res_partner',
#             'objects': http.request.env['res_partner.res_partner'].search([]),
#         })

#     @http.route('/res_partner/res_partner/objects/<model("res_partner.res_partner"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('res_partner.object', {
#             'object': obj
#         })
