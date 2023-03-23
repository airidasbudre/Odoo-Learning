from odoo import api, models, fields


class NotebookFields(models.Model):
    _inherit = 'product.template'

    image1 = fields.Binary(string='Image')

    def add_photos(self):
        # Open a dialog box to add image1
        image1 = self.env['ir.attachment'].search([('res_model', '=', 'product.template'), ('res_id', '=', self.id)])
        if len(image1) < 2:
            return {
                'type': 'ir.actions.act_url',
                'url': '/web#action=ir.attachment.action_wizard&model=ir.attachment&context={"default_res_model": "product.template", "default_res_id": %d}' % self.id,
                'target': 'new',
            }
        else:
            return {
                'warning': {
                    'title': 'Warning',
                    'message': 'You can only add up to 2 image1.'
                }
            }

    alternative_product_ids = fields.Many2many(
        'product.template', 'product_alternative_rel', 'src_id', 'dest_id', check_company=True,
        string='Alternative Products', help='Suggest alternatives to your customer (upsell strategy). '
        'Those products show up on the product page.')
    
    accessory_product_ids = fields.Many2many(
        'product.product', 'product_accessory_rel', 'src_id', 'dest_id', string='Accessory Products', check_company=True,
        help='Accessories show up when the customer reviews the cart before payment (cross-sell strategy).')
    
    allow_out_of_stock_order = fields.Boolean(string='Continue selling when out-of-stock', default=True)


class ProgressBar(models.Model):
    _inherit = 'product.product'

    progress_amazon = fields.Float(string='Amazon', compute='_compute_amazon_percentage', store=True)
    progress_ebay = fields.Float(string='Ebay', compute='_compute_ebay_percentage', store=True)
    progress_lt = fields.Float(string='LT', compute='_compute_lt_percentage', store=True)
    progress_lv = fields.Float(string='LV', compute='_compute_lv_percentage', store=True)
    progress_ee = fields.Float(string='EE', compute='_compute_ee_percentage', store=True)

    @api.depends('list_price', 'uom_id', 'image_1920', 'weight')
    def _compute_amazon_percentage(self):
        for product in self:
            filled_fields = 0
            if not product.list_price == 1: #Other solution is make list_price field by default empty
                filled_fields += 1
            if product.uom_id:
                filled_fields += 1
            if product.image_1920:
                filled_fields += 1
            if product.weight:
                filled_fields += 1
            tracked_fields = 4  
            product.progress_amazon = (filled_fields / tracked_fields) * 100

    @api.depends('list_price', 'allow_out_of_stock_order', 'image_1920', 'attribute_line_ids')
    def _compute_ebay_percentage(self):
        for product in self:
            filled_fields = 0
            if not product.list_price == 1:
                filled_fields += 1
            if product.allow_out_of_stock_order:
                filled_fields += 1
            if product.image_1920:
                filled_fields += 1
            if len(product.attribute_line_ids) > 0:
                filled_fields += 1
            tracked_fields = 4  
            product.progress_ebay = (filled_fields / tracked_fields) * 100

    @api.depends('list_price', 'uom_id', 'image_1920', 'alternative_product_ids')
    def _compute_lt_percentage(self):
        for product in self:
            filled_fields = 0
            if not product.list_price == 1:
                filled_fields += 1
            if product.uom_id:
                filled_fields += 1
            if product.image_1920:
                filled_fields += 1
            if len(product.alternative_product_ids) > 0:
                filled_fields += 1
            tracked_fields = 4  
            product.progress_lt = (filled_fields / tracked_fields) * 100

    @api.depends('list_price', 'weight', 'image_1920', 'volume')
    def _compute_lv_percentage(self):
        for product in self:
            filled_fields = 0
            if not product.list_price == 1:
                filled_fields += 1
            if product.weight:
                filled_fields += 1
            if product.image1:
                filled_fields += 1
            if product.volume:
                filled_fields += 1
            tracked_fields = 4  
            product.progress_lv = (filled_fields / tracked_fields) * 100

    @api.depends('list_price', 'weight', 'accessory_product_ids', 'image_1920', 'volume')
    def _compute_ee_percentage(self):
        for product in self:
            filled_fields = 0
            if not product.list_price == 1:
                filled_fields += 1
            if product.weight:
                filled_fields += 1
            if product.volume:
                filled_fields += 1
            if product.image_1920:
                filled_fields += 1
            if len(product.accessory_product_ids) > 0:
                filled_fields += 1
            tracked_fields = 5  
            product.progress_ee = (filled_fields / tracked_fields) * 100