from django import forms

from tasks.models import Tasks


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
        exclude = ('author', 'added_on', )
