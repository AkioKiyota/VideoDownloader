from django.forms import *


class input_form(Form):
    data = CharField(label='URL', max_length=100, required=True)


class video_form(Form):
    resolution = ChoiceField(widget=Select)
