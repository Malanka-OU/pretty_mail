# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    users_as_incoming = fields.Many2many('res.users', string="Users whose messages will be considered incoming")

    def set_values(self):
        self.ensure_one()
        super(ResConfigSettings, self).set_values()
        set_param = self.env['ir.config_parameter'].sudo().set_param
        set_param('contact_deduplicate.users_as_incoming', self.users_as_incoming.ids)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        get_param = self.env['ir.config_parameter'].sudo().get_param
        u_ids = get_param('contact_deduplicate.users_as_incoming')
        if u_ids:
            res['users_as_incoming'] = eval(u_ids)
        return res

    @api.model
    def _get_incoming_users(self):
        get_param = self.env['ir.config_parameter'].sudo().get_param
        u_ids = get_param('contact_deduplicate.users_as_incoming')
        u_ids = eval(u_ids) if u_ids else []
        users = self.env['res.users'].browse(u_ids)
        return users