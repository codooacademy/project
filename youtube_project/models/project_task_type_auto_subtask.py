from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)

class ProjectTaskTypeAutoSubtask(models.Model):
    _name = "project.task.type.auto.subtask"
    _description = ""

    name = fields.Char(string="Name", required=True)
    stage_id = fields.Many2one('project.task.type', string="Stage", required=True, ondelete='cascade')
