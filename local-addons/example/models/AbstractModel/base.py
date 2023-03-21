# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Tool(models.AbstractModel):
    _name = 'example.base'
    _description = '基础模型'
    _order = 'sequence, id desc'

    sequence = fields.Integer(default=1)
    active = fields.Boolean(string="是否归档", default=True)

    def do_archive(self):
        for record in self:
            record.active = not record.active

    def unlink(self):
        for record in self:
            record.active = False
