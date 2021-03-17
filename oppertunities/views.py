from django.shortcuts import render
from .models import Writing,HealthCare_LiveSession,HealthCare_OnlineConseltant,HealthCare_VideoLesson,HomeCare,Research,Translation

# Create your views here.
def writing(request):
    writing_list=Writing.objects.all()
    context={"writing_list":writing_list}
    return render(request,'oppertunites/writing.html',context)


def research(request):
    research_list=Research.objects.all()
    context={"research_list":research_list}
    return render(request,'oppertunites/Reaserch.html',context)



def translation(request):
    translation_list=Translation.objects.all()
    context={"translation_list":translation_list}
    return render(request,'oppertunites/Translation.html',context)



def healthCare_LiveSession(request):
    healthCare_LiveSession_list=HealthCare_LiveSession.objects.all()
    context={"healthCare_LiveSession_list":healthCare_LiveSession_list}
    return render(request,'oppertunites/healthcareLive.html',context)


def healthCare_OnlineConseltant(request):
    healthCare_OnlineConseltant_list=HealthCare_OnlineConseltant.objects.all()
    context={"healthCare_OnlineConseltant_list":healthCare_OnlineConseltant_list}
    return render(request,'oppertunites/healthCareOnline.html',context)


def healthCare_VideoLesson(request):
    healthCare_VideoLesson_list=HomeCare.objects.all()
    context={"healthCare_VideoLesson_list":healthCare_VideoLesson_list}
    return render(request,'oppertunites/healthcareVideo.html',context)



def  homeCare(request):
    homeCare_list=HomeCare.objects.all()
    context={"homeCare_list":homeCare_list}
    return render(request,'oppertunites/homecare.html',context)


def apply(request):
    return render(request,'oppertunites/apply.html')