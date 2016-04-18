# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ValueSetContains

    _name = "hc.value.set.contains"
    _description = "Value Set Contains"

    system = fields.Char(string="System", help="System value for the code")
    is_abstract = fields.Boolean(string="Abstract", help="If user cannot select this entry")
    version = fields.Char(string="Version", help="Version in which this code / display is defined")
    code = fields.Char(string="Code", help="Code - if blank, this is not a choosable code")
    display = fields.Char(string="Display", help="User display for the concept")
    level = fields.Integer(string="Level", help="Level in a hierarchy of codes")
    source = fields.Char(string="Source", help="The source of the definition of the code")
    definition = fields.Text(string="Definition", help="An explanation of the meaning of the concept")
    comments = fields.Text(string="Comments", help="Additional notes about how to use the code")


# class hc_base(models.Model):
#     _name = 'hc_base.hc_base'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100