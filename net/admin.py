from django.contrib import admin

from net.models import Contact, NetMember, Product


@admin.register(NetMember)
class NetMemberAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "level",
        "suplier",
        "debt",
        "created_at",
    )
    list_filter = ("contacts__city",)
    actions = [
        "clear_netmember_debt",
    ]

    def clear_netmember_debt(self, request, queryset):
        queryset.update(debt=0.00)

    clear_netmember_debt.short_description = "Очиcтить долги"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "country",
        "city",
        "street",
    )
    list_filter = (
        "country",
        "city",
        "street",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "model",
        "release_date",
    )
    list_filter = (
        "name",
        "model",
    )
