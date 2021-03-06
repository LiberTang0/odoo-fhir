# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Annotation(models.Model):

    _name = "hc.annotation"
    _description = "Annotation"

    name = fields.Text(
    	string="Annotation", 
    	help="The text content."
    	)
    recorded_date = fields.Datetime(string="Recorded Date", help="When the annotation was made.")
    author_type = fields.Selection(
    	string="Author Type", 
        selection=[
            ("person", "Person"), 
            ("practitioner", "Practitioner"),
            ("patient", "Patient"),
            ("related person", "Related Person")],
        help="The use of a human name."
        )
    # author_id = fields.Many2one(
    # 	comodel_name="hc.res.person", 
    # 	string="Author", 
    # 	help="Individual responsible for the annotation."
    # 	)
#     author_practitioner = fields.Many2one(comodel_name="hc.annotation.author.practitioner", string="Author Practitioner", 
#         help="Practitioner responsible for the annotation.")
    # author_patient = fields.Many2one(comodel_name="hc.annotation.author.patient", string="Author Patient", 
    #     help="Patient responsible for the annotation.")
    # author_related_person = fields.Many2one(comodel_name="hc.annotation.author.related.person", string="Author Related Person", 
    #     help="Related Person responsible for the annotation.")
    
    
    
