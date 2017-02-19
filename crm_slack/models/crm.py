# -*- coding: utf-8 -*-
from openerp import fields, models, api, _
from slackclient import SlackClient
import threading


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.model
    def create(self, vals):
        res = super(CrmLead, self).create(vals)
        channel = self.env['ir.config_parameter'].\
            sudo().get_param('slack.sales_channel', "#general")
        # found at https://api.slack.com/web#authentication
        api_token = self.env['ir.config_parameter'].\
            sudo().get_param('slack.api_token')

        msg = vals.get('name', vals.get('contact_name', _('New Lead')))

        msg += " Email:%s" % vals.get('email_from', 'email not supplied')

        thcall = threading.Thread(target=self.send_slack_message, args=(api_token, channel, msg))
        thcall.start()

        return res

    def send_slack_message(self, token, channel, message):
        sc = SlackClient(token)
        sc.api_call("api.test")
        sc.api_call(
            "chat.postMessage", channel=channel, text=message,
            username='pybot', icon_emoji=':robot_face:'
        )
        return {}
