from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)



class ProjectProject(models.Model):
    _inherit = "project.project"

    epic_ids = fields.One2many('project.epic', 'project_id', string="Epics")

    def get_epic_count(self):
        self.ensure_one()
        return {
            'epicCount': len(self.epic_ids),
        }
