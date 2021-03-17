from django.shortcuts import render
from course.models import *
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import View
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse


from django.conf import settings
from django.views.decorators.csrf import csrf_exempt 

# Create your views here.

@csrf_exempt
def payment_done(request):
	return render(request,'payment/done.html')




def payment_canceled(request):
	return render(request,'payment/canceled.html')



# def razorpay_getway(request,id):
#     import pdb
#     pdb.set_trace()
#     #if request.method == 'POST':
#     data = get_object_or_404(Course, pk=id)
#     name = data.name
#     payment = data.selling_price_dolor * 100
#     client = razorpay.Client(auth=("rzp_test_ZREFgKjvkqNsLX","wUb00zO4eRyrWwIk9sYQiZmO"))
#     payment = client.order.create({'amount': payment , 'currency': 'USD', 'payment_capture':'1'})
#     return render(request,'course/success.html',{'payment':payment})

	

def payment_process(request,id):
	host = request.get_host()
	data = get_object_or_404(Course, pk=id)
	name=data.name
	payment = int(data.selling_price_dolor) 
	paypal_dict={
		'business': settings.PAYPAL_RECEIVER_EMAIL,
		'amount': payment,
		'currency_code':'USD',
		'notify_url':'http://{}{}'.format(host, reverse('paypal-ipn')),
		'return_url':'http://{}{}'.format(host,reverse('done')),
		#'cancel_return':'http://{}{}'.format(host,reverse('canceled')),

	}
	form = PayPalPaymentsForm(initial=paypal_dict)
	return render(request,'payment/process.html',{'form':form})

