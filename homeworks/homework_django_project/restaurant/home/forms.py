from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'Your Name',
            'data-rule': 'minlen:4',
            'data-msg': 'Please enter at least 4 chars'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Your Email',
            'data-rule': 'email',
            'data-msg': 'Please enter a valid email'
        })
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'phone',
            'placeholder': 'Your Phone',
            'data-rule': 'minlen:4',
            'data-msg': 'Please enter at least 4 chars'
        })
    )
    date = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'date',
            'placeholder': 'Date',
            'type': 'date',
            'data-rule': 'minlen:4',
            'data-msg': 'Please enter at least 4 chars'
        })
    )
    time = forms.TimeField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'time',
            'placeholder': 'Time',
            'type': 'time',
            'data-rule': 'minlen:4',
            'data-msg': 'Please enter at least 4 chars'
        })
    )
    number_of_guests = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'people',
            'placeholder': '# of people',
            'data-rule': 'minlen:1',
            'data-msg': 'Please enter at least 1 chars'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Message'
        })
    )

    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone', 'date', 'time', 'number_of_guests', 'message')
