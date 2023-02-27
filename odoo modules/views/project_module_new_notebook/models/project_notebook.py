from odoo import models, fields, api

class ProjectCemeteries(models.Model):
    _inherit = 'project.project'

    cemetery = fields.Char(string='Cemeteries')

    # @api.onchange('cemetery_ids')
    # def _onchange_cemetery_ids(self):
    #     for cemetery in self.cemetery_ids:
    #         if cemetery not in self.partner_ids:
    #             self.partner_ids += cemetery
