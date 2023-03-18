# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class go_fdfs(models.Model):
#     _name = 'go_fdfs.go_fdfs'
#     _description = 'go_fdfs.go_fdfs'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
