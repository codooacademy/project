from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from markupsafe import Markup
import logging
_logger = logging.getLogger(__name__)

class ProjectTask(models.Model):
    _inherit = "project.task"

    date_deadline = fields.Datetime()
    name = fields.Char(translate=True)
    description = fields.Html(translate=True)


    is_youtube_task = fields.Boolean(related="project_id.is_youtube_project")
    is_ready_next_stage = fields.Boolean(compute="_compute_is_ready_next_stage")
    next_stage_id = fields.Many2one('project.task.type', compute="_compute_next_stage_id")
    active_language_id = fields.Many2one('res.lang', default=lambda self: self.env['res.lang'].search([('code', '=', self.env.user.lang)], limit=1))
    translated_name = fields.Char(compute="_compute_translated_name")
    full_description = fields.Html(compute="_compute_full_description", translate=True)

    # kanban_state > Change to done when all subtasks are done


    # Create task.type for a youtube video, and add a project to them (project_ids) if it's a youtube project
    #       -> Add also tasks to a stage, that will be automatically created when moving to that stage

    # Use subtasks to create templates of video creation. Example: Script > 3 tasks: 1. Write a plan, 2. Write a script, 3. Write translations


    @api.depends('child_ids.kanban_state')
    def _compute_is_ready_next_stage(self):
        for task in self:
            task.is_ready_next_stage = all([subtask.kanban_state == 'done' for subtask in task.child_ids])


    @api.depends('stage_id.sequence', 'project_id')
    def _compute_next_stage_id(self):
        for task in self:
            task.next_stage_id = self.env['project.task.type'].search([
                                    ('project_ids', '=', task.project_id.id),
                                    ('sequence', '>', task.stage_id.sequence),
                                    ('id', '!=', task.stage_id.id)
                                ], limit=1)


    @api.depends('name', 'active_language_id')
    def _compute_translated_name(self):
        for task in self:
            translated_task = task.with_context(lang=task.active_language_id.code)
            task.translated_name = translated_task.name

    @api.depends('active_language_id', 'description', 'project_id.description', 'project_id.youtube_account_id.default_description')
    def _compute_full_description(self):
        for task in self:
            translated_task = task.with_context(lang=task.active_language_id.code)
            task.full_description = "%s %s %s %s" % (
                    translated_task.description,
                    Markup("<br />---<br />"),
                    translated_task.project_id.description or Markup(""),
                    translated_task.project_id.youtube_account_id.default_description or Markup(""),
            )

    # --------------------------------------------
    #                   ORM
    # --------------------------------------------


    def write(self, vals):
        res = super(ProjectTask, self).write(vals)
        if 'stage_id' in vals:
            self.create_auto_subtasks()
        return res

    @api.model
    def create(self, vals):
        if vals.get('project_id'):
            project = self.env['project.project'].browse(vals['project_id'])
            vals['tag_ids'] = [(4, tag.id) for tag in project.tag_ids]
            vals['user_ids'] = [(4, project.user_id.id)]
        print("=====================================================")
        print(vals)
        print("=====================================================")
        res = super(ProjectTask, self).create(vals)
        res.create_auto_subtasks()
        return res


    # --------------------------------------------
    #                   MISC
    # --------------------------------------------


    def create_auto_subtasks(self):
        # Create auto subtasks only for first level subtask
        for task in self.filtered(lambda t: not t.parent_id):
            self.create([
                {
                    'name': subtask.name,
                    'project_id': task.project_id.id,
                    'parent_id': task.id,
                } for subtask in task.stage_id.auto_subtask_ids
            ])




    # --------------------------------------------
    #                   ACTIONS
    # --------------------------------------------


    def action_move_next_stage(self):
        self.ensure_one()
        if self.is_ready_next_stage and self.next_stage_id:
            self.write({'stage_id': self.next_stage_id.id})

