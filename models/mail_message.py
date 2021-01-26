# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MailMessage(models.Model):
    _inherit = 'mail.message'
    _description = 'mail.message'

    is_outgoing = fields.Boolean()

    def create(self, vals):
        res = super(MailMessage, self).create(vals)
        users_as_incoming = self.env['res.config.settings']._get_incoming_users().mapped('partner_id')
        for msg in res:
            user = self.env['res.users'].search([('partner_id', '=', msg.author_id.id)])
            if user and not msg.author_id in users_as_incoming:
                msg.is_outgoing = True
        return res

    def _get_message_format_fields(self):
        return [
            'id', 'body', 'date', 'author_id', 'email_from',
            'message_type', 'subtype_id', 'subject',
            'model', 'res_id', 'record_name',
            'channel_ids', 'partner_ids', 'is_outgoing',
            'starred_partner_ids',
            'moderation_status',
        ]