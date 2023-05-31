from django.contrib import admin
from vier_node.models import pricing_table, membership, contact_us, newsletter, login_details

admin.site.register(pricing_table)
admin.site.register(membership)
admin.site.register(contact_us)
admin.site.register(newsletter)
admin.site.register(login_details)