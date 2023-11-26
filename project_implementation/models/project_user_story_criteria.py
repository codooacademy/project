from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)


class ProjectUserStoryCriteria(models.Model):
    _name = "project.user.story.criteria"
    _description = "project.user.story.criteria"

    name = fields.Text(required=True)
    date = fields.Date(required=True, default=fields.Date.today)

    story_id = fields.Many2one('project.user.story', required=True, ondelete='cascade')
    task_id = fields.Many2one('project.task', ondelete='cascade')       # Todo: generate a task and link it here
    type_id = fields.Many2one(
        'project.user.story.criteria.type',
        required=True,
        default=lambda self: self.env.ref('project_implementation.criteria_type_standard', raise_if_not_found=False),
    )
    must_create_task = fields.Boolean(related='type_id.must_create_task')


