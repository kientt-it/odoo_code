from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_create_invoice_and_pay(self):
        """ Tạo hóa đơn từ đơn hàng và mở trang thanh toán """
        # Tạo hóa đơn
        invoice = self._create_invoices()
        if invoice:
            invoice.action_post()
            # Redirect tới trang thanh toán trên website với thông tin hóa đơn
            return {
                'type': 'ir.actions.act_url',
                'url': f'/payment/invoice/{invoice.id}',
                'target': 'self',
            }
