from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import ast
import logging
_logger = logging.getLogger(__name__)

class ProjectProject(models.Model):
    _inherit = "project.project"

    description = fields.Html(translate=True)

    is_youtube_project = fields.Boolean()
    youtube_account_id = fields.Many2one('social.account', domain="[('media_type', '=', 'youtube')]")



    # if is_youtube_project: add to youtube tasks stages (data + maybe a boolean field)


    @api.model
    def create(self, vals):
        res = super(ProjectProject, self).create(vals)
        res.add_to_youtube_task_type()
        return res


    def add_to_youtube_task_type(self):
        youtube_task_types = self.env['project.task.type'].search([('is_youtube_default', '=', True)])
        youtube_task_types.write({'project_ids': [(4, project.id) for project in self.filtered('is_youtube_project')]})


    def action_view_videos(self):
        """ Copy cat of action_view_tasks() """
        self.ensure_one()
        action = self.env['ir.actions.act_window'].with_context({'active_id': self.id})._for_xml_id('project_youtube.action_see_videos')
        action['display_name'] = _("%(name)s", name=self.name)
        context = action['context'].replace('active_id', str(self.id))
        context = ast.literal_eval(context)
        context.update({
            'create': self.active,
            'active_test': self.active
        })
        action['context'] = context
        return action

