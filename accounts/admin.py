from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User
from .models import ActivationRequest


class CustomUserAdmin(UserAdmin):

    # list_display = ('username', 'email', 'first_name', 'phone', 'address', 'is_staff')
    list_display = ('username', 'email', 'first_name', 'phone', 'address', 'reseller_status')
    # list_filter = ('is_staff', 'is_superuser', 'is_active')
    list_filter = ()
    search_fields = ('username', 'email', 'first_name', 'phone', 'address')
    ordering = ('username',)

    # admin panel user info interface
    fieldsets = (
        ('User', {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name','shopname', 'email', 'phone', 'address', 'is_active', 'reseller_status', 'is_staff', 'is_superuser')}),
        # ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined', 'activation_date', 'expiry_date')}),
    )

    # adding user using admin panel interface
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            # 'fields': ('username', 'password1', 'password2', 'first_name', 'email', 'phone', 'address', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            'fields': ('username', 'password1', 'password2', 'shopname', 'first_name', 'email', 'phone', 'address', 'is_active', 'is_staff', 'is_superuser',)}
        ),
    )


class ActivationRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'trxid', 'requested_at')
    search_fields = ('user__username', 'trxid')
    list_filter = ('requested_at',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('user')


admin.site.register(User, CustomUserAdmin)
admin.site.register(ActivationRequest)
admin.site.unregister(Group)


