from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)

STATUS_COLOR = {
    'in_progress': 24,  # purple
    'new': 21,          # light blue
    'done': 20,         # green / success
    'cancelled': 0,     # grey
    False: 0,     # grey
}


class ProjectEpic(models.Model):
    _name = "project.epic"
    _description = "project.epic"
    _inherit = ['mail.thread.cc', 'mail.activity.mixin']

    name = fields.Char(required=True)
    description = fields.Html(help="Detailed description of the epic (for who? what? why?)")
    active = fields.Boolean(default=True)
    category_id = fields.Many2one('project.epic.category', string="Category")
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('in_progress', 'In Progress'),
            ('done', 'Done'),
            ('cancelled', 'Cancelled')
        ],
        default='new',
        required=True,
        tracking=True,
    )
    date_deadline = fields.Date(string="Deadline")

    color = fields.Integer(compute='_compute_color')
    progress = fields.Integer(compute='_compute_progress')
    progress_percentage = fields.Float(compute='_compute_progress')

    project_id = fields.Many2one('project.project', required=True, ondelete='cascade')
    milestone_id = fields.Many2one('project.milestone', string="Milestone", domain="[('project_id', '=', project_id)]")
    story_ids = fields.One2many('project.user.story', 'epic_id', string="Stories")



    @api.depends('state')
    def _compute_color(self):
        for update in self:
            update.color = STATUS_COLOR[update.state]

    @api.depends('progress_percentage')
    def _compute_progress(self):
        for epic in self:
            epic.progress_percentage = 0.3
            epic.progress = round(epic.progress_percentage, 2) * 100

