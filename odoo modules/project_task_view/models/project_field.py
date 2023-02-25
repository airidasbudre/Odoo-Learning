from odoo import models, fields


class ProjectTask(models.Model):
    _inherit = 'project.task'

    # Define the writable fields for the calendar view
    CALENDAR_WRITABLE_FIELDS = {
        'name',
        'partner_id',
        'partner_email',
        'date_deadline',
        'tag_ids',
        'sequence',
        'priority',
    }

    # Add the partner_email field to the model
    partner_email = fields.Char(related='partner_id.email', string="Partner Email", readonly=True)
