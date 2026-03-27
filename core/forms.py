from django import forms
from .models import ContactEnthusiasts, GENDER_CHOICES, YES_NO_CHOICES, DISCOVER_ART_CHOICES


class ContactEnthusiastsForm(forms.ModelForm):
    gender_other = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Please specify'})
    )
    discover_art_other = forms.CharField(
        max_length=500,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Please specify'})
    )

    class Meta:
        model = ContactEnthusiasts
        fields = ['name', 'email', 'country', 'gender', 'knows_emerging_artist', 'artist_details', 'discover_art']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
            'country': forms.TextInput(attrs={'placeholder': 'Your country'}),
            'gender': forms.RadioSelect(choices=GENDER_CHOICES),
            'knows_emerging_artist': forms.RadioSelect(choices=YES_NO_CHOICES),
            'artist_details': forms.TextInput(attrs={'placeholder': 'Artist name or link'}),
            'discover_art': forms.RadioSelect(choices=DISCOVER_ART_CHOICES),
        }
        labels = {
            'knows_emerging_artist': 'Do you know any emerging artists?',
            'artist_details': 'Artist name / link',
            'discover_art': 'How do you discover art?',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['artist_details'].required = False
        # Override field choices to remove the "-------" blank option
        self.fields['gender'].choices = GENDER_CHOICES
        self.fields['knows_emerging_artist'].choices = YES_NO_CHOICES
        self.fields['discover_art'].choices = DISCOVER_ART_CHOICES

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        # Exclude the current instance when editing an existing record
        qs = ContactEnthusiasts.objects.filter(email__iexact=email)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(
                'This email address has already been registered.'
            )
        return email

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('gender') == 'other':
            gender_other = cleaned_data.get('gender_other')
            if not gender_other:
                self.add_error('gender_other', 'Please specify your gender.')
            else:
                cleaned_data['gender'] = gender_other

        if cleaned_data.get('discover_art') == 'other':
            discover_art_other = cleaned_data.get('discover_art_other')
            if not discover_art_other:
                self.add_error('discover_art_other', 'Please specify how you discover art.')
            else:
                cleaned_data['discover_art'] = discover_art_other

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.gender = self.cleaned_data['gender']
        instance.discover_art = self.cleaned_data['discover_art']
        if commit:
            instance.save()
        return instance