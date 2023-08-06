from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)


class SocialAccount(models.Model):
    _inherit = "social.account"

    default_description = fields.Html(translate=True)
