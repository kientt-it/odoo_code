{
    'name': 'Website Order Payment',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Enable online payment for orders on website',
    'depends': ['website', 'sale', 'account', 'payment'],
    'data': [
        'views/website_payment_template.xml',
        'views/payment_inherited_view.xml',
    ],
    'installable': True,
    'application': False,
}
