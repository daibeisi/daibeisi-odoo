# -*- coding: utf-8 -*-
# from odoo import http


# class DiyHr(http.Controller):
#     @http.route('/diy_hr/diy_hr', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/diy_hr/diy_hr/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('diy_hr.listing', {
#             'root': '/diy_hr/diy_hr',
#             'objects': http.request.env['diy_hr.diy_hr'].search([]),
#         })

#     @http.route('/diy_hr/diy_hr/objects/<model("diy_hr.diy_hr"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('diy_hr.object', {
#             'object': obj
#         })
