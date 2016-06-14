# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Patient(models.Model):    
    _name = "hc.res.patient"    
    _description = "Patient"
    _inherit = ["hc.res.person"]

    is_deceased = fields.Boolean(string="Deceased", help="Indicates if the patient is deceased or not.")
    deceased_date = fields.Datetime(string="Deceased Date", help="When the patient was deceased.")
    marital_status_id = fields.Many2one(comodel_name="hc.vs.marital.status", string="Marital Status", help="Marital (civil) status of a patient.")
    is_multiple_birth = fields.Boolean(string="Multiple Birth", help="Whether patient is part of a multiple birth.")
    multiple_birth_count = fields.Integer(string="Multiple Birth Count", size=1, help="Number of births in a multiple birth.")
    multiple_birth_order = fields.Integer(string="Multiple Birth Order", size=1, help="The actual birth order in a multiple birth.")
    # care_provider_practitioner_ids = fields.One2many(comodel_name="hc.res.practitioner", inverse_name="patient_id", string="Care Provider Practitioners", help="Practitioner who is patient's nominated care provider.")
    # care_provider_organization_ids = fields.One2many(comodel_name="hc.res.organization", inverse_name="patient_id", string="Care Provider Organizations", help="Organization who is patient's nominated care provider.")
    # managing_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Managing Organization", help="Organization that is the custodian of the patient record.")
    is_active = fields.Boolean(string="Active", help="Whether this patient's record is in active use.")

class MaritalStatus(models.Model):  
    _name = "hc.vs.marital.status"  
    _description = "Marital Status" 
    _inherit = ["hc.value.set.contains"]

class PatientContact(models.Model): 
    _name = "hc.patient.contact"    
    _description = "Patient Contact"    
    _inherit = ["hc.res.person"]

class ContactRelationship(models.Model):    
    _name = "hc.vs.contact.relationship"    
    _description = "Contact Relationship"   
    _inherit = ["hc.value.set.contains"]

class PatientAnimal(models.Model):  
    _name = "hc.patient.animal" 
    _description = "Patient Animal" 

class AnimalSpecies(models.Model):  
    _name = "hc.vs.animal.species"  
    _description = "Animal Species" 
    _inherit = ["hc.value.set.contains"]

class AnimalBreed(models.Model):    
    _name = "hc.vs.animal.breed"    
    _description = "Animal Breed"   
    _inherit = ["hc.value.set.contains"]

class AnimalGenderStatus(models.Model): 
    _name = "hc.vs.animal.gender.status"    
    _description = "Animal Gender Status"   
    _inherit = ["hc.value.set.contains"]

class PatientCommunication(models.Model):   
    _name = "hc.patient.communication"  
    _description = "Patient Communication"

class PatientLink(models.Model):    
    _name = "hc.patient.link"   
    _description = "Patient Link"   


# class hc_patient(models.Model):
#     _name = 'hc_patient.hc_patient'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100