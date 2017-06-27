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
	all_relations = relations.objects.all()
	id_list = []
	parent_relation = []
	for relation in all_relations:
		if str(relation.parent_id) == str(all_stories.story_id):
			print 'As Parent:'
			print relation.parent_id, all_stories.story_id
			id_list.append(relation)
		elif str(relation.child_id) == str(all_stories.story_id):
			print 'As Child:'
			parent_relation = relation
	#print 'idlen',len(id_list)
	data = {"curr_story" : all_stories,
			"s_id" : s_id,
			"relations_data" : id_list,
			"parent_relation" : parent_relation
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

def get_data(request):
	treeData = [
		{
			"name": "Top Level",
			"parent": "null",
			"children": [
				{
					"name": "Level 2: A",
					"parent": "Top Level",
					"children": [
						{
							"name": "Son of A",
							"parent": "Level 2: A"
						},
						{
							"name": "Daughter of A",
							"parent": "Level 2: A"
						}
					]
				},
				{
					"name": "Level 2: B",
					"parent": "Top Level"
				}
			]
		},
		{
			"name": "Top Level1",
			"parent": "null",
			"children": [
				{
					"name": "Level 2: A",
					"parent": "Top Level1",
					"children": [
						{
							"name": "Son of A",
							"parent": "Level 2: A"
						},
						{
							"name": "Daughter of A",
							"parent": "Level 2: A"
						}
					]
				},
				{
					"name": "Level 2: B",
					"parent": "Top Level1"
				}
			]
		}
	]
	return render(request, 'index1.html', {'data' :treeData})