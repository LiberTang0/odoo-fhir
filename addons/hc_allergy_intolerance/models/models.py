# -*- coding: utf-8 -*-

from openerp import models, fields, api

class AllergyIntolerance(models.Model):

    _name = "hc.res.allergy.intolerance"
    _description = "Allergy Intolerance"

#    identifier_ids = fields.One2many(comodel_name="hc.allergy.intolerance.identifier", inverse_name="allergy_intolerance_id", 
#    	string="Identifiers", help="External IDs for the allergy.")
	recorded_date = fields.Datetime(string="Recorded Date", help="When recorded.")
#	recorder_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Recorder Practitioner", 
#		help="Practitioner who recorded the sensitivity.")
	recorder_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Recorder Patient", 
		help="Patient who recorded the sensitivity.")
#	patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Patient", required=True, 
		help="Patient who the sensitivity is for.")
	onset = fields.Datetime(string="Onset Date", help="Date(/time) when manifestations showed.")
#	reporter_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Reporter Patient", 
		help="Patient source of the information about the allergy.")
#	reporter_related_person_id = fields.Many2one(comodel_name="hc.res.related.person", string="Reporter Related Person", 
		help="Related Person source of the information about the allergy.")
#	reporter_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Reporter Practitioner", 
		help="Practitioner source of the information about the allergy.")
#	substance_id = fields.Many2one(comodel_name="hc.vs.allergy.intolerance.substance", 
#		string="Substance", required=True, help="Type of the substance and Negation codes for reporting no known allergies.")
	status = fields.Selection(string="Allergy Intolerance Status", 
		[("active", "Active"), ("unconfirmed", "Unconfirmed"), 
		("confirmed", "Confirmed"), 
		("inactive", "Inactive"), 
		("resolved", "Resolved"), 
		("refuted", "Refuted"), 
		("entered-in-error", "Entered in Error")], 
		help="Assertion about certainty associated with a propensity, or potential risk, of a reaction to the identified Substance.")
	criticality = fields.Selection(string="Allergy Intolerance Criticality", 
		[("low", "Low"), 
		("high", "High"), 
		("unable-to-assess", "Unable to Assess Risk")], 
		help="Estimate of the potential clinical harm, or seriousness, of a reaction to an identified Substance.")
	type = fields.Selection(string="Allergy Intolerance Type", 
		[("allergy", "Allergy"), 
		("intolerance", "Intolerance")], 
		help="Identification of the underlying physiological mechanism for a Reaction Risk.")
	category = fields.Selection(string="Allergy Intolerance Category", 
		[("food", "Food"), 
		("medication", "Medication"), 
		("environment", "Environment"), 
		("other", "Other")], 
		help="Category of an identified Substance.")
	last_occurence = fields.Datetime(string="Last Occurence Date", help="Date(/time) of last known occurence of a reaction.")
#	note_ids = fields.One2many(comodel_name="hc.allergy.intolerance.annotation", inverse_name="allergy_intolerance_id", string="Notes", 
#		help="Additional text not captured in other fields.")

class AllergyIntoleranceReaction(models.Model):

    _name = 'hc.allergy.intolerance.reaction'
    _description = "Allergy Intolerance Reaction"

	allergy_intolerance_id = fields.Many2one(comodel_name="hc.res.allergy.intolerance", string="Allergy Intolerance", 
		help="Allergy intolerance that is associated with this reaction.")
#	substance_id = fields.Many2one(comodel_name="hc.vs.allergy.intolerance.reaction.substance", string="Substance", help="Type of the substance.")
	certainty = fields.Selection(string="Reaction Certainty", [("unlikely", "Unlikely"), ("likely", "Likely"), ("confirmed", "Confirmed")], help="Statement about the degree of clinical certainty that a Specific Substance was the cause of the Manifestation in an reaction event.")
#	manifestation_ids = fields.One2many(comodel_name="hc.vs.allergy.intolerance.reaction.manifestation", inverse_name="allergy_intolerance_reaction_id", string="Manifestations", required=True, help="Clinical symptoms and/or signs that are observed or associated with an Adverse Reaction Event.")
	description = fields.Char(string="Description", help="Description of the event as a whole.")
	onset = fields.Datetime(string="Onset Date", help="Date(/time) when manifestations showed.")
	severity = fields.Selection(string="Reaction Severity", 
		[("mild", "Mild"), 
		("moderate", "Moderate"), 
		("severe", "Severe")], 
		help="Clinical assessment of the severity of a reaction event as a whole, potentially considering "\
		"multiple different manifestations.")
#	exposure_route_id = fields.Many2one(comodel_name="hc.vs.allergy.intolerance.reaction.exposure.route", string="Exposure Route", help="The route or physiological path of administration of a therapeutic agent into or onto the body of a subject.")
#	note_ids = fields.One2many(comodel_name="hc.allergy.intolerance.reaction.annotation", inverse_name="allergy_intolerance_reaction_id", string="Notes", 
#		help="Text about event not captured in other fields.")

#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
