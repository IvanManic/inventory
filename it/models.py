from django.db import models


class VirtualMachineType(models.Model):
    type = models.CharField(max_length=32)

    def __unicode__(self):
        return self.type


class VirtualMachine(models.Model):
    type = models.ForeignKey(VirtualMachineType)
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name


class ItemType(models.Model):
    type = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    default_name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name


class Item(models.Model):
    type = models.ForeignKey(ItemType)
    name = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    inv_number = models.CharField(max_length=32)
    vm_link = models.ForeignKey(VirtualMachine)

    def __unicode__(self):
        return self.name


class InventoryUserCompany(models.Model):
    name = models.CharField(max_length=64)
    short_name = models.CharField(max_length=6)

    def __unicode__(self):
        return self.name


class InventoryUser(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    short_name = models.CharField(max_length=3)
    email = models.EmailField()
    company = models.ForeignKey(InventoryUserCompany)

    def __unicode__(self):
        return self.first_name + " " + self.last_name


class Project(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name


class Reservation(models.Model):
    item = models.ForeignKey(Item)
    user = models.ForeignKey(InventoryUser)
    project = models.ForeignKey(Project)
    created = models.DateTimeField()
    reserved_until = models.DateTimeField()
    is_active = models.BooleanField(default=True)