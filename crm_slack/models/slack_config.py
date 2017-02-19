# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleConfiguration(models.TransientModel):
    _inherit = 'sale.config.settings'

    module_crm_slack = fields.Boolean("Slack integration", help="Integration with slack, so that you"
                                      "can be warned on slack everytime you get a new lead on the CRM app")
    slack_api_key = fields.Char(string='Slack API Key')

    def set_slack_api_key(self):
        self.env['ir.config_parameter'].set_param(
            'slack_api_key', (self.slack_api_key or '').strip(), groups=['base.group_system'])

    def get_default_slack_api_key(self, fields):
        slack_api_key = self.env['ir.config_parameter'].get_param('slack.api_token', default='')
        return dict(slack_api_key=slack_api_key)