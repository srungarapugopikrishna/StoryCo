from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import MainForm 
# Create your views here.
def index(request):
    return HttpResponse("Hello, Welcome to the UNIVERSE.")

@login_required
def home(request):
	#return HttpResponse("Logged in successfully")
	return render(request, 'home.html')
def registered():
	return HttpResponse("Registered in successfully")
def editor(request):
	context = {}
	context['form'] = MainForm()
	if request.method == 'POST':
		# if request.POST['form-type']=='storyForm':
		data = request.POST
		print data
	return render(request, 'editor.html',context)
def formData(request):
	if request.method == 'POST':
		if request.POST['form-type']=='storyForm':
			data = request.POST
			print data
