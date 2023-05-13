import uuid

from django.db import models

# Create your models here.


class Interface(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=255)

    def __str__(self):
        return self.name


class Component(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # PK
    name = models.TextField(max_length=255)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)  # choices?, FK
    url = models.URLField(blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="images")
    description = models.TextField(max_length=255)
    datasheet = models.URLField(blank=True)
    location = models.ForeignKey(
        "Location", on_delete=models.CASCADE
    )  # choices, also foreign key
    mfn_pn = models.TextField(max_length=255)
    count = models.IntegerField(default=1)
    interfaces = models.ManyToManyField(Interface, blank=True)
    voltage_operating = models.FloatField(blank=True, null=True)


class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(max_length=255)

    def __str__(self):
        return self.name
