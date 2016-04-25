# -*- coding: utf-8 -*-

from openerp import models, fields, api

class RelatedPerson(models.Model):  
    _name = "hc.res.related.person" 
    _description = "Related Person"
    _inherit = ["hc.res.person"]

#    patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Patient", required=True, help="The patient this person is related to.")     
    relationship_id = fields.Many2one(comodel_name="hc.vs.related.person.relationship.type", string="Relationship", help="The nature of the relationship.")
    start_date = fields.Datetime(string="Start Date", help="Start of the period of time that this relationship is considered valid.")       
    end_date = fields.Datetime(string="End Date", help="End of the period of time that this relationship is considered valid.")

class RelatedPersonRelationshipType(models.Model):  
    _name = "hc.vs.related.person.relationship.type"    
    _description = "Related Person Relationship Type"
    _inherit = ["hc.value.set.contains"]

# class RelatedPersonIdentifier(models.Model):    
#     _name = "hc.related.person.identifier"  
#     _description = "Related Person Identifier"  
#     _inherit = ["hc.person.identifier"]

# class RelatedPersonName(models.Model):  
#     _name = "hc.related.person.name"    
#     _description = "Related Person Name"    
#     _inherit = ["hc.person.name"]

# class RelatedPersonTelecom(models.Model):   
#     _name = "hc.related.person.telecom" 
#     _description = "Related Person Telecom" 
#     _inherit = ["hc.person.telecom"]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
# class RelatedPersonAttachment(models.Model):    
#     _name = "hc.related.person.attachment"  
#     _description = "Related Person Attachment"  
#     _inherit = ["hc.person.attachment"]

# class RelatedPersonAddress(models.Model):   
#     _name = "hc.related.person.address" 
#     _description = "Related Person Address" 
#     _inherit = ["hc.person.address"]

# class hc_related_person(models.Model):
#     _name = 'hc_related_person.hc_related_person'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100