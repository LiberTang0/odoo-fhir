# -*- coding: utf-8 -*-

from openerp import models, fields, api

class HumanNameTerm(models.Model):  
    _name = "hc.human.name.term" 
    _description = "Human Name Term"
    _inherit = ["res.partner.title"]         

    name = fields.Char( string="Human Name Term", help="Term part of a human name (e.g., John, Smith).")

    _sql_constraints = [
        ('name_unique',
        'UNIQUE(name)',
        "The term must be unique."),
        ]

class SuffixHumanName(models.Model):    
    _name = "hc.suffix.human.name"   
    _description = "Suffix Human Name"      
    _inherit = ["res.partner.title"]     

    name = fields.Char( string="Suffix Human Name Term", help="Suffix part of a human name. May be a family title (e.g., Jr.) or initials of a credential (e.g., RN).")

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
    name = fields.Char(string="Full Name", readonly=True, help="A full text representation of the human name.")
    # family_ids = fields.One2many(comodel_name="hc.human.name.family", inverse_name="human_name_id", string="Family Names", help="Family name (often called 'Surname').")
    # given_ids = fields.One2many(comodel_name="hc.human.name.given", inverse_name="human_name_id", string="Given Names", help="Given names (not always 'first'). Includes middle names.")
    prefix_ids = fields.Many2many(comodel_name="res.partner.title", string="Prefix Names", help="Parts that come before the name.")
    first_id = fields.Many2one(comodel_name="hc.human.name.term", string="First Name", help="Part of given name.")
    middle_ids = fields.Many2many(comodel_name="hc.human.name.term", relation="middle_name_human_term_rel", string="Middle Names", help="Part of given name.")
    initial_ids = fields.Many2many(comodel_name="hc.human.name.term", relation="initial_name_human_term_rel", string="Initial Names", help="Part of given name.")
    nickname_ids = fields.Many2many(comodel_name="hc.human.name.term", relation="nick_name_human_term_rel", string="Nickname", help="Part of given name.")
    surname_id = fields.Many2one(comodel_name="hc.human.name.term", string="Surname", help="Part of last name.")
    previous_last_id = fields.Many2one(comodel_name="hc.human.name.term", string="Previous Surname", help="Part of last name.")
    suffix_ids = fields.Many2many(comodel_name="hc.suffix.human.name", string="Suffix Names", help="Parts that come after the name.")
    preferred_name = fields.Char(string="Preferred Name", help="How the person prefers to be named.")
    mother_maiden_name_id = fields.Many2one(comodel_name="hc.human.name.term", string="Mother Maiden Name", help="Mother's family name at birth.")
    birth_last_name_id = fields.Many2one(comodel_name="hc.human.name.term", string="Birth Last Name", help="Person's family name at birth.")
    is_last_before_first = fields.Boolean(string="Last Before First", default=True, help="Indicates that family name(s) are arranged before given name(s). Example: Chinese names.")
    is_maiden_after_last = fields.Boolean(string="Maiden After Last", default=False, help="Indicates that last name(s) are arranged before maiden name(s). Example: Spanish names.")

class HcExtensionHumanName(models.Model):
    _inherit = 'hc.human.name'

    @api.model
    def create(self, vals):

        first = self.env['hc.human.name.term'].browse(vals['first_id']).name
        last = self.env['hc.human.name.term'].browse(vals['surname_id']).name
        maiden = self.env['hc.human.name.term'].browse(vals['mother_maiden_name_id']).name
        full = first+' '+last
        vals['name'] = full

        return super(HcExtensionHumanName, self).create(vals)

    @api.multi
    def write(self, vals):
       

        if 'first_id' in vals:   
            first = self.env['hc.human.name.term'].browse(vals['first_id']).name
        else:
            first = self.first_id.name

        if 'surname_id' in vals:    
            last = self.env['hc.human.name.term'].browse(vals['surname_id']).name
        else:
            last = self.surname_id.name

        full = first+' '+last
        vals['name'] = full

        return super(HcExtensionHumanName, self).create(vals)
