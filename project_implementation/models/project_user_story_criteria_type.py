from random import randint
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)


class ProjectUserStoryCriteriaType(models.Model):
    _name = "project.user.story.criteria.type"
    _description = "project.user.story.criteria.type"

    @api.model
    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char(required=True)
    color = fields.Integer(default=_get_default_color)
    must_create_task = fields.Boolean(default=False)
