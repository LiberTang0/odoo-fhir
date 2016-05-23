# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ValueSetContains(models.Model):

    _name = "hc.value.set.contains"
    _description = "Value Set Contains"
    _order = "code asc"

    system = fields.Char(string="Source URL", help="Web address of the source of the code.")
    is_abstract = fields.Boolean(string="Abstract", help="If user cannot select this entry.")
    version = fields.Char(string="Version", help="Version in which this code / display is defined.")
    code = fields.Char(string="Code", help="Code - if blank, this is not a choosable code.")
    name = fields.Char(string="Display", help="User display for the concept.")
    level = fields.Integer(string="Level", help="Level in a hierarchy of codes.")
    source = fields.Char(string="Source", help="The source of the definition of the code.")
    definition = fields.Text(string="Definition", help="An explanation of the meaning of the concept.")
    comments = fields.Text(string="Comments", help="Additional notes about how to use the code.")

class BasicAssociation(models.Model):   
    _name = "hc.basic.association"  
    _description = "Basic Association"
    
    is_active = fields.Boolean(string="Active", default=True, help="Whether this record is in active use.")      
    is_preferred = fields.Boolean(string="Preferred", help="Record preference indicator.")        
    start_date = fields.Datetime(string="Start Date", help="Start of the period during which this record is valid.")        
    end_date = fields.Datetime(string="End Date", help="End of the period during which this record is valid.")      

class Annotation(models.Model):

    _name = "hc.annotation"
    _description = "Annotation"

#     author_practitioner = fields.Many2one(comodel_name="hc.annotation.author.practitioner", string="Annotation Author Practitioner", 
#         help="Practitioner responsible for the annotation.")
    # author_patient = fields.Many2one(comodel_name="hc.annotation.author.patient", string="Annotation Author Patient", 
    #     help="Patient responsible for the annotation.")
    # author_related_person = fields.Many2one(comodel_name="hc.annotation.author.related.person", string="Annotation Author Related Person", 
    #     help="Related Person responsible for the annotation.")
    author = fields.Text(string="Author", help="Individual responsible for the annotation.")
    recorded_date = fields.Datetime(string="Recorded Date", help="When the annotation was made.")
    name = fields.Text(string="Annotation", help="The text content.")

class CountryPostalCodeType(models.Model):    
    _name = "hc.vs.country.postal.code.type"    
    _description = "Postal Code Type"       
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(string="Postal Code Type", help="Type of postal code (e.g., standard, PO Box).")
    country_id = fields.Many2one(comodel_name="res.country", string="Postal Code Country Owner", help="Country that maintains the postal code type.")

class CountryPostalCode(models.Model):  
    _name = "hc.vs.country.postal.code" 
    _description = "Postal Code"        
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(string="Postal Code", help="A group of numbers or letters and numbers that are added to a postal address to assist the sorting of mail.")
    postal_place = fields.Char(string="Place", help="A geographic point of interest associated with a postal code.")
    type_id = fields.Many2one(comodel_name="hc.vs.country.postal.code.type", string="Postal Code Type", help="Type of postal code (e.g., standard, PO Box).")
    is_decommissioned = fields.Boolean(string="Active", help="Indicates if the postal code is in active use.")
    latitude = fields.Float(string="Latitude", help="Average latitude for the postal code.")
    longitude = fields.Float(string="Latitude", help="Average longitude for the postal code.")
    postal_code_owner_country_id = fields.Many2one(comodel_name="res.country", string="Postal Code Country Owner", help="Country that maintains the postal code.")
    city_ids = fields.Many2many(comodel_name="hc.vs.country.city", string="Cities/Places", help="The name of the city, town, village or other community or delivery center.")
    district_id = fields.Many2one(comodel_name="hc.vs.country.district", string="District/County", help="The name of the administrative area (e.g., county).")
    state_id = fields.Many2one(comodel_name="res.country.state", string="State", help="Sub-unit of country (abreviations ok).")
    division_id = fields.Many2one(comodel_name="hc.vs.country.division", string="Division", help="Group of states (e.g., Pacific, Mountain).")
    region_id = fields.Many2one(comodel_name="hc.vs.country.region", string="Region", help="First level subdivision of a country (e.g. West, Midwest).")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", help="Country (can be ISO 3166 3 letter code).")

class CountryCityType(models.Model):    
    _name = "hc.vs.country.city.type"    
    _description = "City/Place Type"       
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(string="City/Place Type", help="Type of place or county subdivision (e.g., city, town).")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", help="Country that maintains the city/place type.")

