from django import forms
from .models import Bug


class BugForm(forms.ModelForm):
    """this is the form to capture the data entered in the form"""

    class Meta:
        """this class captures the field names"""
        model = Bug
        fields = ['description', 'bug_type', 'status']
