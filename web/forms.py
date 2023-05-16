from django import forms

from web.models import Category
from web.models import Component
from web.models import Interface
from web.models import Location


class NewComponentForm(forms.Form):
    name = forms.CharField(label="Item Name", max_length=255)
    category = forms.ModelChoiceField(
        label="Category", queryset=Category.objects.all(), initial=0
    )
    url = forms.URLField(label="Manufacturer page")
    image = forms.ImageField()
    description = forms.CharField(label="Long description", max_length=255)
    datasheet = forms.URLField()
    location = forms.ModelChoiceField(
        label="Location",
        queryset=Location.objects.all(),
        to_field_name="name",
        initial=0,
    )
    mfn_pn = forms.CharField(label="Manufacturer part number", max_length=255)
    count = forms.IntegerField(label="Count")
    interfaces = forms.ModelMultipleChoiceField(
        queryset=Interface.objects.all(),
        initial=0,
        widget=forms.CheckboxSelectMultiple(),
    )
    voltage_operating = forms.FloatField(label="Operating Voltage")
    # TODO should be implementing clean(self)


class NewCategoryForm(forms.Form):
    name = forms.CharField(label="Category", max_length=255)


class NewLocationForm(forms.Form):
    name = forms.CharField(label="Location", max_length=255)


class NewInterfaceForm(forms.Form):
    name = forms.CharField(label="Interface", max_length=255)


class EditComponent(forms.ModelForm):
    name = forms.CharField(label="Item Name", max_length=255)
    category = forms.ModelChoiceField(
        label="Category", queryset=Category.objects.all(), initial=0
    )
    url = forms.URLField(label="Manufacturer page")
    image = forms.ImageField()
    description = forms.CharField(label="Long description", max_length=255)
    datasheet = forms.URLField()
    location = forms.ModelChoiceField(
        label="Location",
        queryset=Location.objects.all(),
        to_field_name="name",
        initial=0,
    )
    mfn_pn = forms.CharField(label="Manufacturer part number", max_length=255)
    count = forms.IntegerField(label="Count")
    interfaces = forms.ModelMultipleChoiceField(
        queryset=Interface.objects.all(),
        initial=0,
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    # TODO should be implementing clean(self)
    class Meta:
        model = Component
        exclude = []


class EditLocation(forms.ModelForm):
    name = forms.CharField(label="Name", max_length=255)

    class Meta:
        model = Location
        exclude = []


class EditInterface(forms.ModelForm):
    name = forms.CharField(label="Name", max_length=255)

    class Meta:
        model = Interface
        exclude = []


class EditCategory(forms.ModelForm):
    name = forms.CharField(label="Name", max_length=255)

    class Meta:
        model = Category
        exclude = []
