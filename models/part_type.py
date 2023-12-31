# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class supplier_approve(models.Model):
#     _name = 'supplier_approve.supplier_approve'
#     _description = 'supplier_approve.supplier_approve'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class ProductType(models.Model):
    _name = 'supplier_approve.product_type'
    _description ='vcs.supplier_approve.product_type'

    fcskid = fields.Char(string="FCSKID")
    name = fields.Char(string="Name")
    description = fields.Text(string="Description")