class CountryCity(models.Model):    
    _name = "hc.vs.country.city"    
    _description = "City"       
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(string="City/Place", help="The name of the city, town, village or other community or delivery center.")
    type_id = fields.Many2one(comodel_name="hc.vs.country.city.type", string="Place Type", help="Type of place or county subdivision (e.g., city, town)")
    postal_code_ids = fields.Many2many(comodel_name="hc.vs.country.postal.code", string="Postal Codes", help="A group of numbers or letters and numbers that are added to a postal address to assist the sorting of mail.")
    primary_postal_code_city = fields.Boolean(string="Primary City", help="Indicates if this city is the primary city for a postal code.")
    district_ids = fields.Many2many(comodel_name="hc.vs.country.district", string="Districts/Counties", help="The name of the administrative area (e.g., county).")
    state_id = fields.Many2one(comodel_name="res.country.state", string="State", help="Sub-unit of country (abbreviations ok).")
    division_id = fields.Many2one(comodel_name="hc.vs.country.division", string="Division", help="Group of states (e.g., Pacific, Mountain).")
    region_id = fields.Many2one(comodel_name="hc.vs.country.region", string="Region", help="First level subdivision of a country (e.g. West, Midwest).")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", help="Country (can be ISO 3166 3 letter code).")

class CountryDistrict(models.Model):    
    _name = "hc.vs.country.district"    
    _description = "District"       
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(string="District/County", help="The name of the administrative area (e.g., county).")
    city_ids = fields.Many2many(comodel_name="hc.vs.country.city", string="Cities/Places", help="The name of the city, town, village or other community or delivery center.")
    state_id = fields.Many2one(comodel_name="res.country.state", string="State", help="Sub-unit of country (abreviations ok).")
    division_id = fields.Many2one(comodel_name="hc.vs.country.division", string="Division", help="Group of states (e.g., Pacific, Mountain).")
    region_id = fields.Many2one(comodel_name="hc.vs.country.region", string="Region", help="First level subdivision of a country (e.g. West, Midwest).")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", help="Country (can be ISO 3166 3 letter code).")

class CountryState(models.Model):    
    _name = "res.country.state"    
    _description = "Country State"       
    _inherit = ["res.country.state"]

    name = fields.Char(string="Name", help="Sub-unit of country (abreviations ok).")
    code = fields.Char(string="Code")
    division_id = fields.Many2one(comodel_name="hc.vs.country.division", string="Division", help="Group of states (e.g., Pacific, Mountain).")
    region_id = fields.Many2one(comodel_name="hc.vs.country.region", string="Region", help="First level subdivision of a country (e.g. West, Midwest).")

class CountryDivision(models.Model):  
    _name = "hc.vs.country.division"  
    _description = "Division"     
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(string="Division", help="User display for the concept.")
    region_id = fields.Many2one(comodel_name="hc.vs.country.region", string="Region", help="First level subdivision of a country (e.g. West, Midwest).")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", help="Country (can be ISO 3166 3 letter code).")

class CountryRegion(models.Model):  
    _name = "hc.vs.country.region"  
    _description = "Region"     
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(string="Region", help="First level subdivision of a country (e.g. West, Midwest).")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", help="Country (can be ISO 3166 3 letter code).")

class Address(models.Model):

    _name = "hc.address"
    _description = "Address"

    name = fields.Char(string="Full Address", help="A full text representation of the address.")
    line1 = fields.Char(string="Address Line 1", help="Street name, number, direction & P.O. Box etc.")
    line2 = fields.Char(string="Address Line 2", help="Street name, number, direction & P.O. Box etc.")
    line3 = fields.Char(string="Address Line 3", help="Street name, number, direction & P.O. Box etc.")
    city_id = fields.Many2one(comodel_name="hc.vs.country.city", string="City/Place", help="The name of the city, town, village or other community or delivery center.")
    district_id = fields.Many2one(comodel_name="hc.vs.country.district", string="District/County", help="The name of the administrative area (e.g., county).")
    state_id = fields.Many2one(comodel_name="res.country.state", string="State", help="Sub-unit of country (abreviations ok).")
    postal_code_id = fields.Many2one(comodel_name="hc.vs.country.postal.code", string="Postal Code", help="Postal code for area.")
    division_id = fields.Many2one(comodel_name="hc.vs.country.division", string="Division", help="Group of states (e.g., Pacific, Mountain).")
    region_id = fields.Many2one(comodel_name="hc.vs.country.region", string="Region", help="First level subdivision of a country (e.g. West, Midwest).")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", help="Country (can be ISO 3166 3 letter code).")

class Attachment(models.Model): 
    _name = "hc.attachment" 
    _description = "Attachment"
    _inherit = ["ir.attachment"]

    mimetype = fields.Many2one(comodel_name="hc.vs.mime.type", string="MIME Type", help="Mime type of the content, with charset etc.")
    language_id = fields.Many2one(comodel_name="res.lang", string="Language", help="Human language of the content (BCP-47).")
    hash = fields.Binary(string="Hash", help="Hash of the data (sha-1, base64ed ).")
    creation_date = fields.Datetime(string="Attachment Creation Date", help="Date attachment was first created.")

class AttachmentMimeType(models.Model): 
    _name = "hc.vs.mime.type"    
    _description = "MIME Type"
    _inherit = ["hc.value.set.contains"]

