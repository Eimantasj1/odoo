from odoo import models, fields, api


class DocumentWizard(models.TransientModel):
    _name = 'document_module.wizard'
    _description = 'Document Wizard'

    date_from = fields.Date(string='From Date')
    date_to = fields.Date(string='To Date')
    employee_ids = fields.Many2many('res.users', string='Select Employees')

    def print_documents(self):
        documents = self.env['document_module.document'].search([
            ('created_date', '>=', self.date_from),
            ('created_date', '<=', self.date_to),
            ('creator_user_id', 'in', self.employee_ids.ids)
        ])

        if documents:
            return {
                'name': 'Documents',
                'type': 'ir.actions.act_window',
                'view_mode': 'tree,form',
                'target': 'new',
                'res_model': 'document_module.document',
                'domain': [('id', 'in', documents.ids)],
            }
        else:
            return {
                'type': 'ir.actions.act_window_close',
                'context': {'message': 'No documents found matching the criteria.'}
            }
