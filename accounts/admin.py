from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Account)
admin.site.register(PasswordResetToken)
admin.site.register(TemporaryAccount)
admin.site.register(Evenement)
# admin.site.register(Events)
# admin.site.register(ReserveEvent)