from odoo import fields, models

class Cemetery(models.Model):
    _name = 'cemeteries.list.view'
    _description = 'Cemeteries List View'
   
    name = fields.Char(string='Name')
    location = fields.Char(string='Location')
    date = fields.Datetime(string='Date')

    grave_number = fields.Integer(string='Grave number')
    number_in_journals = fields.Integer(string='Number in Journals')
    cemetery_area = fields.Float(string='Cemetery Area')
    grave_photos = fields.Integer(string='Grave Photos')

    project_ids = fields.Many2one('project.project', string='Project')
