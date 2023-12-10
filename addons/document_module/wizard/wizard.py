from odoo import models, fields, api

class DocumentWizard(models.TransientModel):
    _name = 'document_module.wizard'
    _description = 'Document Wizard'

    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    employee_id = fields.Many2one('hr.employee', string='Employee')

    def print_documents(self):
        domain = []

        if self.date_from:
            domain.append(('created_date', '>=', self.date_from))
        if self.date_to:
            domain.append(('created_date', '<=', self.date_to))
        if self.employee_id:
            domain.append(('responsible_employee_ids', 'in', [self.employee_id.id]))

        documents = self.env['document_module.document'].search(domain)

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'document_module.document',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', documents.ids)],
            'target': 'current',
        }
