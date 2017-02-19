from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import login_data
import requests
import random
import urllib
import urllib2

# Create your views here.
@csrf_exempt
def login_home(request):
	if request.method=='GET':
		return render(request,"index.html",{})
	else:
		try:

		    name=request.POST.get("name") 
		    number=request.POST.get("number")

		    random_number=send_otp(name,number)

		    login_data.objects.create(name=name,number=number,otp=random_number)

		    return render(request,"OtpPage.html",{"number" : number})
		    
		except Exception,e:
			print "Error"


@csrf_exempt
def login_check(request):

	if request.method=="GET":

		return render(request,"OtpPage.html",{})

	if request.method=="POST":
		otp_from_user=request.POST.get("otp")
		number_from_otp=request.POST.get("number")

		try:
			print "ff"
			otp_from_db= login_data.objects.get(number=number_from_otp)
			print "Done"
			if otp_from_db.otp==otp_from_user:
				print "Login Successful"
			return render(request,'index.html')
		except Exception,e:
			print "Error"
			return render(request,"OtpPage.html")



def send_otp(name,number):

	rand = random.randint(1000,9999)

	authkey = "125195AvX4LUlVf57dcd941"
	mobiles = str(number)
	message = "Dear " +str(name)+", welcome to CODENICELY this is the one time password "+str(rand)+" for login"
	sender = "CODNIC"
	route = "4"


	values = {
    	      'authkey' : authkey,
        	  'mobiles' : mobiles,
      	      'message' : message,
              'sender' : sender,
              'route' : route
              }


	url="http://api.msg91.com/api/sendhttp.php"

	postdata = urllib.urlencode(values)
	req = urllib2.Request(url, postdata)
	response = urllib2.urlopen(req)

	output = response.read() # Get Response

	return rand