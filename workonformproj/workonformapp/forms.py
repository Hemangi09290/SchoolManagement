# import the standard Django Forms
from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Student, Country, City

# creating a form here InputForm will takes input from user kinds of field
class InputForm(forms.Form):

	first_name = forms.CharField(max_length = 200)
	last_name = forms.CharField(max_length = 200)
	roll_number = forms.IntegerField(
					help_text = "Enter 6 digit roll number"
					)
	password = forms.CharField(widget = forms.PasswordInput())

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'roll_number', 'password', 'picture', 'DOB', 'email', 'country', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set

