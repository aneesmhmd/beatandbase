from decimal import Decimal
from admin_products.models import Product
from admin_variant.models import Product_Variant



class Cart():
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get('session_key')

        if not 'session_key' in request.session:
            cart = self.session['session_key'] = {}
        
        self.cart =  cart

    def add(self,variant,product,color,price,product_qty):
        variant_id = str(variant.id)

        if variant_id in self.cart:
            if self.cart[variant_id]['color'] == color:
                self.cart[variant_id]['qty'] = product_qty
            else:
                self.cart[variant_id] = {'color':str(color),'price':str(price),'qty':product_qty}
        
        else:
            self.cart[variant_id] = {'color':str(color),'price':str(price),'qty':product_qty}
        self.session.modified = True

    def delete(self, variant):

        variant_id = str(variant)

        if variant_id in self.cart:

            del self.cart[variant_id]

        self.session.modified = True

    
    def update(self, variant, qty):

        variant_id = str(variant)
        product_quantity = qty

        if variant_id in self.cart:

            self.cart[variant_id]['qty'] = product_quantity

        self.session.modified = True



    def __len__(self):

        val = 0
        for x in self.cart.values():
            val += 1
        
        return val
    


    def __iter__(self):

        all_product_ids = self.cart.keys()

        variants = Product_Variant.objects.filter(id__in=all_product_ids)

        cart = self.cart.copy()

        for variant in variants:

            cart[str(variant.id)]['variant'] = variant

        
        for item in cart.values():

            item['price'] = Decimal(item['price'])

            item ['total'] = item['price'] * item['qty']

            yield item

    
    def get_total(self):

        return sum(Decimal( item['price']) * item['qty'] for item in self.cart.values() )
    
    def get_gst(self):
        sub_total = sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())
        gst = Decimal(sub_total) * Decimal('0.05')
        grand = gst + sub_total + 100
        # grand = 9
        return grand

    