# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Delivery Costs',
    'version': '1.0',
    'category': 'Inventory/Delivery',
    'description': """
Allows you to add delivery methods in sale orders and picking.
==============================================================

You can define your own carrier for prices. When creating
invoices from picking, the system is able to add and compute the shipping line.
""",
    'depends': ['sale_stock', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'security/delivery_carrier_security.xml',
        'views/product_template_view.xml',
        'views/delivery_view.xml',
        'views/contact_views.xml',
        'views/delivery_portal_template.xml',
        'data/delivery_data.xml',
        'views/report_shipping.xml',
        'views/report_deliveryslip.xml',
        'views/report_package_barcode.xml',
        'views/res_config_settings_views.xml',
        'wizard/choose_delivery_package_views.xml',
        'wizard/choose_delivery_carrier_views.xml',
        'views/stock_package_type_views.xml',
        'views/stock_picking_type_views.xml',
        'views/stock_rule_views.xml',
        'views/stock_move_line_views.xml',
        'report/ir_actions_report_templates.xml',
    ],
    'demo': ['data/delivery_demo.xml'],
    'installable': True,
    'license': 'LGPL-3',
}