from django.contrib import admin
from it.models import VirtualMachineType, VirtualMachine, ItemType, Item, InventoryUserCompany, InventoryUser, Project, Reservation


admin.site.register(VirtualMachineType)
admin.site.register(VirtualMachine)
admin.site.register(ItemType)
admin.site.register(Item)
admin.site.register(InventoryUserCompany)
admin.site.register(InventoryUser)
admin.site.register(Project)
admin.site.register(Reservation)
