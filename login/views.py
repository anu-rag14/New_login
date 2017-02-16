from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import login_data

# Create your views here.
@csrf_exempt
def login_home(request):
	if request.method=='GET':
		return render(request,"index.html",{})
	else:
		name=request.POST.get("name")
		number=request.POST.get("number")

		p=login_data.objects.create(name=name,number=number)


		return render(request,"index.html",{}) 


