from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import MainForm,SomeForm
from .models import Story,relations 
from django.shortcuts import render_to_response
import uuid
# Create your views here.
def index(request):
    return HttpResponse("Hello, Welcome to the UNIVERSE.")

@login_required
def home(request):
	#return HttpResponse("Logged in successfully")

	all_stories = Story.objects.all()
	data = {"stories": all_stories}
	#request.session['data'] = data
	return render_to_response('home.html', data)
def registered():
	return HttpResponse("Registered in successfully")
def editor(request):
	context = {}
	context['form'] = MainForm()
	if request.method == 'POST':
		# if request.POST['form-type']=='storyForm':
		data = request.POST
		print request.POST.get('title')
		print request.POST.get('text')
		print request.POST.get('pub_date')
		data = Story(title = request.POST.get('title'),text = request.POST.get('text'),created_by = request.user)
		data.save()
		print (data.story_id)
		s = Story.objects.get()
	return render(request, 'editor.html',context)
def editor_child(request,s_id):
	context = {}
	context['form'] = MainForm()
	if request.method == 'POST':
		# if request.POST['form-type']=='storyForm':
		data = request.POST
		print request.POST.get('title')
		print request.POST.get('text')
		print request.POST.get('pub_date')
	#	relationship = relations(parent_id=s_id,child_id)		
		data = Story(title = request.POST.get('title'),text = request.POST.get('text'),created_by = request.user)
		data.save()
		print (' parent_id : ',s_id,' child_id : ',data.story_id)
		relationData = relations(parent_id=s_id,child_id=data.story_id)
		relationData.save()
		return HttpResponseRedirect('/myblog/home')
	return render(request, 'editor.html',context)

def StoryPage(request,s_id):
	all_stories = Story.objects.get(story_id=s_id)
	data = {"curr_story": all_stories,
			"s_id" : s_id,
			}

	print s_id
	return render_to_response('StoryPage.html',data)

def some_view(request):
	form = SomeForm()
	if request.method == "POST":
		print 'hereeeee'
		form = SomeForm(request.POST)
		if form.is_valid():
			like = form.cleaned_data['like']
			print like
	return render(request, 'test.html', {'form' :form})