from django.shortcuts import render,redirect
from course.models import Course
from .models import Team,Contact,Create_Course,Upload_Content
# Create your views here.
def index(request):
    courses=Course.objects.order_by('-name').filter(is_popluar=True)[:6]
    featured_course=Course.objects.order_by('-name').filter(is_featured=True)[:3]
    context={'courses':courses,
    'featured_course':featured_course
    
    }
    return render(request,'pages/home.html',context)


def aboutus(request):
    team=Team.objects.all()
    context={'team':team}
    return render(request,'pages/about.html',context)



def contactus(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        phone=request.POST['phone']
        email=request.POST['email']
        message=request.POST['message']
        contact=Contact(first_name=first_name,last_name=last_name,phone=phone,email=email,message=message)
        contact.save()
        return redirect('home')
    else:
        return render(request,'pages/contact.html')


def createcourse(request):
    if request.method=='POST':
        name=request.POST['name']
        qualification=request.POST['qualification']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        create=Create_Course(name=name,qualification=qualification,email=email,phone=phone,content=content)
        create.save()
        return redirect('home')
    else:
        return render(request,'pages/createcourse.html')

def uploadcontent(request):
    if request.method=='POST':
        name=request.POST['name']
        qualification=request.POST['qualification']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        upload=Upload_Content(name=name,qualification=qualification,email=email,phone=phone,content=content)
        upload.save()
        return redirect('home')
    else:
        return render(request,'pages/uploadcontent.html')


def privacypolicy(request):
    return render(request,'pages/policy.html')



