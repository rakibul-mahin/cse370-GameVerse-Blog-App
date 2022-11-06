from dataclasses import fields
from xml.etree.ElementInclude import include
from django.forms import ModelForm
from .models import Room, Item

class CreateRoomForm(ModelForm):
    class Meta:
        model = Room
        # fields = '__all__'
        exclude = ['host','participants']

class CreateItemForm(ModelForm):
    class Meta:
        model = Item
        # fields = '__all__'
        exclude = ['creator','sold','buyer']

class SoldItem(ModelForm):
    class Meta:
        model = Item
        fields = ['sold']