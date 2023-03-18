# -*- coding: utf-8 -*-
# from odoo import http


# class GoFdfs(http.Controller):
#     @http.route('/go_fdfs/go_fdfs', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/go_fdfs/go_fdfs/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('go_fdfs.listing', {
#             'root': '/go_fdfs/go_fdfs',
#             'objects': http.request.env['go_fdfs.go_fdfs'].search([]),
#         })

#     @http.route('/go_fdfs/go_fdfs/objects/<model("go_fdfs.go_fdfs"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('go_fdfs.object', {
#             'object': obj
#         })
