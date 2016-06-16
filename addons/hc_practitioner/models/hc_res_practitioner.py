# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Practitioner(models.Model):   
    _name = "hc.res.practitioner"   
    _description = "Practitioner"   
    _inherits = {"hc.res.person": "person_id"}

    person_id = fields.Many2one(
        comodel_name="hc.res.person",
        string="Person",
        required=True,
        ondelete="restrict",
        help="Person associated with this practitioner.")
    is_active_practitioner = fields.Boolean(
        string="Active Practitioner", 
        default=True, 
        help="Whether this practitioner's record is in active use.")
    qualification_ids = fields.One2many(
        comodel_name="hc.practitioner.qualification", 
        inverse_name="practitioner_id", 
        string="Qualification", 
        help="Qualification obtained by training and certification")
    role_ids = fields.One2many(
        comodel_name="hc.practitioner.role", 
        inverse_name="practitioner_id", 
        string="Role", 
        help="Roles/organizations that the practitioner is associated with.")

class PractitionerQualification(models.Model):  
    _name = "hc.practitioner.qualification" 
    _description = "Practitioner Qualification"
    _inherit = ["hc.basic.association"]

    practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Practitioner", 
        help="Practitioner who associated with this qualification.")
    code_id = fields.Many2one(
        comodel_name="hc.vs.occupation.code", 
        string="Qualification Code", 
        help="Coded representation of the qualification.") 
    identifier_ids = fields.One2many(
        comodel_name="hc.practitioner.qualification.identifier", 
        inverse_name="practitioner_qualification_id", 
        string="Identifiers", 
        help="An identifier for this qualification for the practitioner.")                 
    # issuer_organization_id = fields.Many2one(
    #     comodel_name="hc.res.organization", 
    #     string="Issuer Organization", 
    #     help="Organization that regulates and issues the qualification.")        

class OccupationCode(models.Model):  
    _name = "hc.vs.occupation.code"  
    _description = "Occupation Code" 
    _inherit = ["hc.value.set.contains"]

class PractitionerQualificationIdentifier(models.Model):  
    _name = "hc.practitioner.qualification.identifier"  
    _description = "Occupation Code" 
    _inherit = ["hc.person.identifier"]

    practitioner_qualification_id = fields.Many2one(
        comodel_name="hc.practitioner.qualification", 
        string="Practitioner Qualification", 
        help="Practitioner Qualification which is associated with this identifier.")

class PractitionerRole(models.Model):   
    _name = "hc.practitioner.role"  
    _description = "Practitioner Role"
    _inherit = ["hc.basic.association"]
    
    practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Practitioner", 
        help="Practitioner that is able to provide the defined services for the organization.")
    # organization_id = fields.Many2one(
    #     comodel_name="hc.res.organization", 
    #     string="Organization", 
    #     help="Organization where the roles are performed.")
    role_id = fields.Many2one(
        comodel_name="hc.vs.practioner.role", 
        string="Role", 
        help="Roles which this practitioner may perform.")
    specialty_ids = fields.One2many(
        comodel_name="hc.practitioner.role.specialty", 
        inverse_name="practitioner_role_id", 
        string="Specialties", 
        help="Specific specialty of the practitioner.")
    identifier_ids = fields.One2many(
        comodel_name="hc.practitioner.role.identifier", 
        inverse_name="practitioner_role_id", 
        string="Identifiers", 
        help="Business Identifiers that are specific to a role/location.")
    is_active = fields.Boolean(
        string="Active", 
        help="Whether this practitioner's record is in active use.")
    telecom_ids = fields.One2many(
        comodel_name="hc.practitioner.role.telecom", 
        inverse_name="practitioner_role_id", 
        string="Telecoms", 
        help="Contact details that are specific to the role/location/service.")
    start_date = fields.Datetime(
        string="Start Date", 
        help="Start of the the period during which the practitioner is authorized to perform in these role(s).")
    end_date = fields.Datetime(
        string="End Date", 
        help="End of the the period during which the practitioner is authorized to perform in these role(s).")
    location_ids = fields.Many2many(
        comodel_name="hc.practitioner.role.location", 
        inverse_name="practitioner_role_id",       
        relation="location_practitioner_role_rel",
        string="Locations", 
        help="The location(s) at which this practitioner provides care.")
    healthcare_service_ids = fields.One2many(
        comodel_name="hc.practitioner.role.healthcare.service", 
        inverse_name="practitioner_role_id", 
        string="Healthcare Services", 
        help="The list of healthcare services that this worker provides for this role's Organization/Location(s).")
    availability_exceptions = fields.Char(
        string="Availability Exceptions", 
        help="Description of availability exceptions.")

