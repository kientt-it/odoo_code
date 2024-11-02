from odoo import http
from odoo.http import request

class WebsiteOrderPayment(http.Controller):
    @http.route(['/payment/invoice/<int:invoice_id>'], type='http', auth="public", website=True)
    def payment_invoice(self, invoice_id, **kwargs):
        """Xử lý yêu cầu thanh toán cho hóa đơn"""
        invoice = request.env['account.move'].sudo().browse(invoice_id)
        if not invoice or invoice.state != 'posted':
            return request.not_found()

        # Kiểm tra nếu hóa đơn đã được thanh toán
        if invoice.amount_residual == 0:
            return request.render("website_order_payment.payment_already_paid", {})

        # Lấy URL thanh toán của cổng tích hợp
        payment_url = invoice.get_payment_url()

        return request.redirect(payment_url)

    @http.route(['/payment/status'], type='http', auth="public", website=True)
    def payment_status(self, **post):
        """Kiểm tra trạng thái thanh toán và cập nhật hóa đơn"""
        payment_status = post.get('status')
        invoice_id = post.get('invoice_id')
        invoice = request.env['account.move'].sudo().browse(int(invoice_id))

        if payment_status == 'success':
            invoice.payment_state = 'paid'
            return request.render("website_order_payment.payment_success", {})
        else:
            return request.render("website_order_payment.payment_failed", {})
