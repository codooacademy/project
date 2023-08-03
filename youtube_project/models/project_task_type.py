from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)



class ProjectTaskType(models.Model):
    _inherit = "project.task.type"

    auto_subtask_ids = fields.One2many('project.task.type.auto.subtask', 'stage_id', string="Auto Subtasks")
    is_youtube_default = fields.Boolean()


    """
    Queue
    > Planned Date
    Scripting
    Filming
    Editing
    SEO
    > Check title
    > Check description
    > Add chapters
    > Add cards & end-screens
    
    Uploading
    
    Promoting
    > Create a new social post
    
    Done
    
    """


