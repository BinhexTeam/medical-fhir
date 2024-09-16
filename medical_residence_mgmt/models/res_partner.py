from odoo import models, fields, api, tools, _
import logging
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class Resident(models.Model):
    _inherit = "res.partner"

    room_id = fields.Many2one(
        "residence.room", 
        string=_("Room"),
        track_visibility='onchange'
    ) 