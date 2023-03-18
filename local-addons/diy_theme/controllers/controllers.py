# -*- coding: utf-8 -*-
# from odoo import http


# class DiyTheme(http.Controller):
#     @http.route('/diy_theme/diy_theme', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/diy_theme/diy_theme/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('diy_theme.listing', {
#             'root': '/diy_theme/diy_theme',
#             'objects': http.request.env['diy_theme.diy_theme'].search([]),
#         })

#     @http.route('/diy_theme/diy_theme/objects/<model("diy_theme.diy_theme"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('diy_theme.object', {
#             'object': obj
#         })
