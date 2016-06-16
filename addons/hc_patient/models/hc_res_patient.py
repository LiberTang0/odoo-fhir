# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Patient(models.Model):    
    _name = "hc.res.patient"    
    _description = "Patient"
    _inherits = {"hc.res.person": "person_id"}

    person_id = fields.Many2one(
        comodel_name="hc.res.person",
        string="Person",
        required=True,
        ondelete="restrict",
        help="Person who is this patient.")
    birth_time = fields.Char(
        string="Birth Time", 
        help="The time when the patient was born.")
    is_deceased = fields.Boolean(
        string="Deceased", 
        default=False, 
        help="Indicates if the patient is deceased or not.")
    deceased_date = fields.Date(
        string="Deceased Date", 
        help="The date when the patient died.")
    deceased_time = fields.Char(
        string="Deceased Time", 
        help="The time when the patient died.")
    marital_status_ids = fields.One2many(
        comodel_name="hc.patient.marital.status",
        inverse_name="patient_id", 
        string="Marital Statuses", 
        help="Marital (civil) status of a person.")
    race_ids = fields.Many2many(
        comodel_name="hc.vs.race", 
        relation="race_patient_rel", 
        string="Races", 
        help="General race category reported by the patient - subject may have more than one.")
    ethnicity_ids = fields.Many2many(
        comodel_name="hc.vs.ethnicity", 
        relation="ethnicity_patient_rel", 
        string="Ethnicities", 
        help="General ethnicity category reported by the patient - subject may have more than one.")
    is_multiple_birth = fields.Boolean(
        string="Multiple Birth", 
        help="Whether patient is part of a multiple birth.")
    multiple_birth_count = fields.Integer(
        string="Multiple Birth Count", 
        size=1, 
        help="Number of births in a multiple birth.")
    multiple_birth_order = fields.Integer(
        string="Multiple Birth Order", 
        size=1, 
        help="The actual birth order in a multiple birth.")
    # care_provider_practitioner_ids = fields.One2many(comodel_name="hc.res.practitioner", inverse_name="patient_id", string="Care Provider Practitioners", help="Practitioner who is patient's nominated care provider.")
    # care_provider_organization_ids = fields.One2many(comodel_name="hc.res.organization", inverse_name="patient_id", string="Care Provider Organizations", help="Organization who is patient's nominated care provider.")
    # managing_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Managing Organization", help="Organization that is the custodian of the patient record.")
    is_active_patient = fields.Boolean(
        string="Active Patient", 
        adefault=True, 
        help="Whether this patient's record is in active use.")
    is_patient = fields.Boolean(string="Patient", default=True, help="Indicates a patient record.")

class MaritalStatus(models.Model):  
    _name = "hc.vs.marital.status"  
    _description = "Marital Status" 
    _inherit = ["hc.value.set.contains"]

class PatientMaritalStatus(models.Model):   
    _name = "hc.patient.marital.status"  
    _description = "Patient Marital Status"
    _inherit = ["hc.basic.association"]

    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Patient associated with this marital status.")
    marital_status_id = fields.Many2one(
        comodel_name="hc.vs.marital.status", 
        string="Marital Status", 
        help="Marital Status associated with this patient.")

class Race(models.Model):  
    _name = "hc.vs.race"  
    _description = "Race" 
    _inherit = ["hc.value.set.contains"]

class Ethnicity(models.Model):  
    _name = "hc.vs.ethnicity"  
    _description = "Ethnicity" 
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