class PractitionerRoleRole(models.Model):  
    _name = "hc.vs.practioner.role"  
    _description = "Practitioner Role" 
    _inherit = ["hc.value.set.contains"]

class PractitionerRoleSpecialty(models.Model):  
    _name = "hc.practitioner.role.specialty"    
    _description = "Practitioner Role Specialty"        
    _inherit = ["hc.basic.association"]

    practitioner_role_id = fields.Many2one(
        comodel_name="hc.practitioner.role", 
        string="Practitioner Role", 
        help="Practitioner role associated with a specialty.")              
    practitioner_specialty_id = fields.Many2one(
        comodel_name="hc.vs.practitioner.specialty", 
        string="Specialty", 
        help="Specialty associated with a practitioner role.")             
    is_active = fields.Boolean(
        string="Active", 
        help="Whether this practioner role record is in active use.")               
    start_date = fields.Datetime(
        string="Start Date", 
        help="Start of the period when the practitioner role specialty is/was valid.")                
    end_date = fields.Datetime(
        string="End Date", 
        help="End of the period when the practitioner role specialty is/was valid.")              

class PractitionerSpecialty(models.Model):  
    _name = "hc.vs.practitioner.specialty"  
    _description = "Practitioner Specialty"     
    _inherit = ["hc.value.set.contains"]

class PractitionerRoleIdentifier(models.Model): 
    _name = "hc.practitioner.role.identifier"   
    _description = "Practitioner Role Identifier"       
    _inherit = ["hc.basic.association"]
    
    practitioner_role_id = fields.Many2one(
        comodel_name="hc.practitioner.role", 
        string="Practitioner Role", 
        help="Practitioner role associated with this identifier.")              
    identifier_id = fields.Many2one(
        comodel_name="hc.identifier", 
        string="Identifier", 
        help="Identifier associated with this practitioner role.")               
    identifier_use = fields.Selection(
        string="Identifier Use", 
        selection=[
            ("usual", "Usual"), 
            ("official", "Official"), 
            ("temp", "Temporary"), 
            ("secondary", "Secondary")], 
        help="The purpose of this identifier.")             
    value = fields.Char(
        string="Value", 
        help="The portion of the identifier typically relevant to the user and which is unique within the context of the system.")              

class PractitionerRoleTelecom(models.Model):    
    _name = "hc.practitioner.role.telecom"  
    _description = "Practitioner Role Telecom"      
    _inherit = ["hc.basic.association"]
    
    practitioner_role_id = fields.Many2one(
        comodel_name="hc.practitioner.role", 
        string="Practitioner Role", 
        help="Practitioner role associated with this telecom contact point.")               
    telecom_id = fields.Many2one(
        comodel_name="hc.telecom", 
        string="Telecom", 
        help="Telecom contact point associated with this practitioner role.")             
    telecom_use = fields.Selection(
        string="Telecom Use", 
        selection=[
            ("home", "Home"), 
            ("work", "Work"), 
            ("temp", "Temp"), 
            ("old", "Old"), 
            ("mobile", "Mobile")], 
        help="The purpose for the telecom contact point.")             

class PractitionerRoleLocation(models.Model):   
    _name = "hc.practitioner.role.location" 
    _description = "Practitioner Role Location"     
    _inherit = ["hc.basic.association"]
    
    practitioner_role_id = fields.Many2one(
        comodel_name="hc.practitioner.role", 
        string="Practitioner Role", 
        help="Practitioner role associated with this location.")                
    # location_id = fields.Many2one(
    #     comodel_name="hc.res.location", 
    #     string="Location", 
    #     help="Location associated with this practitioner role.")               

