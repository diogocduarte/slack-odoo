# -*- coding: utf-8 -*-
{
    'name': 'Slack CRM integration',
    'version': '1.0',
    'author': 'OdooGAP',
    'summary': 'Slack CRM integration',
    'description': """
Slack CRM integration
=====================
Get Notification when u have a new lead

    """,
    'website': 'http://www.odoogap.com',
    'depends': ['crm'],
    'category': 'Communication',
    'data': [
        'data/slack_data.xml',
        'views/res_config_views.xml'
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
