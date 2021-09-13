from .models import Product, Review, Voucher
from django import forms


class VoucherApplyForm(forms.Form):
    code = forms.CharField()

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('text','photo')
       
        