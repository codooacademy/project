from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)



# Todo: add a warning message group_project_task_dependencies



class ProjectUserStory(models.Model):
    _name = "project.user.story"
    _description = "project.user.story"

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('pending', 'Pending'),
            ('approved', 'Approved'),
            ('cancel', 'Cancelled'),
        ],
        default='draft',
        required=True,
    )
    priority = fields.Selection(
        selection=[
            ('must', 'Must Have'),
            ('should', 'Should Have'),
            ('could', 'Could Have'),
            ('wont', 'Wont Have'),
        ],
        default='must',
        required=True,
    )
    estimated_days = fields.Float()

    persona = fields.Char(required=True)
    wants_to = fields.Char(required=True)
    so_that = fields.Char(required=True)
    display_story = fields.Text(compute='_compute_display_story')

    epic_id = fields.Many2one('project.epic', required=True, ondelete='cascade')
    criteria_ids = fields.One2many('project.user.story.criteria', 'story_id')
    criteria_type_ids = fields.Many2many('project.user.story.criteria.type', compute='_compute_criteria_type_ids', string="Types")

    @api.depends('criteria_ids.type_id')
    def _compute_criteria_type_ids(self):
        for story in self:
            story.criteria_type_ids = story.criteria_ids.type_id

    @api.depends('persona', 'wants_to', 'so_that')
    def _compute_display_story(self):
        for story in self:
            story.display_story = _("As a %s, I want to %s so that %s", story.persona, story.wants_to, story.so_that)
