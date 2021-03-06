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
    is_patient = fields.Boolean(string="Is a Patient", default=True, help="Indicates a patient record.")

# class Person(models.Model):
 
#     _inherit = ["hc.res.person"]

#     is_patient = fields.Boolean(
#         string="Is a Patient", 
#         help="This person is a patient.")

#     target_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Target Patient", required=True, help="Patient who is the resource to which this actual person is associated.")

class PatientIdentifier(models.Model):  
    _name = "hc.patient.identifier" 
    _description = "Patient Identifier"         
    _inherits = {"hc.person.identifier": "person_identifier_id"}

    person_identifier_id = fields.Many2one(
        comodel_name="hc.person.identifier", 
        string="Person Identifier",
        required=True,
        ondelete="restrict", 
        help="Identifies person identifier associated with this patient.")
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Identifies patient associated with this person identifier.")                    

class PatientName(models.Model):    
    _name = "hc.patient.name"   
    _description = "Patient Name"           
    _inherits = {"hc.person.name": "person_name_id"}

    person_name_id = fields.Many2one(
        comodel_name="hc.person.name", 
        string="Person Name", 
        required=True, 
        ondelete="restrict", 
        help="Identifies person name associated with this patient.")                  
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Identifies patient associated with this person name.")                  

class PatientTelecom(models.Model): 
    _name = "hc.patient.telecom"    
    _description = "Patient Telecom"            
    _inherits = {"hc.person.telecom": "person_telecom_id"}

    person_telecom_id = fields.Many2one(
        comodel_name="hc.person.telecom", 
        string="Person Telecom", 
        required=True, 
        ondelete="restrict", 
        help="Identifies person telecom associated with this patient.")                  
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Identifies patient associated with this person telecom.")                   


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

    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        tring="Patient", 
        help="Identifies patient associated with contact.")
    relationship_ids = fields.One2many(
        comodel_name="hc.patient.contact.relationship", 
        inverse_name="patient_contact_id", 
        string="Relationships", 
        help="The kind of relationship.")
    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Organization", 
        help="Organization that is associated with the contact.")
    start_date = fields.Datetime(
        string="Valid from", 
        help="Start of the the period during which this contact person or organization is valid to be contacted relating to this patient.")
    end_date = fields.Datetime(
        string="Valid to", 
        help="End of the the period during which this contact person or organization is valid to be contacted relating to this patient.")
 
class ContactRelationship(models.Model):    
    _name = "hc.vs.patient.contact.relationship"    
    _description = "Patient Contact Relationship"   
    _inherit = ["hc.value.set.contains"]

class PatientContactRelationship(models.Model): 
    _name = "hc.patient.contact.relationship"   
    _description = "Patient Contact Relationship"       
    _inherit = ["hc.basic.association"]

    patient_contact_id = fields.Many2one(
        comodel_name="hc.patient.contact", 
        string="Contact", 
        help="Identifies patient contact associated with this contact relationship.")             
    contact_relationship_id = fields.Many2one(
        comodel_name="hc.vs.patient.contact.relationship", 
        string="Patient Contact Relationship", 
        help="Identifies contact relationship associated with this patient contact.")              

class PatientAnimal(models.Model):  
    _name = "hc.patient.animal" 
    _description = "Patient Animal" 

    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Identifies patient associated with animal.")
    species_id = fields.Many2one(
        comodel_name="hc.vs.animal.species", 
        string="Species", 
        help="Identifies the high level taxonomic categorization of the kind of animal (e.g., dog, cow).")
    breed_id = fields.Many2one(
        comodel_name="hc.vs.animal.breed", 
        string="Breed", 
        help="Identifies the detailed categorization of the kind of animal (e.g., poodle, angus).")
    gender_status_id = fields.Many2one(
        comodel_name="hc.vs.animal.gender.status", 
        string="Gender Status", 
        help="Indicates the current state of the animal's reproductive organs (e.g., neutered, intact).")

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

    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", help="Identifies patient associated with communication.")
    language_id = fields.Many2one(
        comodel_name="res.lang", 
        string="Language", 
        help="The language which can be used to communicate with the patient about his or her health.")
    is_preferred = fields.Boolean(
        string="Preferred", 
        help="Language preference indicator.")


class PatientLink(models.Model):    
    _name = "hc.patient.link"   
    _description = "Patient Link"

    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Identifies patient associated with link.")
    other_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Other Patient", 
        required=True, 
        help="The other patient resource that the link refers to.")
    type = fields.Selection(
        string="Link Type", 
        selection=[
            ("replace", "Replace"), 
            ("refer", "Refer"), 
            ("seealso - type of link", "Seealso - Type Of Link")], 
        help="The type of link between this patient resource and another patient resource.")