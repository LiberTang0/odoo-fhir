# -*- coding: utf-8 -*-

from openerp import models, fields, api

class CountryRegionType(models.Model):    
    _name = "hc.vs.country.region.type"    
    _description = "Region Type"       
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
    	string="Region Type", 
    	help="Type of grouping of divisions (e.g. Region in the US)."
    	)
    country_id = fields.Many2one(
    	comodel_name="res.country", 
    	string="Country", 
    	help="Country that maintains the region type."
    	)

class CountryRegion(models.Model):  
    _name = "hc.vs.country.region"  
    _description = "Region"     
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(string="Region", help="A grouping of divisions (e.g. West and Midwest in the US).")
    type_id = fields.Many2one(comodel_name="hc.vs.country.region.type", string="Region Type", help="Type of grouping of regions (e.g. Region in the US).")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", help="Country (can be ISO-3166 3-letter code).")

class CountryDivisionType(models.Model):    
    _name = "hc.vs.country.division.type"    
    _description = "Division Type"       
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(string="Division Type", help="Type of grouping of principal subdivisions (e.g., Division in the US).")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", help="Country that maintains the division type.")

class CountryDivision(models.Model):  
    _name = "hc.vs.country.division"  
    _description = "Division"     
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(string="Division", help="A grouping of principal subdivisions (e.g., England in the UK, West in the US).")
    type_id = fields.Many2one(comodel_name="hc.vs.country.division.type", string="Division Type", help="Type of grouping of principal subdivisions (e.g., Division in the US).")
    region_id = fields.Many2one(comodel_name="hc.vs.country.region", string="Region", help="A grouping of divisions or states (e.g. West, Midwest).")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", help="Country (can be ISO-3166 3-letter code).")

class CountryStateType(models.Model):    
    _name = "hc.vs.country.state.type"    
    _description = "State Type"       
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(string="State Type", help="Type of principal subdivision of a country (e.g., state, province, two-tier county).")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", help="Country that maintains the city/place type.")
    source = fields.Char(default="ISO 3166-2")

class CountryState(models.Model):    
    _name = "res.country.state"    
    _description = "Country State"       
    _inherit = ["res.country.state"]

    name = fields.Char(string="Name", help="Sub-unit (i.e., primary subdivision) of a country (abreviations ok).")
    code = fields.Char(string="Code", help="The suffix of the ISO 3166-2 code that uniquely identifies a principal subdivision (e.g., states or provinces) within a country.")
    numeric_code = fields.Char(string="Numeric Code", help="Numeric code that uniquely identifies a principal subdivision (e.g., state or province) within a country.")
    type_id = fields.Many2one(comodel_name="hc.vs.country.state.type", string="State Type", help="Type of principal subdivision of a country (e.g., state, province).")
    division_id = fields.Many2one(comodel_name="hc.vs.country.division", string="Division", help="Group of primary subdivisions (e.g., Pacific and Mountain in the US).")
    region_id = fields.Many2one(comodel_name="hc.vs.country.region", string="Region", help="A grouping of divisions or states (e.g. West, Midwest).")
    source = fields.Char(string="Source", help="The source of the definition of the code.")
    system = fields.Char(string="Source URL", help="Web address of the source of the code.")

class CountryDistrictType(models.Model):    
    _name = "hc.vs.country.district.type"    
    _description = "District Type"       
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(string="District/County Type", help="Type of administrative area (e.g., In US, county).")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", help="Country that maintains the district type.")

class CountryDistrict(models.Model):    
    _name = "hc.vs.country.district"    
    _description = "District"       
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(string="District/County", help="Top-level administrative area of a principal subdivision (e.g., County in US State).")
    type_id = fields.Many2one(comodel_name="hc.vs.country.district.type", string="District Type", help="Type of administrative area (e.g., In US, county or parish).")
    city_ids = fields.Many2many(comodel_name="hc.vs.country.city", string="Cities/Places", help="The name of the city, town, village or other community or delivery center.")
    state_id = fields.Many2one(comodel_name="res.country.state", string="State", help="Sub-unit (i.e., primary subdivision) of a country (abreviations ok).")
    division_id = fields.Many2one(comodel_name="hc.vs.country.division", string="Division", help="Group of primary subdivisions (e.g., Pacific and Mountain in the US).")
    region_id = fields.Many2one(comodel_name="hc.vs.country.region", string="Region", help="A grouping of divisions or states (e.g. West, Midwest).")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", help="Country (can be ISO-3166 3-letter code).")

class CountryCityType(models.Model):    
    _name = "hc.vs.country.city.type"    
    _description = "City/Place Type"       
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(string="City/Place Type", help="Type of place or district/county subdivision (e.g., city, town).")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", help="Country that maintains the city/place type.")

class CountryCityCategory(models.Model):    
    _name = "hc.vs.country.city.category"    
    _description = "City/Place Category"       
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(string="City/Place Category", help="Category of place or district/county subdivision (e.g., census designated place, incorporated place).")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", help="Country that maintains the city/place category.")

