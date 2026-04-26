from django import forms
from .models import Faculty, Publication

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name', 'designation', 'joining_date']
        widgets = {
            'joining_date': forms.DateInput(attrs={'type': 'date'}),
        }

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['pub_type', 'title', 'venue_name', 'issn_isbn', 'month', 'year']
