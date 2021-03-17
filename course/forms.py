from django import forms





class PaymentForm(forms.Form):
    name=forms.CharField(max_length=200,label="Enter your name")
    username=forms.CharField(max_length=300,label="enter your User Name")
    email=forms.EmailField(max_length=300,label="Enter your Email")
    phone=forms.CharField(max_length=15,label="Enter Your phone Number")
    image=forms.FileField()