class CountryCityStatus(models.Model):    
    _name = "hc.vs.country.city.status"    
    _description = "City/Place Functional Status"       
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(string="City/Place Functional Status", help="Status of a place from a legal and/or statistical perspective.")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", help="Country that maintains the city/place functional status.")

class CountryCity(models.Model):    
    _name = "hc.vs.country.city"    
    _description = "City/Place"       
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(string="City/Place", help="The name of the city, town, village or other community or delivery center.")
    numeric_code = fields.Char(string="Numeric Code", help="Numeric code that uniquely identifies a place within a primary subdivision (e.g. In US, 5-digit FIPS Place Code).")
    type_id = fields.Many2one(comodel_name="hc.vs.country.city.type", string="Place Type", help="Type of place or county subdivision (e.g., city, town).")
    category_id = fields.Many2one(comodel_name="hc.vs.country.city.category", string="Place Category", help="Category of place or district/county subdivision (e.g., census designated place, incorporated place).")
    status_id = fields.Many2one(comodel_name="hc.vs.country.city.status", string="Functional Status", help="Status of a place from a legal and/or statistical perspective.")
    postal_code_ids = fields.Many2many(comodel_name="hc.vs.country.postal.code", string="Postal Codes", help="A group of numbers or letters and numbers that are added to a postal address to assist the sorting of mail.")
    primary_postal_code_city = fields.Boolean(string="Primary City", help="Indicates if this city is the primary city for a postal code.")
    district_ids = fields.Many2many(comodel_name="hc.vs.country.district", string="Districts/Counties", help="The name of the administrative area (e.g., county).")
    state_id = fields.Many2one(comodel_name="res.country.state", string="State", help="Sub-unit of country (abbreviations ok).")
    division_id = fields.Many2one(comodel_name="hc.vs.country.division", string="Division", help="Group of primary subdivisions (e.g., Pacific and Mountain in the US).")
    region_id = fields.Many2one(comodel_name="hc.vs.country.region", string="Region", help="First level subdivision of a country (e.g. West, Midwest).")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", help="Country (can be ISO-3166 3-letter code).")

class HcExtensionCity(models.Model):
    _inherit = 'hc.vs.country.city'

    state_id = fields.Many2one(comodel_name="res.country.state", string="State", help="Sub-unit of country (abbreviations ok).")
    division_id = fields.Many2one(related='state_id.division_id', string="Division", help="Group of primary subdivisions (e.g., Pacific and Mountain in the US).")
    region_id = fields.Many2one(related='state_id.region_id', string="Region", help="A grouping of divisions or states (e.g. West, Midwest).")
    country_id = fields.Many2one(related='state_id.country_id', string="Country", help="Country (can be ISO-3166 3-letter code).")

class CountryPostalCodeType(models.Model):    
    _name = "hc.vs.country.postal.code.type"    
    _description = "Postal/ZIP Code Type"       
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(string="Postal/ZIP Code Type", help="Type of postal code (e.g., standard, PO Box).")
    country_id = fields.Many2one(comodel_name="res.country", string="Postal Code Country Owner", help="Country that maintains the postal code type.")

class CountryPostalCode(models.Model):  
    _name = "hc.vs.country.postal.code" 
    _description = "Postal Code"        
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(string="Postal/ZIP Code", help="A group of numbers or letters and numbers that are added to a postal address to assist the sorting of mail.")
    postal_place = fields.Char(string="Place", help="A geographic point of interest associated with a postal code.")
    type_id = fields.Many2one(comodel_name="hc.vs.country.postal.code.type", string="Postal Code Type", help="Type of postal code (e.g., standard, PO Box).")
    is_decommissioned = fields.Boolean(string="Decommission", help="Indicates if the postal code is not in active use.")
    latitude = fields.Float(string="Latitude", help="Average geographic latitude of the postal code.")
    longitude = fields.Float(string="Longitude", help="Average geographic longitude of the postal code.")
    postal_code_owner_country_id = fields.Many2one(comodel_name="res.country", string="Postal Code Country Owner", help="Country that maintains the postal code.")
    city_ids = fields.Many2many(comodel_name="hc.vs.country.city", string="Cities/Places", help="The name of the city, town, village or other community or delivery center.")
    district_ids = fields.Many2many(comodel_name="hc.vs.country.district", string="Districts/Counties", help="The name of the administrative area (e.g., county).")
    state_ids = fields.Many2many(comodel_name="res.country.state", string="State", help="Sub-unit (i.e., primary subdivision) of a country (abreviations ok).")
    division_id = fields.Many2one(comodel_name="hc.vs.country.division", string="Division", help="Group of primary subdivisions (e.g., Pacific and Mountain in the US).")
    region_id = fields.Many2one(comodel_name="hc.vs.country.region", string="Region", help="A grouping of divisions or states (e.g. West, Midwest).")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", help="Country (can be ISO-3166 3-letter code).")

