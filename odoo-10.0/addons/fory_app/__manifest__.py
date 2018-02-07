# -*- coding: utf-8 -*-
{
    'name': 'Fory App',
    'version': '1.0',
    'category': 'fory_app',
    'description': """A module to verify the inheritance using _inherits.""",
    'author': 'Spro Group',
    'website': 'http://sprogroup.com',
    'depends': [
        'crm',
        'purchase',
        'stock',
    ],
    'data': [
        'views/fory_app_templates.xml',
        'views/account_view.xml',
        'views/account_payment_views.xml',
        'views/account_journalitembalance.xml',
        'views/report_trialbalance.xml',
        'views/purchase_views.xml',
        'views/sale_views.xml',
        'views/account_invoice_view.xml',
        'views/res_partner_view.xml',
        'views/product_template_view.xml',
        'views/purchase_requisition_views.xml',
        'views/product_views.xml',
        'views/stock_inventory.xml',
        'views/account_voucher_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
