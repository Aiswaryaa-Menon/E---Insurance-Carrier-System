from django.contrib import admin

# Register your models here.
from .models import RoleModel,CustomerRegistration,AgentRegistration

admin.site.register(RoleModel)
admin.site.register(CustomerRegistration)
admin.site.register(AgentRegistration)