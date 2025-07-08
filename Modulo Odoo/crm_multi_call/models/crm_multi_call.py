from odoo import models, fields, api, _
import socket

class CrmMultiCall(models.Model):
    _name = 'crm.multi.call'
    _description = 'CRM Multi Call'

    lead_id = fields.Many2one('crm.lead', string='Lead/Opportunity')
    partner_id = fields.Many2one('res.partner', string='Contact')
    phone_numbers = fields.Char(string='Phone Numbers')  # Comma separated
    status = fields.Selection([
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('answered', 'Answered'),
        ('failed', 'Failed'),
        ('done', 'Done'),
    ], default='pending', string='Status')
    note = fields.Text(string='Note')
    result_number = fields.Char(string='Answered Number')

    def action_start_multi_call(self):
        self.status = 'in_progress'
        numbers = self.phone_numbers.split(',')
        for number in numbers:
            answered = self._call_via_ami(number.strip())
            if answered:
                self.status = 'answered'
                self.result_number = number.strip()
                break
        else:
            self.status = 'failed'
        self._log_activity()

    def _call_via_ami(self, number):
        ami_host = self.env['ir.config_parameter'].sudo().get_param('crm_multi_call.ami_host')
        ami_port = int(self.env['ir.config_parameter'].sudo().get_param('crm_multi_call.ami_port', 5038))
        ami_user = self.env['ir.config_parameter'].sudo().get_param('crm_multi_call.ami_user')
        ami_password = self.env['ir.config_parameter'].sudo().get_param('crm_multi_call.ami_password')
        extension = self.env['ir.config_parameter'].sudo().get_param('crm_multi_call.extension')
        context = self.env['ir.config_parameter'].sudo().get_param('crm_multi_call.context', 'from-internal')
        if not all([ami_host, ami_user, ami_password, extension]):
            return False
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(10)
            s.connect((ami_host, ami_port))
            login = f"Action: Login\r\nUsername: {ami_user}\r\nSecret: {ami_password}\r\nEvents: off\r\n\r\n"
            s.send(login.encode())
            response = s.recv(1024)
            if b'Authentication accepted' not in response:
                s.close()
                return False
            originate = (
                f"Action: Originate\r\n"
                f"Channel: SIP/{extension}\r\n"
                f"Exten: {number}\r\n"
                f"Context: {context}\r\n"
                f"Priority: 1\r\n"
                f"CallerID: {extension}\r\n"
                f"Timeout: 20000\r\n"
                f"Async: false\r\n\r\n"
            )
            s.send(originate.encode())
            originate_response = s.recv(4096)
            logout = "Action: Logoff\r\n\r\n"
            s.send(logout.encode())
            s.close()
            if b'Success' in originate_response:
                return True
        except Exception:
            return False
        return False

    def _log_activity(self):
        if self.lead_id:
            self.env['mail.activity'].create({
                'res_model_id': self.env['ir.model']._get_id('crm.lead'),
                'res_id': self.lead_id.id,
                'activity_type_id': self.env.ref('mail.mail_activity_data_call').id,
                'summary': _('Multi Call'),
                'note': self.note or '',
            })
        elif self.partner_id:
            self.env['mail.activity'].create({
                'res_model_id': self.env['ir.model']._get_id('res.partner'),
                'res_id': self.partner_id.id,
                'activity_type_id': self.env.ref('mail.mail_activity_data_call').id,
                'summary': _('Multi Call'),
                'note': self.note or '',
            })

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def action_create_multi_call(self):
        self.ensure_one()
        phone_numbers = []
        if self.phone:
            phone_numbers.append(self.phone)
        if self.mobile:
            phone_numbers.append(self.mobile)
        multi_call = self.env['crm.multi.call'].create({
            'lead_id': self.id,
            'phone_numbers': ','.join(phone_numbers),
        })
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'crm.multi.call',
            'res_id': multi_call.id,
            'view_mode': 'form',
            'target': 'new',
        }

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def action_create_multi_call(self):
        self.ensure_one()
        phone_numbers = []
        if self.phone:
            phone_numbers.append(self.phone)
        if self.mobile:
            phone_numbers.append(self.mobile)
        multi_call = self.env['crm.multi.call'].create({
            'partner_id': self.id,
            'phone_numbers': ','.join(phone_numbers),
        })
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'crm.multi.call',
            'res_id': multi_call.id,
            'view_mode': 'form',
            'target': 'new',
        } 