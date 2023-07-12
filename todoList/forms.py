from django import forms

class todoList_forms(forms.Form):
    text =forms.CharField(max_length =20,
        widget=forms.Textarea(
        attrs={'class' : 'form-control', 'placeholder' : 'Enter todo e.g grocery shopping ', 'aria-label ':'Todo', 'aria-describeby':'add-btn'}))
