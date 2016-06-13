# -*- coding: utf-8 -*-

from openerp import models, fields, api

class IdentifierType(models.Model): 
    _name = "hc.vs.identifier.type" 
    _description = "Identifier Type"
    _inherit = ["hc.value.set.contains"]

    name = fields.Char( string="Identifier Type", help="Description of identifier.")

class Identifier(models.Model):

    _name = "hc.identifier"
    _description = "Identifier"

    name = fields.Char(string="Name", help="Name of this identifier.")
    code = fields.Char(string="Code", help="Code of this identifier.")
    type_id = fields.Many2one(comodel_name="hc.vs.identifier.type", string="Type", help="Description of identifier.")
    # use = fields.Selection(
    #     string="Identifier Use", 
    #     selection=[
    #         ("usual", "Usual"), 
    #         ("official", "Official"), 
    #         ("temp", "Temporary"), 
    #         ("secondary", "Secondary")
    #         ], 
    #     help="The purpose of this identifier.")
    definition = fields.Char(string="Definition", help="An explanation of the meaning of the identifier.")
    system_uri = fields.Char(string="Source URL", help="The namespace for the identifier.")
#     assigner_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Identifier Assigner Organization", help="Organization that issued id (may be just text).")
    country_id = fields.Many2one(
        comodel_name="res.country", 
        string="Country", 
        help="Country associated with the identifier."
        )

class IdentifierType(models.Model): 
    _name = "hc.vs.identifier.type" 
    _description = "Identifier Type"
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(string="Identifier Type", help="Description of identifier.")

class Identifier(models.Model):

    _name = "hc.identifier"
    _description = "Identifier"

    type_id = fields.Many2one(comodel_name="hc.vs.identifier.type", string="Type", help="Description of identifier.")
    system_uri = fields.Char(string="Source URL", help="The namespace for the identifier.")
    name = fields.Char(string="Name", help="Name of this identifier.")
    code = fields.Char(string="Code", help="Code of this identifier.")
    definition = fields.Char(string="Definition", help="An explanation of the meaning of the identifier.")
    use = fields.Selection(
        string="Identifier Use", 
        selection=[
            ("usual", "Usual"), 
            ("official", "Official"), 
            ("temp", "Temporary"), 
            ("secondary", "Secondary")
            ], 
        help="The purpose of this identifier.")
#     assigner_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Identifier Assigner Organization", help="Organization that issued id (may be just text).")
    country_id = fields.Many2one(
        comodel_name="res.country", 
        string="Country", 
        help="Country associated with the identifier."
        )

