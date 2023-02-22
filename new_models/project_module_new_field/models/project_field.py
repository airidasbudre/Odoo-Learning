from odoo import models, fields



class ProjectField(models.Model):
    _inherit = 'project.project'

    name = fields.Char(string="random")
