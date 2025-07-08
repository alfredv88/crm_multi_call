{
    'name': 'CRM Multi Call',
    'version': '18.0.1.0.0',
    'summary': 'Automatic multi-number calling and logging for CRM integrated with Issabel PBX (AMI)',
    'author': 'Tu Empresa',
    'category': 'CRM',
    'depends': ['crm', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_multi_call_views.xml',
        'views/crm_multi_call_lead_button.xml',
        'views/crm_multi_call_partner_button.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
} 