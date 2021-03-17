from django.shortcuts import render,get_object_or_404,redirect
from .models import Course
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.core.paginator import Paginator
from .choices import title_choices
from course.forms import PaymentForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
import razorpay
from django.views.decorators.csrf import csrf_exempt 

# Create your views here.
def coursehome(request):
    courses=Course.objects.order_by('-name').filter(is_published=True)
    paginator=Paginator(courses,12)
    page=request.GET.get('page')
    course_per_page=paginator.get_page(page)
    context={'courses':course_per_page }
    return render(request,'course/courses.html',context)

def aboutcourse(request,id):
    #import pdb
    #pdb.set_trace()
    if request.user.is_authenticated:
        course=get_object_or_404(Course,pk=id)
        data = get_object_or_404(Course, pk=id)
        name = data.name
        payment = data.selling_price_dolor * 100
        client = razorpay.Client(auth=("rzp_live_aYG3iTy4esBvYq","kiPgCmVVc00QSFdD0FDyrsNW"))

    

        user_details=User.objects.get(id=request.user.id)
        user_phoneno=user_details.userpersonaldetails.phone_no
        user_name=request.user.first_name + request.user.last_name
        user_email = request.user.email
        payment = client.order.create({'amount': payment , 'currency': 'USD', 'payment_capture':'1'}) 


        context={'course':course,
        'payment': payment,
        'user_phoneno':user_phoneno,
        'user_name':user_name,
        'user_email':user_email
        }
        return render(request,'course/course.html',context)
    return render(request,'accounts/register.html')

@csrf_exempt
def success(request):
    return render(request,'course/success.html')    

# def razorpay_getway(request,id):
#     # import pdb
#     # pdb.set_trace()
#     #if request.method == 'POST':
#     data = get_object_or_404(Course, pk=id)
#     name = data.name
#     payment = data.price * 100
#     client = razorpay.Client(auth=("rzp_test_ZREFgKjvkqNsLX","wUb00zO4eRyrWwIk9sYQiZmO"))
#     payment = client.order.create({'amount': payment , 'currency': 'INR', 'payment_capture':'1'})
#     return render(request,'course/success.html',{'payment':payment})
#    #return render(request,'course/course.html')

# def success(request):
#     if request.method == 'POST':
#         a=request.POST
#         print(a)
#     return render(request,'course/success.html')

def search(request):
    query_list=Course.objects.order_by('-title')

    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            query_list=query_list.filter(description__icontains=keywords)
    if 'title' in request.GET:
        city=request.GET['title']
        if title:
            query_list=query_list.filter(title__iexact=title)
    context={
        'title_choices':title_choices,
        'values':request.GET
    }
    return render(request,'course/search.html',context)

def paymentpage(request):
    return render(request,'course/payment.html')

def paymentconform(request):
    paymentpage=PaymentForm()
    context={'paymentpage':paymentpage}
    return render(request,'course/confirm.html',context)


def paymentdetail(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        reference=request.POST['refference']
        reference_image=request.POST['refference_image']
        user=User.objects.create_user(first_name=first_name,last_name=last_name,
        username=username,reference=reference,email=email,reference_image=refference_image)
                    #login after registration
                    #auth.login(request,user)
                    #messages.success(request,'you are logged in')
                    #return redirect('home')
                    
        user.save()
        messages.success(request,'you are successfully registered ')
        return rediect('home')
    else:
        messages.success(request,'something went wrong')
        return render(request,'accounts/confirm.html')





def cart_add(request, id):
    cart = Cart(request)
    product = Course.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Course.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


def item_increment(request, id):
    cart = Cart(request)
    product = Course.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")



def item_decrement(request, id):
    cart = Cart(request)
    product = Course.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


#@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'course/cart_detail.html')



