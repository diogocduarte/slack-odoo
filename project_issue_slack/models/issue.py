# -*- coding: utf-8 -*- 
from odoo import models, fields, api 
from odoo import exceptions
import requests
import simplejson as json

class Project(models.Model):
    _inherit = ['project.project']
    slack_webhook = fields.Char("SlackWebHook")


class Issue(models.Model):
    _inherit = ['project.issue']

    @api.multi
    def write(self, vals):
        import q
        res = super(Issue, self).write(vals)

        if 'issue_stage_id' in vals:
            self.ensure_one()
            webhook = self.project_id.slack_webhook
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
                'attachments':[
                    {
                     "pretext": u"Odoo: {}".format(project_name),
                        "author_name": issue_name,
                        "title": "Issue: {} ".format(issue_id),
                        "title_link":link,
                        'fields':[{
                            'title': 'Stage',
                            'value': state_name,
                            },{
                                'title': 'Asigned',
                                'value': assigned
                            }
                        ]
                    },
                ]
            })}
            requests.post(webhook, data)
        return res
        
