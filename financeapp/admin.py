from django.contrib import admin
from financeapp.models import User,LogInForm,appointment, Contact


# Register your models here.
admin.site.register(User)

admin.site.register(LogInForm)

admin.site.register(appointment)

admin.site.register(Contact)