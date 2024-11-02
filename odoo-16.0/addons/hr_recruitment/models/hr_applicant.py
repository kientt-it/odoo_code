from odoo import fields, models, api
from odoo.exceptions import ValidationError


class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    detailed_status_id = fields.Many2one('status.details', string='Detail Status Id')
    graduated_school = fields.Char(string='Graduated School')
    gpa_4_scale = fields.Float(string='GPA for 4.0')
    gpa_10_scale = fields.Float(string='GPA for 10.0')

    @api.constrains('gpa_10_scale')
    def _check_gpa_10_scale(self):
        for record in self:
            if record.gpa_10_scale < 0 or record.gpa_10_scale > 10:
                raise ValidationError("Value > 10")

            print(self.search)

    @api.onchange('gpa_10_scale')
    def _onchange_gpa_10_scale(self):
        for record in self:
            if record.gpa_10_scale:
                record.gpa_4_scale = (record.gpa_10_scale / 10) * 4
            else:
                record.gpa_4_scale = 0.0

    def action_accept(self):
        for record in self:
            record.interviewer_ids = [(4, self.env.user.id)]