class HcExtensionPostalCode(models.Model):
    _inherit = 'hc.vs.country.postal.code'

    division_id = fields.Many2one(comodel_name="hc.vs.country.division", string="Division", help="Group of primary subdivisions (e.g., Pacific and Mountain in the US).")
    region_id = fields.Many2one(related='division_id.region_id', string="Region", help="A grouping of divisions or states (e.g. West, Midwest).")
    country_id = fields.Many2one(related='division_id.country_id', string="Country", help="Country (can be ISO-3166 3-letter code).")

class Address(models.Model):
    _name = "hc.address"
    _description = "Address"

    name = fields.Char(string="Full Address", help="A full text representation of the address.")
    line1 = fields.Char(string="Address Line 1", help="Street name, number, direction & P.O. Box etc.")
    line2 = fields.Char(string="Address Line 2", help="Street name, number, direction & P.O. Box etc.")
    line3 = fields.Char(string="Address Line 3", help="Street name, number, direction & P.O. Box etc.")
    city_id = fields.Many2one(comodel_name="hc.vs.country.city", string="City/Place", help="The name of the city, town, village or other community or delivery center.")
    district_id = fields.Many2one(comodel_name="hc.vs.country.district", string="District/County", help="The name of the administrative area (e.g., county).")
    state_id = fields.Many2one(comodel_name="res.country.state", string="State/Province", help="Sub-unit (i.e., primary subdivision) of a country (abreviations ok).")
    postal_code_id = fields.Many2one(comodel_name="hc.vs.country.postal.code", string="Postal/ZIP Code", help="Postal code for area.")
    division_id = fields.Many2one(comodel_name="hc.vs.country.division", string="Division", help="Group of primary subdivisions (e.g., Pacific and Mountain in the US).")
    region_id = fields.Many2one(comodel_name="hc.vs.country.region", string="Region", help="A grouping of divisions or states (e.g. West, Midwest).")
    country_id = fields.Many2one(comodel_name="res.country", string="Country", help="Country (can be ISO-3166 3-letter code).")


class HcExtensionAddress(models.Model):
    _inherit = 'hc.address'

    postal_code_id = fields.Many2one(comodel_name="hc.vs.country.postal.code", string="Postal/ZIP Code", help="Postal code for area.")
    
    division_id = fields.Many2one(related='postal_code_id.division_id', string="Division", help="Group of primary subdivisions (e.g., Pacific and Mountain in the US).")
    region_id = fields.Many2one(related='postal_code_id.region_id', string="Region", help="A grouping of divisions or states (e.g. West, Midwest).")
    country_id = fields.Many2one(related='postal_code_id.country_id', string="Country", help="Country (can be ISO-3166 3-letter code).")

    @api.model
    def create(self, vals):

        lines = vals['line1']+', '+vals['line2']+', '+vals['line3']+', '
        city = self.env['hc.vs.country.city'].browse(vals['city_id']).name
        state = self.env['res.country.state'].browse(vals['state_id']).name
        postal = self.env['hc.vs.country.postal.code'].browse(vals['postal_code_id']).name
        district = self.env['hc.vs.country.district'].browse(vals['district_id']).name
        division = self.env['hc.vs.country.division'].browse(vals['division_id']).name
        region = self.env['hc.vs.country.region'].browse(vals['region_id']).name
        country = self.env['res.country'].browse(vals['country_id']).name
        address = lines+city+', '+state+', '+postal+', '+country
        vals['name'] = address

        return super(HcExtensionAddress, self).create(vals)

    @api.multi
    def write(self, vals):
        #I think this code can be improved but time is constraint so...
        if 'line1' in vals:
            line1 = vals['line1']
        else:
            line1 = self.line1

        if 'line2' in vals:
            line2 = vals['line2']
        else: 
            line2 = self.line2

        if 'line3' in vals:
            line3 = vals['line3']
        else:
            line3 = self.line3

        if 'city_id' in vals:   
            city = self.env['hc.vs.country.postal.city'].browse(vals['city_id']).name
        else:
            city = self.city_id.name

        if 'postal_code_id' in vals:    
            postal = self.env['hc.vs.country.postal.code'].browse(vals['postal_code_id']).name
        else:
            postal = self.city_id.name

        if 'state_id' in vals:  
            state = self.env['res.country.state'].browse(vals['state_id']).name
        else:
            state = self.state_id.name

        if 'district_id' in vals:
            district = self.env['hc.vs.country.district'].browse(vals['district_id']).name
        else:
            district = self.district_id.name

        if 'division_id' in vals:
            division = self.env['hc.vs.country.division'].browse(vals['division_id']).name
        else:
            division = self.division_id.name

        if 'region_id' in vals:
            region = self.env['hc.vs.country.region'].browse(vals['region_id']).name
        else:
            region = self.region_id.name

        if 'country_id' in vals:
            country = self.env['res.country'].browse(vals['country_id']).name
        else:
            country = self.country_id.name

        address = lines+city+', '+state+', '+postal+', '+country
        vals['name'] = address

        return super(HcExtensionAddress, self).write(vals)
