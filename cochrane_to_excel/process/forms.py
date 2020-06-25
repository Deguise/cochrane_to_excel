"""
Form file
"""
from django import forms

class ProcessForm(forms.Form):
    """
    Process Form
    """
    html_pages = forms.FileField(
        label='HTML pages',
        required=True,
        widget=forms.ClearableFileInput(
            attrs={
                'accept': '.html',
                'multiple': True
                }
            )
        )
