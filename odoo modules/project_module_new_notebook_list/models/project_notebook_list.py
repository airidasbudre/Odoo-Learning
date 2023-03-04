from odoo import fields, models

class Cemetery(models.Model):
    _name = 'cemeteries.list.view'
    _description = 'Cemeteries List View'

    name = fields.Char(string='Name', required=True)
    # project_id = fields.Many2one(
    #     comodel_name='project.project',
    #     string='Project',
    # )
    cemeteries = fields.Char(string='Cemeteries')
    name = fields.Char(string='Name')
    location = fields.Char(string='Location')
    date = fields.Char(string='Date')

    # favorite_user_ids = fields.Many2many(
    #     comodel_name='res.users',
    #     relation='project_cemeteries_list_view_favorite_users_rel',
    #     column1='cemeteries_id',
    #     column2='user_id',
    #     string='Favorite Users',
    # )

# class ProjectProfile(models.Model):
#     _inherit = 'project.project'

#     cemetery_ids = fields.One2many(
#         comodel_name='project.cemeteries.list.view',
#         inverse_name='project_id',
#         string='Cemeteries',
#     )