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
    # telecom_contact_ids = fields.One2many(
    #     comodel_name="hc.organization.telecom", 
    #     inverse_name="organization_id", 
    #     string="Telecom Contacts", 
    #     help="A contact detail for the organization.")             
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
    _inherit = ["hc.basic.association", "hc.identifier"]

    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Organization", 
        help="Organization associated with this identifier.")
    identifier_id = fields.Many2one(
        help="Identifier associated with this organization.")
    value = fields.Char(
        string="Value", 
        help="The value of this identifier that is unique.")    

class OrganizationType(models.Model):  
    _name = "hc.vs.organization.type"  
    _description = "Organization Type" 
    _inherit = ["hc.value.set.contains"]

# class EntityTelecom(models.Model):  
#     _name = "hc.entity.telecom" 
#     _description = "Entity Telecom"
#     _inherit = ["hc.basic.association"]
#     _inherits = {"hc.telecom": "telecom_id"}
 
#     telecom_id = fields.Many2one(
#         comodel_name="hc.telecom", 
#         string="Telecom", 
#         required=True,
#         ondelete="restrict", 
#         help="Telecom contact point associated with this entity.")
#     use = fields.Selection(string="Telecom Use", 
#         selection=[
#             ("home", "Home"), 
#             ("work", "Work"), 
#             ("temp", "Temp"), 
#             ("old", "Old"),
#             ("mobile", "Mobile")], 
#         help="Purpose of this telecom contact point.")

# class OrganizationTelecom(models.Model):  
#     _name = "hc.organization.telecom" 
#     _description = "Organization Telecom"
#     _inherit = ["hc.entity.telecom"]
 
#     organization_id = fields.Many2one(
#         comodel_name="hc.res.organization", 
#         string="Organization", 
#         help="Organization associated with this telecom contact point.")

#     telecom_id = fields.Many2one(
#         help="Telecom contact point associated with this organization.")

# class EntityAddress(models.Model):

#     _name = "hc.entity.address" 
#     _description = "Entity Address"
#     _inherit = ["hc.basic.association"]
#     _inherits = {"hc.address": "address_id"}

#     address_id = fields.Many2one(
#         comodel_name="hc.address", 
#         string="Address", 
#         required=True,
#         ondelete="restrict", 
#         help="Address associated with this entity.") 
#     use = fields.Selection(string="Use",
#         selection=[
#             ("home", "Home"), 
#             ("work", "Work"), 
#             ("temp", "Temp"), 
#             ("old", "Old")],
#         default="home",  
#         help="The purpose of this address.")
#     type = fields.Selection(string="Type", 
#         selection=[
#             ("postal", "Postal"), 
#             ("physical", "Physical"), 
#             ("both", "Both")], 
#         default="both", 
#         help="Distinguishes between physical addresses (those you can visit) and mailing addresses (e.g. PO Boxes and care-of addresses). Most addresses are both.")

class OrganizationAddress(models.Model):

    _name = "hc.organization.address" 
    _description = "Organization Address"
    _inherit = ["hc.entity.address"]

    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Organization", 
        help="Organization associated with this address.")

    address_id = fields.Many2one(
        help="Address associated with this organization.")

class OrganizationContact(models.Model):    
    _name = "hc.organization.contact"   
    _description = "Organization Contact"       
    # _inherits = {"hc.res.person": "person_id"}

    person_id = fields.Many2one(
        comodel_name="hc.res.person", 
        string="Person", 
        help="Person associated with this organization contact.") 
    purpose_id = fields.Many2one(
        comodel_name="hc.vs.organization.contact.purpose", 
        string="Purpose", 
        help="The type of contact.")              
    name_id = fields.Many2one(
        comodel_name="hc.human.name", 
        string="Name", 
        help="A name associated with the contact.")              
    # telecom_contact_ids = fields.One2many(
    #     comodel_name="hc.organization.contact.telecom", 
    #     inverse_name="organization_contact_id", 
    #     string="Telecom Contacts", 
    #     help="Contact details (telephone, email, etc) for a contact.")             
    address_ids = fields.One2many(
        comodel_name="hc.organization.contact.address",
        inverse_name="organization_contact_id",  
        string="Addresses", 
        help="Visiting or postal addresses for the contact.")
    is_organization_contact = fields.Boolean(
        string="Active",
        default=True, 
        help="This person is an organization contact.")                

class OrganizationContactAddress(models.Model):

    _name = "hc.organization.contact.address" 
    _description = "Organization Contact Address"
    _inherit = ["hc.entity.address"]

    organization_contact_id = fields.Many2one(
        comodel_name="hc.organization.contact", 
        string="Organization", 
        help="Organization contact associated with this address.")


# class Person(models.Model):
 
#     _inherit = ["hc.res.person"]

#     is_organization_contact = fields.Boolean(
#         string="Active", 
#         help="This person is an organization contact.")


# class hc_organization(models.Model):
#     _name = 'hc_organization.hc_organization'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100