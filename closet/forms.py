from django import forms
from .models import ClosetClothes

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ClosetClothes
        fields = ['image', 'color', 'category', 'subcategory']

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ImageUploadForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance
