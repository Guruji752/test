from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def contact(request):
    if request.method=='POST':
        course_id=request.POST['course_id']
        course=request.POST['course']
        email=request.POST['email']
        name=request.POST['name']
        phone=request.POST['phone']
        user_id=request.POST['user_id']
        message=request.POST['message']
        contact=Contact(course_id=course_id,course=course,email=email,name=name,
        phone=phone,message=message,user_id=user_id)
        #check for already request
        if request.user.is_authenticated:
            user_id=request.user.id
            has_conected=Contact.objects.all().filter(course_id=course_id,user_id=user_id)
            if has_conected:
                messages.error(request,'you already made a request for this listing')
                return redirect('/Courses/' +course_id)
        contact.save()
        messages.success(request,'your request has been submitted, a realtor will get back to you soon')
        return redirect('/Courses/'+ course_id)
