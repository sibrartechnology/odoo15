# -*- coding: utf-8 -*-

from odoo import models, fields, api


class multi_view(models.Model):
    _name = 'multi_view.multi_view'
    _description = 'multi_view.multi_view'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
