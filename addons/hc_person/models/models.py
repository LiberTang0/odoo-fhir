# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Person(models.Model): 

    _name = "hc.res.person" 
    _description = "Person"
#    _inherit = ["res.partner"]

    identifier_ids = fields.One2many(comodel_name="hc.person.identifier", inverse_name="person_id", string="Identifiers", help="A human identifier for this person.")
    name_ids = fields.One2many(comodel_name="hc.person.name", inverse_name="person_id", string="Names", help="A name associated with the person.")
    telecom_contact_ids = fields.One2many(comodel_name="hc.person.telecom", inverse_name="person_id", string="Telecom Contacts", help="A contact detail for the person.")
    gender = fields.Selection(string="Person Gender", 
        selection=[
            ("male", "Male"), 
            ("female", "Female"), 
            ("other", "Other"), 
            ("unknown", "Unknown")], 
            
        help="The gender of a person used for administrative purposes.")
#     birth_date = fields.Datetime(string="Birth Date", help="The birth date for the person.")
    address_ids = fields.One2many(comodel_name="hc.person.address", inverse_name="person_id", string="Addresses", 
        help="One or more addresses for the person.")
    photo_attachment_id = fields.Many2one(comodel_name="hc.person.attachment", string="Photo Attachment", help="Image of the Person.")
#     managing_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Managing Organization", help="The Organization that is the custodian of the person record.")
#     is_active = fields.Boolean(string="Active", help="This person's record is in active use.")

class PersonLink(models.Model): 

    _name = "hc.person.link"    
    _description = "Person Link"

    person_id = fields.Many2one(comodel_name="hc.res.person", string="Person", 
        help="Person associated with this link.")
#    target_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Target Patient", required=True, help="Patient who is the resource to which this actual person is associated.")
#    target_related_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Target Practitioner", help="Practitioner who is the resource to which this actual person is associated.")
#    target_related_person_id = fields.Many2one(comodel_name="hc.res.related.person", string="Target Related Person", help="Related Person who is the resource to which this actual person is associated.")
    target_person_id = fields.Many2one(comodel_name="hc.res.person", string="Target Person", help="Person who is the resource to which this actual person is associated.")

    assurance = fields.Selection(string="Link Assurance", 
        selection=[
            ("level1", "Level1"), 
            ("level2", "Level2"), 
            ("level3", "Level3"), 
            ("level4", "Level4")], 
        help="Level of assurance that this link is actually associated with the target resource.")

class PersonAddress(models.Model):

    _name = "hc.person.address" 
    _description = "Person Address"

    person_id = fields.Many2one(comodel_name="hc.res.person", string="Person", help="Entity associated with this address.")
    address_id = fields.Many2one(comodel_name="hc.address", string="Address", help="Address associated with this entity.")      
    is_active = fields.Boolean(string="Active", help="Whether this record is in active use.")       
    is_preferred = fields.Boolean(string="Preferred", help="Whether this record is preferred for use.")     
    use = fields.Selection(string="Use", 
        selection=[
            ("home", "Home"), 
            ("work", "Work"), 
            ("temp", "Temp"), 
            ("old", "Old")], 
        help="The purpose of this address.")
    type = fields.Selection(string="Type", default="Both", 
        selection=[
            ("postal", "Postal"), 
            ("physical", "Physical"), 
            ("both", "Both")], 
        help="Distinguishes between physical addresses (those you can visit) and mailing addresses (e.g. PO Boxes and care-of addresses). Most addresses are both.")
    start_date = fields.Datetime(string="Start Date", help="Start of the time period when address was/is in use.")      
    end_date = fields.Datetime(string="End Date", help="End of the time period when address was/is in use.")        

class PersonIdentifier(models.Model):   
    _name = "hc.person.identifier"  
    _description = "Person Identifier"

    person_id = fields.Many2one(comodel_name="hc.res.person", string="Person", help="Entity associated with this identifier.")
    identifier_id = fields.Many2one(comodel_name="hc.identifier", string="Identifier", help="Identifier associated with this entity.")
    use = fields.Selection(string="Use", 
        selection=[
            ("usual", "Usual"), 
            ("official", "Official"), 
            ("temp", "Temporary"), 
            ("secondary", "Secondary")], 
        help="The purpose of this identifier.")
    value = fields.Char(string="Value", help="The value that is unique.")
    start_date = fields.Datetime(string="Start Date", help="Start of the time period when identifier was/is in use.")
    end_date = fields.Datetime(string="End Date", help="End of the time period when identifier was/is in use.")

class PersonName(models.Model): 
    _name = "hc.person.name"    
    _description = "Person Name"

    person_id = fields.Many2one(comodel_name="hc.res.person", string="Person", help="Entity associated with this name.")
        
class PersonTelecom(models.Model):  
    _name = "hc.person.telecom" 
    _description = "Person Telecom"

    person_id = fields.Many2one(comodel_name="hc.res.person", string="Person", help="Entity associated with this telecom contact.")
    telecom_id = fields.Many2one(comodel_name="hc.telecom", string="Telecom", help="Telecom contact associated with this entity.")
    use = fields.Selection(string="Person Telecom Use", 
        selection=[
            ("home", "Home"), 
            ("work", "Work"), 
            ("temp", "Temp"), 
            ("old", "Old")], 
        help="Purpose of this telecom contact point.")
    start_date = fields.Datetime(string="Start Date", help="Start of the time period when the contact point was/is in use.")
    end_date = fields.Datetime(string="End Date", help="End of the time period when the contact point was/is in use.")
     
class PersonAttachment(models.Model):   
    _name = "hc.person.attachment"  
    _description = "Person Attachment"

    person_id = fields.Many2one(comodel_name="hc.res.person", string="Person", help="Entity associated with this attachment.")      
    attachment_id = fields.Many2one(comodel_name="hc.attachment", string="Attachment", help="Attachment associated with this entity.")      


# class hc_person(models.Model):
#     _name = 'hc_person.hc_person'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100