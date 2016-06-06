# -*- coding: utf-8 -*-

from openerp import models, fields, api

class AttachmentMimeType(models.Model): 
    _name = "hc.vs.mime.type"    
    _description = "MIME Type"
    _inherit = ["hc.value.set.contains"]

class Attachment(models.Model): 
    _name = "hc.attachment" 
    _description = "Attachment"
    _inherit = ["ir.attachment"]

    mimetype = fields.Many2one(
    	comodel_name="hc.vs.mime.type", 
    	string="MIME Type", 
    	help="Mime type of the content, with charset etc."
    	)
    language_id = fields.Many2one(
    	comodel_name="res.lang", 
    	string="Language", 
    	help="Human language of the content (BCP-47)."
    	)
    hash_attachment = fields.Binary(
    	string="Hash", 
    	help="Hash of the data (sha-1, base64ed )."
    	)
    creation_date = fields.Datetime(
    	string="Attachment Creation Date", 
    	help="Date attachment was first created."
    	)