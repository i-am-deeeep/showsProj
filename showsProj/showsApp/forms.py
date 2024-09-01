from django.forms import ModelForm
from showsApp.models import Shows

# Create the form class.
class ShowsForm(ModelForm):
    class Meta:
        model = Shows
        fields = "__all__"