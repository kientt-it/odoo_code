from pkg_resources import require

from odoo import fields, models, api

class StatusDetails(models.Model):
    _name = 'status.details'

    name = fields.Char(string="Name", required=True, unique=True)
    description = fields.Text(string="Description")
    applicant_ids = fields.One2many('hr.applicant', 'detailed_status_id', string="Applicant")

    @api.model
    def action_view_applicants(self):
        return {
            'name': 'Applicants',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'hr.applicant',
            'type': 'ir.actions.act_window',
            'domain': [('detailed_status_id', '=', self.id)],
            'target': 'current',
        }