class SuffixHumanName(models.Model):    
    _name = "hc.vs.suffix.human.name"   
    _description = "Suffix Human Name"      
    _inherit = ["hc.value.set.contains"]     

class HumanNameTerm(models.Model):  
    _name = "hc.vs.human.name.term" 
    _description = "Human Name Term"        

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
    name = fields.Char(string="Full Name", help="A full text representation of the human name.")
    family_ids = fields.One2many(comodel_name="hc.human.name.family", inverse_name="human_name_id", string="Family Names", help="Family name (often called 'Surname').")
    given_ids = fields.One2many(comodel_name="hc.human.name.given", inverse_name="human_name_id", string="Given Names", help="Given names (not always 'first'). Includes middle names.")
    prefix_ids = fields.One2many(comodel_name="hc.human.name.prefix", inverse_name="human_name_id", string="Prefix Names", help="Parts that come before the name.")
    suffix_ids = fields.One2many(comodel_name="hc.human.name.suffix", inverse_name="human_name_id", string="Suffix Names", help="Parts that come after the name.")
    preferred_name = fields.Char(string="Preferred Name", help="How the person prefers to be named.")
    mother_maiden_family_name = fields.Char(string="Mother Maiden Family Name", help="Mother's original family name.")
    birth_family_name = fields.Char(string="Birth Family Name", help="Person's family name at birth.")
    is_last_before_first = fields.Boolean(string="Last Before First", help="Indicates that family name(s) are arranged before given name(s). Example: Chinese names.")
    is_maiden_after_last = fields.Boolean(string="Maiden After Last", help="Indicates that last name(s) are arranged before maiden name(s). Example: Spanish names.")

class HumanNameGiven(models.Model): 
    _name = "hc.human.name.given"   
    _description = "Human Name Given"

    human_name_id = fields.Many2one(comodel_name="hc.human.name", string="Human Name", help="Human name associated with this given name.")
    name_id = fields.Many2one(comodel_name="hc.vs.human.name.term", string="Name", help="Given name of this human name.")
    sequence = fields.Integer(string="Sequence", default="1", size=1, help="Display order of this given name.")
    type = fields.Selection(string="Type", selection=[("first", "First"), ("middle", "Middle"), ("initial", "Initial"), ("nickname", "Nickname")], help="Type of given name.")

class HumanNameFamily(models.Model):    
    _name = "hc.human.name.family"  
    _description = "Human Name Family"

    human_name_id = fields.Many2one(comodel_name="hc.human.name", string="Human Name", help="Human name associated with this family name.")
    name_id = fields.Many2one(comodel_name="hc.vs.human.name.term", string="Name", help="Family name of this human name.")
    sequence = fields.Integer(string="Sequence", default="1", size=1, help="Display order of this family name.")
    type = fields.Selection(string="Type", selection=[("surname", "Surname"), ("patronymic", "Patronymic"), ("previous (maiden)", "Previous (Maiden)"), ("mother", "Mother")], help="Type of family name.")

class HumanNamePrefix(models.Model):    
    _name = "hc.human.name.prefix"  
    _description = "Human Name Prefix"      

    human_name_id = fields.Many2one(comodel_name="hc.human.name", string="Human Name", help="Human name associated with this prefix name.")
    prefix_id = fields.Many2one(comodel_name="res.partner.title", string="Prefix", help="Prefix name of this human name.")

class HumanNameSuffix(models.Model):    
    _name = "hc.human.name.suffix"  
    _description = "Human Name Suffix"      

    human_name_id = fields.Many2one(comodel_name="hc.human.name", string="Human Name", help="Human name associated with this suffix name.")
    suffix_id = fields.Many2one(comodel_name="hc.vs.suffix.human.name", string="Suffix", help="Suffix name of this human name.")

class IdentifierType(models.Model): 
    _name = "hc.vs.identifier.type" 
    _description = "Identifier Type"
    _inherit = ["hc.value.set.contains"]

class Identifier(models.Model):

    _name = "hc.identifier"
    _description = "Identifier"

    type_id = fields.Many2one(comodel_name="hc.vs.identifier.type", string="Type", help="Description of identifier.")
    system_uri = fields.Char(string="Source URL", help="The namespace for the identifier.")
    name = fields.Char(string="Name", help="Name of this identifier.")
    code = fields.Char(string="Code", help="Code of this identifier.")
    definition = fields.Char(string="Definition", help="An explanation of the meaning of the identifier.")
    use = fields.Selection(string="Identifier Use", 
        selection=[
            ("usual", "Usual"), 
            ("official", "Official"), 
            ("temp", "Temporary"), 
            ("secondary", "Secondary")], 
        help="The purpose of this identifier.")
#     assigner_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Identifier Assigner Organization", help="Organization that issued id (may be just text).")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", help="Country associated with the identifier.")

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