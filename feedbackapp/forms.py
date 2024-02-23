from django import forms
from feedbackapp.models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 400px; height: 40px;','placeholder':'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'width: 400px; height: 40px;','placeholder':'Your Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 400px; height: 150px;','placeholder':'Message'}),
        }