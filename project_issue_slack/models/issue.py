# -*- coding: utf-8 -*- 
from odoo import models, fields, api 
from odoo import exceptions
import requests
import json

class Project(models.Model):
    _inherit = ['project.project']
    slack_channel = fields.Char("SlackWebHook")


class Issue(models.Model):
    _inherit = ['project.issue']

    @api.multi
    def write(self, vals):
        res = super(Issue, self).write(vals)

        if "project_id" in self  and 'issue_stage_id' in vals:
            self.ensure_one()
            webhook = self.env['ir.config_parameter'].sudo().get_param('slack.webhook')
            channel = self.project_id.slack_channel
            project_name = self.project_id.name
            issue_id = self.id
            issue_name = self.name
            d = [   
                    ('id','=',vals.get("issue_stage_id")),
                ]
            r = self.env["project.issue.stage"].search(d, limit=1)
            state_name = r.name
            assigned = self.user_id.name
            link = "https://odoo.interalia.net/web?#id={}&view_type=form&model=project.issue".format(issue_id)
            data = {'payload':json.dumps({
                'username': 'Odoo Interalia',
                'icon_url': 'https://i.imgur.com/oujlb7V.png',
                'channel': channel,
                'attachments':[
                    {
		     "fallback": u"{} {} {}".format(project_name, assigned, state_name),
                     "pretext": u"Project: *{}*".format(project_name),
                        "author_name": issue_name,
                        "title": "Issue: {} ".format(issue_id),
                        "title_link":link,
                        'fields':[{
                            'title': 'Stage',
                            'value': state_name,
                            },{
                                'title': 'Assigned to',
                                'value': assigned
                            }
                        ]
                    },
                ]
            })}
            requests.post(webhook, data)
        return res
        
