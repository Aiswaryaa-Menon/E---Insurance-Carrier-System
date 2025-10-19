from django.contrib import admin
from .models import CustPolDocs,CustomerPolicy,PremiumSchedules
# Register your models here.
admin.site.register(CustPolDocs)
admin.site.register(CustomerPolicy)
admin.site.register(PremiumSchedules)
