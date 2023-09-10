from django.contrib import admin
from .models import *
# Register the models in the admin site.
admin.site.register(Category)
admin.site.register(Product)
# admin.site.register(Coupon)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Tag)
admin.site.register(ProductComment)
