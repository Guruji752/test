from django.shortcuts import render,redirect
from .models import Review

# Create your views here.
def feedback(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        review=Review(name=name,email=email,subject=subject,feedback=message)
        review.save()
        return redirect('home')
    else:
        return render(request,'pages/home.html',{})
