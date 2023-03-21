# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Example(models.Model):
    _name = 'diy.example'
    _description = '自定义示例模型'
    # _rec_name = 'short_name'
    _order = 'id desc'
    _log_access = True

    name = fields.Char(string="名字")
    short_name = fields.Char(string="简要名称")
    sequence = fields.Integer(default=1)
    active = fields.Boolean(string="是否归档", default=True)
    state = fields.Selection(selection=[
        ('draft', "草案"),
        ('audit', "审核中"),
        ('yes', "通过"),
        ('no', "拒绝")
    ], string="状态")
    image = fields.Binary(string="照片")
    content = fields.Text(string="内容")
    description = fields.Html(string="介绍")
    date = fields.Date(string="日期")
    datetime = fields.Datetime(string="时间")
    money = fields.Monetary(string="货币")

    # 使用可配置精度浮点数字段
    example_price = fields.Float(string="示例价格", digits='Example Price')

    # 模型添加计算字段
    value = fields.Integer()
    value2 = fields.Float(compute='_value_pc',
                          digits=(15, 2),
                          store=True)

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    # 模型添加等级
    parent_id = fields.Many2one(comodel_name='diy.example', string="上级",
                                ondelete='restrict', index=True)
    child_ids = fields.One2many(comodel_name='diy.example', inverse_name='parent_id',
                                string="下级")
    parent_path = fields.Char(index=True)
    _parent_store = True
    _parent_name = 'parent_id'

    @api.constrains('parent_id')
    def _check_parent_id(self):
        """防止循环关系的检查"""
        if not self._check_recursion():
            raise models.ValidationError("错误！你不能创建递归记录。")

    # 模型添加约束验证
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', '错误！名字不能重复。')
    ]

    @api.constrains('name')
    def _check_name(self):
        for record in self:
            if not record.name:
                raise models.ValidationError("错误！名字必须设置。")

    def name_get(self):
        return [(record.id, "{id}:{name}".format(id=record.id, name=record.name)) for record in self]

    def unlink(self):
        for record in self:
            record.active = False
