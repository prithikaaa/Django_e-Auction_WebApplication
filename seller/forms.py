from django import forms
'''STATE_CHOICES = (
    ("CHANDIGARH"),
    ("HIMACHALPRADESH"),
    ("UTTARPRADESH"),
    ("WEST BENGAL")
)'''

class SellerForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    phone=forms.CharField(max_length=10)
   # city=forms.ChoiceField(choices=STATE_CHOICES)
    address=forms.CharField()