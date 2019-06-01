# -*- coding: utf-8 -*-
{
    'name': 'Slack Projet Issue integration',
    'version': '1.0',
    'author': 'zodman',
    'summary': 'Slack Project Issue Integration',
    'description': """
Get Notification when u have a new issue

    """,
    'website': 'http://opensrc.mx',
    'depends': ['project_issue'],
    'category': 'Communication',
    'data': [
        'views.xml',
        'slack_data.xml',
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
