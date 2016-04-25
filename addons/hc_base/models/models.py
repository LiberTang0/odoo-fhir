# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ValueSetContains(models.Model):

    _name = "hc.value.set.contains"
    _description = "Value Set Contains"

    system = fields.Char(string="System", help="System value for the code.")
    is_abstract = fields.Boolean(string="Abstract", help="If user cannot select this entry.")
    version = fields.Char(string="Version", help="Version in which this code / display is defined.")
    code = fields.Char(string="Code", help="Code - if blank, this is not a choosable code.")
    display = fields.Char(string="Display", help="User display for the concept.")
    level = fields.Integer(string="Level", help="Level in a hierarchy of codes.")
    source = fields.Char(string="Source", help="The source of the definition of the code.")
    definition = fields.Text(string="Definition", help="An explanation of the meaning of the concept.")
    comments = fields.Text(string="Comments", help="Additional notes about how to use the code.")

class Annotation(models.Model):

    _name = "hc.annotation"
    _description = "Annotation"

#     author_practitioner = fields.Many2one(comodel_name="hc.annotation.author.practitioner", string="Annotation Author Practitioner", 
#         help="Practitioner responsible for the annotation.")
    author_patient = fields.Many2one(comodel_name="hc.annotation.author.patient", string="Annotation Author Patient", 
        help="Patient responsible for the annotation.")
    author_related_person = fields.Many2one(comodel_name="hc.annotation.author.related.person", string="Annotation Author Related Person", 
        help="Related Person responsible for the annotation.")
    author = fields.Text(string="Author", help="Individual responsible for the annotation.")
    recorded_date = fields.Datetime(string="Recorded Date", help="When the annotation was made.")
    annotation = fields.Text(string="Annotation", help="The text content.")

class Address(models.Model):
    
    _name = "hc.address"
    _description = "Address"

    use = fields.Selection(string="Address Use", 
        selection=[
            ("home", "Home"), 
            ("work", "Work"), 
            ("temp", "Temp"), 
            ("old", "Old")], 
        help="The purpose of this address.")
    type = fields.Selection(string="Address Type", default="Both", 
        selection=[
            ("postal", "Postal"), 
            ("physical", "Physical"), 
            ("both", "Both")], 
        help="Distinguishes between physical addresses (those you can visit) and mailing addresses (e.g. PO Boxes and care-of addresses). Most addresses are both.")
    text = fields.Char(string="Full Address", help="A full text representation of the address.")
    line1 = fields.Char(string="Address Line 1", help="Street name, number, direction & P.O. Box etc.")
    line2 = fields.Char(string="Address Line 2", help="Street name, number, direction & P.O. Box etc.")
    line3 = fields.Char(string="Address Line 3", help="Street name, number, direction & P.O. Box etc.")
    city = fields.Char(string="City", help="The name of the city, town, village or other community or delivery center.")
    district = fields.Char(string="District", help="The name of the administrative area (e.g., county).")
    state = fields.Many2one(comodel_name="res.country.state", string="State", help="Sub-unit of country (abbreviations ok).")
    postal_code = fields.Char(string="Postal Code", help="Postal code for area.")
    country = fields.Many2one(comodel_name="res.country", string="Country", help="Country (can be ISO 3166 3-letter code).")
    start_date = fields.Datetime(string="Address Start_Date", help="Start of the time period when address was/is in use.")
    end_date = fields.Datetime(string="Address End_Date", help="End of the time period when address was/is in use.")

class Attachment(models.Model): 
    _name = "hc.attachment" 
    _description = "Attachment"
    _inherit = ["ir.attachment"]

    mimetype = fields.Many2one(comodel_name="hc.vs.attachment.mime.type", string="Content Type", help="MIMEtype of the content, with charset etc.")
    hash = fields.Binary(string="Hash", help="Hash of the data (sha-1, base64ed ).")

class AttachmentMimeType(models.Model): 
    _name = "hc.vs.attachment.mime.type"    
    _description = "MIME Type"
    _inherit = ["hc.value.set.contains"]

class HumanName(models.Model):

    _name = "hc.human.name"
    _description = "Human Name"

    use = fields.Selection(string="Human Name Use", 
        selection=[
            ("usual", "Usual"), 
            ("official", "Official"),
            ("temp", "Temp"),
            ("nickname", "Nickname"),
            ("anonymous", "Anonymous"),
            ("old", "Old"),
            ("maiden", "Maiden")],
        help="The use of a human name.")
    text = fields.Char(string="Full Human Name", help="A full text representation of the human name.")
#     family_name_ids = fields.Many2many(comodel_name="hc.vs.human.name.family", inverse_name="human_name_ids", 
#         string="Family Names", help="Family name (often called 'Surname').")
#     given_name_ids = fields.Many2many(comodel_name="hc.vs.human.name.given", inverse_name="human_name_ids", 
#         string="Given Names", help="Given names (not always 'first'). Includes middle names.")
#     prefix_name_ids = fields.Many2many(comodel_name="hc.vs.human.name.prefix", inverse_name="human_name_ids", 
#         string="Prefix Names", help="Parts that come before the name.")
#     suffix_name_ids = fields.Many2many(comodel_name="hc.vs.human.name.suffix", inverse_name="human_name_ids", 
#         string="Suffix Names", help="Parts that come after the name.")
    start_date = fields.Datetime(string="Human Name Start Date", help="Start of the time period when name was/is in use.")
    end_date = fields.Datetime(string="Human Name End Date", help="End of the time period when name was/is in use.")


class Identifier(models.Model):

    _name = "hc.identifier"
    _description = "Identifier"

    type_id = fields.Many2one(comodel_name="hc.vs.identifier.type", string="Type", help="Description of identifier.")
    system = fields.Char(string="System", help="The namespace for the identifier.")
#     assigner_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Identifier Assigner Organization", help="Organization that issued id (may be just text).")

class IdentifierType(models.Model): 
    _name = "hc.vs.identifier.type" 
    _description = "Identifier Type"
    _inherit = ["hc.value.set.contains"]

class Telecom(models.Model):    
    _name = "hc.telecom"    
    _description = "Telecom Contact Point"

    system = fields.Selection(string="Telecom System", 
        selection=[
            ("phone", "Phone"), 
            ("fax", "Fax"), 
            ("email", "Email"), 
            ("url", "Url")], 
        help="Telecommunications form for contact point - what communications system is required to make use of the contact.")
    value = fields.Char(string="Value", help="The actual telecom contact point details.")



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