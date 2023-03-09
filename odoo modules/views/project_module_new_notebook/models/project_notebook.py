from odoo import models, fields, api

class ProjectNotebook(models.Model):
    _inherit = 'project.project'

    cemetery_ids = fields.One2many('cemeteries.list.view', 'project_ids', string='Cemeteries')
