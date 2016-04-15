from openerp import models, fields, api, _
from openerp.osv import osv
import time
from openerp.exceptions import Warning

class hc_country_city(models.Model):
    _name = 'hc.country.city'
    
    name = fields.Char('Name', size=50, required=True)
    code = fields.Char('Code', size=50, required=True)
    country_id = fields.Many2one('res.country', 'Country', required=True)
    state_id = fields.Many2one('res.country.state', 'State', required=True)
    postal_code_ids = fields.Many2many('hc.country.postal.code','hc_country_city_postal_code_rel', 'city_id', 'postal_code_id', string="Postal Codes")
    
    @api.onchange('state_id')
    def _onchnage_state_id(self):
        self.country_id = self.state_id.country_id.id
        
    
class hc_country_postal_code(models.Model):
    _name = 'hc.country.postal.code'
    
    code = fields.Char('Code', size=50, required=True)
    place = fields.Char('Place', size=50,)
    city_ids = fields.Many2many('hc.country.city', 'hc_country_city_postal_code_rel', 'postal_code_id', 'city_id', string='Cities')
    state_id = fields.Many2one('res.country.state', 'State',)
    country_id = fields.Many2one('res.country', 'Country',)

    _rec_name = 'code'

    @api.onchange('state_id')
    def _onchnage_state_id(self):
        self.country_id = self.state_id.country_id.id

class hc_address(models.Model):
    _name = 'hc.address'
    
    name = fields.Char('Name', size=50, required=True)
    street = fields.Char('Street', size=250)
    street2 = fields.Char('Street2', size=250)
    city_id = fields.Many2one('hc.country.city', 'City')
    state_id = fields.Many2one('res.country.state', 'State',)
    postal_code_id = fields.Many2one('hc.country.postal.code', 'Postal Code')
    country_id = fields.Many2one('res.country', 'Country',)

    @api.onchange('state_id')
    def _onchnage_state_id(self):
        self.country_id = self.state_id.country_id.id
    

class hc_patient_address(models.Model):
    _name = 'hc.patient.address'
    
    @api.one
    @api.depends('address_id.street', 'address_id.street2', 'address_id.city_id', 'address_id.postal_code_id', 'address_id.country_id')
    def _get_address_fields(self):
        self.street = self.address_id.street
        self.street2 = self.address_id.street2
        self.city_id = self.address_id.city_id.id
        self.postal_code_id = self.address_id.postal_code_id.id
        self.country_id = self.address_id.country_id.id

    
    address_id = fields.Many2one('hc.address', 'Address', required=True)
    use = fields.Selection([('home','Home'), ('work','Work'), ('temp','Temp'), ('old','Old')], 'Use', required=True)
    is_preferred = fields.Boolean('Is Preferred?')
    acive = fields.Boolean('Is Active?', default=True)
    patient_id = fields.Many2one('res.partner', 'Patient')
    start_date = fields.Date('Start Date', required=True, default=time.strftime('%Y-%m-%d') )
    end_date = fields.Date('End Date')
    
    ## function fields added only for view purpose
    street = fields.Char('Street', size=250, compute='_get_address_fields', track_visibility='always')
    street2 = fields.Char('Street2', size=250, compute='_get_address_fields', track_visibility='always')
    city_id = fields.Many2one('hc.country.city', 'City', compute='_get_address_fields', track_visibility='always')
    state_id = fields.Many2one('res.country.state', 'State', compute='_get_address_fields', track_visibility='always')
    postal_code_id = fields.Many2one('hc.country.postal.code', 'Postal Code', compute='_get_address_fields', track_visibility='always')
    country_id = fields.Many2one('res.country', 'Country', compute='_get_address_fields', track_visibility='always')
    
    _sql_constraints = [
        ('preferred_uniq', 'unique(use, is_preferred, patient_id)',
            'You can have only one preferred Address!!!'),
    ]     
    
    @api.one
    @api.constrains('start_date', 'end_date')
    def _check_end_date(self):
        if self.end_date and self.end_date < self.start_date:            
            raise Warning(_("End Date should be grater than Start Date"))
        
class hc_ethnicity(models.Model):
    _name = 'hc.ethnicity'
    
    parent_id = fields.Many2one('hc.ethnicity', 'Parent')
    code = fields.Char('Code', size=50, required=True)
    name = fields.Char('Name', size=50, required=True)
    country_id = fields.Many2one('res.country', 'Country',)
    
class hc_race(models.Model):
    _name = 'hc.race'
    
    parent_id = fields.Many2one('hc.race', 'Parent')
    code = fields.Char('Code', size=50, required=True)
    name = fields.Char('Name', size=50, required=True)
    country_id = fields.Many2one('res.country', 'Country',)
    
    

class hc_partner_type(models.Model):
    _name = 'hc.partner.type'
      
    code = fields.Char('Code', size=50, required=True)
    name = fields.Char('Name', size=50, required=True)

class res_partner(osv.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
     
    gender = fields.Selection([('male','Male'), ('female','Female'), ('undifferentiated','Undifferentiated'), ('unknown','Unknown')])
    birth_date = fields.Date('Birth Date')
    race_id = fields.Many2one('hc.race', 'Race')
    ethnicity_id = fields.Many2one('hc.ethnicity', 'Ethnicity')
    is_deceased = fields.Boolean('is Deceased?')
    deceased_date = fields.Date('Decease Date')
    address_ids = fields.One2many('hc.patient.address','patient_id', 'Addresses')
    is_multiple_birth = fields.Boolean('Is Multiple Birth')
    multiple_birth_count = fields.Integer('Multiple Birth Count')
    multiple_birth_order = fields.Integer('Multiple Birth Order')
    patient = fields.Boolean('Patient', help="Check this box if this contact is an Employee.")
    
## objects are created only for view purpose    
    
class hc_practitioner(osv.Model):
    _name = 'hc.practitioner'
    
    name = fields.Char('Name', size=50, required=True)

class hc_related_person(osv.Model):
    _name = 'hc.related.person'
    
    name = fields.Char('Name', size=50, required=True)

class hc_organization(osv.Model):
    _name = 'hc.organization'
    
    name = fields.Char('Name', size=50, required=True)

class hc_clinical(osv.Model):
    _name = 'hc.clinical'
    
    name = fields.Char('Name', size=50, required=True)

class hc_financial(osv.Model):
    _name = 'hc.financial'
    
    name = fields.Char('Name', size=50, required=True)

class hc_infrastructure(osv.Model):
    _name = 'hc.infrastructure'
    
    name = fields.Char('Name', size=50, required=True)
