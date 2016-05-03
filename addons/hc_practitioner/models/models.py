# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Practitioner(models.Model):	
	_name = "hc.res.practitioner"	
	_description = "Practitioner"	
	_inherit = ["hc.res.person"]

class PractitionerRole(models.Model):	
	_name = "hc.practitioner.role"	
	_description = "Practitioner Role"	

# class hc_practitioner(models.Model):
#     _name = 'hc_practitioner.hc_practitioner'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100