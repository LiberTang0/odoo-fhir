# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Organization(models.Model):   
    _name = "hc.res.organization"   
    _description = "Organization"       
    _inherit = ["res.partner"]

    identifier_ids = fields.One2many(
        comodel_name="hc.organization.identifier", 
        inverse_name="organization_id", 
        string="Identifiers", 
        help="Identifies this organization across multiple systems.")             
    name = fields.Char(
        string="Name", 
        help="Name used for the organization.")               
    type_id = fields.Many2one(
        comodel_name="hc.vs.organization.type", 
        string="Type", 
        help="Kind of organization.")              
    telecom_contact_ids = fields.One2many(
        comodel_name="hc.organization.telecom", 
        inverse_name="organization_id", 
        string="Telecom Contacts", 
        help="A contact detail for the organization.")             
    address_ids = fields.One2many(
        comodel_name="hc.organization.address", 
        inverse_name="organization_id", 
        string="Addresses", 
        help="An address for the organization.")               
    part_of_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Part Of", 
        help="The organization of which this organization forms a part.")                
    is_active = fields.Boolean(
        string="Active", 
        help="Whether the organization's record is still in active use.")               
				
class OrganizationIdentifier(models.Model):   
    _name = "hc.organization.identifier"  
    _description = "Organization Identifier"
    _inherit = ["hc.object.identifier"]

    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Organization", 
        help="Organization associated with this identifier.")
    # identifier_id = fields.Many2one(
    #     help="Identifier associated with this organization.")
    # value = fields.Char(
    #     string="Value", 
    #     help="The value of this identifier that is unique.")    

class OrganizationType(models.Model):  
    _name = "hc.vs.organization.type"  
    _description = "Organization Type" 
    _inherit = ["hc.value.set.contains"]

class OrganizationTelecom(models.Model):  
    _name = "hc.organization.telecom" 
    _description = "Organization Telecom"
    _inherit = ["hc.object.telecom"]
 
    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Organization", 
        help="Organization associated with this telecom contact point.")
    telecom_id = fields.Many2one(
        help="Telecom contact point associated with this organization.")

class OrganizationAddress(models.Model):

    _name = "hc.organization.address" 
    _description = "Organization Address"
    _inherit = ["hc.object.address"]

    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Organization", 
        help="Organization associated with this address.")

    address_id = fields.Many2one(
        help="Address associated with this organization.")

class OrganizationContact(models.Model):    
    _name = "hc.organization.contact"   
    _description = "Organization Contact"       
    _inherits = {"hc.res.person": "person_id"}

    person_id = fields.Many2one(
        comodel_name="hc.res.person", 
        string="Person",
        required=True,
        ondelete="restrict", 
        help="Person associated with this organization contact.") 
    purpose_id = fields.Many2one(
        comodel_name="hc.vs.organization.contact.purpose", 
        string="Purpose", 
        help="The type of contact.")              
    name_id = fields.Many2one(
        comodel_name="hc.human.name", 
        string="Name", 
        help="A name associated with the organization contact.")              
    telecom_contact_ids = fields.One2many(
        comodel_name="hc.organization.contact.telecom", 
        inverse_name="organization_contact_id", 
        string="Telecom Contacts", 
        help="Contact details (telephone, email, etc) for a contact.")             
    address_ids = fields.One2many(
        comodel_name="hc.organization.contact.address",
        inverse_name="organization_contact_id",  
        string="Addresses", 
        help="Visiting or postal addresses for the organization contact.")
    is_organization_contact = fields.Boolean(
        string="Active",
        default=True, 
        help="This person is an organization contact.")                

class OrganizationContactPurpose(models.Model): 
    _name = "hc.vs.organization.contact.purpose"    
    _description = "Organization Contact Purpose"       
    _inherit = ["hc.value.set.contains"]

class OrganizationContactAddress(models.Model):

    _name = "hc.organization.contact.address" 
    _description = "Organization Contact Address"
    _inherit = ["hc.object.address"]

    organization_contact_id = fields.Many2one(
        comodel_name="hc.organization.contact", 
        string="Organization Contact", 
        help="Organization contact associated with this address.")
    address_id = fields.Many2one(
        help="Address associated with this organization contact.")

class OrganizationContactTelecom(models.Model):  
    _name = "hc.organization.contact.telecom" 
    _description = "Organization Contact Telecom"
    _inherit = ["hc.object.telecom"]
 
    organization_contact_id = fields.Many2one(
        comodel_name="hc.organization.contact", 
        string="Organization Contact", 
        help="Organization contact associated with this telecom contact point.")
    telecom_id = fields.Many2one(
        help="Telecom contact point associated with this organization contact.")

class Person(models.Model):
 
    _inherit = ["hc.res.person"]

    is_organization_contact = fields.Boolean(
        string="Is an Organization Contact", 
        help="This person is an organization contact.")