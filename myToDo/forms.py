from django import forms

class ToDoForm(forms.Form):   # forms.Form inherite
      text_todo = forms.CharField(widget = forms.TextInput(attrs =
                                            {'class': 'form-control','placeholder': 'Add new Todo here'}))