class PractitionerRoleSpecialty(models.Model):  
    _name = "hc.practitioner.role.specialty"    
    _description = "Practitioner Role Specialty"        
    _inherit = ["hc.basic.association"]
    
    practitioner_role_id = fields.Many2one(
        comodel_name="hc.practitioner.role", 
        string="Practitioner Role", 
        help="Practitioner role associated with a specialty.")              
    practitioner_specialty_id = fields.Many2one(
        comodel_name="hc.vs.practitioner.specialty", 
        string="Specialty", 
        help="Specialty associated with a practitioner role.")             
    is_active = fields.Boolean(
        string="Active", 
        help="Whether this practioner role record is in active use.")               
    start_date = fields.Datetime(
        string="Start Date", 
        help="Start of the period when the practitioner role specialty is/was valid.")                
    end_date = fields.Datetime(
        string="End Date", 
        help="End of the period when the practitioner role specialty is/was valid.")              

class PractitionerRoleHealthcareService(models.Model):  
    _name = "hc.practitioner.role.healthcare.service"   
    _description = "Practitioner Role Healthcare Service"       
    _inherit = ["hc.basic.association"]

    practitioner_role_id = fields.Many2one(
        comodel_name="hc.practitioner.role", 
        string="Practitioner Role", 
        help="Practitioner role associated with this healthcare service.")              
    # healthcare_service_id = fields.Many2one(
    #     comodel_name="hc.res.healthcare service", 
    #     string="Healthcare Service", 
    #     help="Healthcare service associated with this practitioner role.")               

class AvailableTime(models.Model):  
    _name = "hc.available.time" 
    _description = "Available Time"

    practitioner_role_id = fields.Many2one(
        comodel_name="hc.practitioner.role", 
        string="Practitioner Role", 
        help="Practitioner role associated with available time.")       
    days_of_week = fields.Selection(
        string="Days Of Week", 
        selection=[
            ("mon", "Mon"), 
            ("tue", "Tue"), 
            ("wed", "Wed"), 
            ("thu", "Thu"), 
            ("fri", "Fri"), 
            ("sat", "Sat"), 
            ("sun", "Sun")], 
        help="The days of the week.")        
    is_all_day = fields.Boolean(
        string="All Day", 
        help="Always available? e.g. 24 hour service.")       
    available_start_time = fields.Char(
        string="Available Start Time", 
        help="Opening time of day (ignored if allDay = true).")       
    available_end_time = fields.Char(
        string="Available End Time", 
        help="Closing time of day (ignored if allDay = true).")       

class NotAvailableTime(models.Model):   
    _name = "hc.not.available.time" 
    _description = "Not Available Time"     

    description = fields.Char(
        string="Description", 
        help="Reason presented to the user explaining why time not available.")             
    not_available_start_time = fields.Char(
        string="Not Available Start Time", 
        help="Start of the period service not available from this date.")             
    not_available_end_time = fields.Char(
        string="Not Available End Time", 
        help="End of the period service not available from this date.")               
    practitioner_role_id = fields.Many2one(
        comodel_name="hc.practitioner.role", 
        string="Practitioner Role", 
        help="Practitioner role associated with time not available.")               

class AvailableTimeDaysOfWeek(models.Model):    
    _name = "hc.available.time.days.of.week"    
    _description = "Available Time Days Of Week"        

    days_of_week = fields.Selection(
        comodel_name="", 
        string="Days Of Week", 
        selection=[
            ("mon", "Mon"), 
            ("tue", "Tue"), 
            ("wed", "Wed"), 
            ("thu", "Thu"), 
            ("fri", "Fri"), 
            ("sat", "Sat"), ("sun", "Sun")], 
            help="Day of Week associated with the available time.")             
    available_time_id = fields.Many2one(
        comodel_name="hc.available.time", 
        string="Available Time", 
        help="Available time associated with the day of week.")              