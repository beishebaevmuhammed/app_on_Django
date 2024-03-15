from django.contrib import admin

from carts.admin import CartTabAdmin
from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email",]
    search_fields = ["first_name", "last_name", "email",]
    list_filter = ["first_name", "last_name", "email",]

    inlines = [CartTabAdmin,]
