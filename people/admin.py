from django.contrib import admin

from people.models import Customer, Vendor

class MembershipInline(admin.TabularInline):
    model = Vendor.clients.through

class CustomerAdmin(admin.ModelAdmin):
	inlines = [
        MembershipInline,
    ]
	# pass

class VendorAdmin(admin.ModelAdmin):
	inlines = [
        MembershipInline,
    ]
	# pass
	exclude = ('clients',)

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Vendor, VendorAdmin)



# from django.contrib import admin

# class MembershipInline(admin.TabularInline):
#     model = Group.members.through

# class PersonAdmin(admin.ModelAdmin):
#     inlines = [
#         MembershipInline,
#     ]

# class GroupAdmin(admin.ModelAdmin):
#     inlines = [
#         MembershipInline,
#     ]
#     exclude = ('members',)