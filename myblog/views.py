from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import MainForm, ItemForm, EpisodeForm
from .models import Story, relations, Genres, Item, Episode, Representation_Type, Content_Type
from django.shortcuts import render_to_response
import uuid, json


# Create your views here.
def index(request):
    return HttpResponse("Hello, Welcome to the UNIVERSE.")


def home(request):
    # return HttpResponse("Logged in successfully")

    all_stories = Story.objects.all()
    data = {"stories": all_stories}
    # request.session['data'] = data
    return render_to_response('home.html', data)


def registered():
    return HttpResponse("Registered in successfully")

@login_required
def item(request):
    context = {}
    context['form'] = ItemForm()
    if request.method == 'POST':
        item_typ = Representation_Type.objects.get(representation_id=request.POST.get('item_type'))
        data = Item(item_title=request.POST.get('item_title'),
                    item_type=item_typ,
                    item_description=request.POST.get('item_description'),
                    created_by=request.user)
        data.save()
        context = {}
        context['form'] = EpisodeForm()
        context['item_id'] = data.item_id
        request.session['parent_id'] = str(data.item_id)
        return HttpResponseRedirect('/myblog/episode')
        #return render(request, 'episode.html', context)#HttpResponseRedirect('/myblog/home')
    return render(request, 'item.html', context)


def item_details(request, item_id):
    item_Object = Item.objects.get(item_id=item_id)
    data = {"item": item_Object}
    return render_to_response('item_details.html', data)


@login_required
def episode(request):
    context = {}
    context['form'] = EpisodeForm()
    if request.method == 'POST':
        parent_id = request.session['parent_id']
        item_Object = Item.objects.get(item_id=parent_id)
        episode_typ = Representation_Type.objects.get(representation_id=request.POST.get('episode_type'))
        episode_content_typ = Content_Type.objects.get(content_id=request.POST.get('episode_content_type'))
        data = Episode(episode_description=request.POST.get('episode_description'),
                       parent_id = item_Object,
                       episode_type=episode_typ,
                       episode_content=request.POST.get('episode_content'),
                       episode_content_type=episode_content_typ,
                       episode_content_relative_url=request.POST.get('episode_content_relative_url'),
                       categories=request.POST.get('categories'),
                       created_by=request.user)
        data.save()
        del request.session['parent_id']
        print "testing:::::::::"
        #print request.session['parent_id']
        return HttpResponseRedirect('/myblog/items')
    return render(request, 'episode.html', context)


@login_required
def editor(request):
    context = {}
    context['form'] = MainForm()
    if request.method == 'POST':
        # if request.POST['form-type']=='storyForm':
        data = request.POST
        print request.POST.get('title')
        print request.POST.get('text')
        print request.POST.get('pub_date')
        data = Story(title=request.POST.get('title'),
                     text=request.POST.get('text'),
                     created_by=request.user)
        data.save()
    return render(request, 'editor.html', context)


@login_required
def editor_child(request, s_id):
    context = {}
    context['form'] = MainForm()
    if request.method == 'POST':
        # if request.POST['form-type']=='storyForm':
        data = request.POST
        print request.POST.get('title')
        print request.POST.get('text')
        print request.POST.get('pub_date')
        #	relationship = relations(parent_id=s_id,child_id)
        data = Story(title=request.POST.get('title'),
                     text=request.POST.get('text'),
                     created_by=request.user)
        data.save()
        print (' parent_id : ', s_id, ' child_id : ', data.story_id)
        relationData = relations(parent_id=s_id, child_id=data.story_id)
        relationData.save()
        return HttpResponseRedirect('/myblog/home')
    return render(request, 'editor.html', context)


def StoryPage(request, s_id):
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
    # print 'idlen',len(id_list)
    data = {"curr_story": all_stories,
            "s_id": s_id,
            "relations_data": id_list,
            "parent_relation": parent_relation
            }

    print s_id
    return render_to_response('StoryPage.html', data)


def items_list(request):
    list_items = Item.objects.all()
    data = {"items": list_items}
    # request.session['data'] = data
    return render_to_response('items_list.html', data)


def get_jsonData(parent_id):
    all_relations = relations.objects.all()
    curr_story = Story.objects.get(story_id=parent_id)
    main_parent = "null"
    for relation in all_relations:
        if str(parent_id) == str(relation.child_id):
            main_parent = relation.parent_id
    data = {
        # "name": str(parent_id),
        "name": str(curr_story.title),
        "parent": str(main_parent),
        "children": [get_jsonData(relation.child_id) for relation in all_relations if
                     str(parent_id) == str(relation.parent_id)]
    }
    return data


def visualize(request, s_id):
    parent_id = s_id
    jsonData = get_jsonData(parent_id)
    # jsonData = {}
    treeData = {
        "name": "Top Level",
        "parent": "null",
        "children": [
            {
                "name": "Level 2: A",
                "parent": "Top Level",
                "children": [
                    {
                        "name": "Level 3: Son of A",
                        "parent": "Level 2: A",
                        "children": [
                            {
                                "name": "Level 4: Child",
                                "parent": "Level 3: Son of A",
                                "children": []
                            }
                        ]
                    },
                    {
                        "name": "Level 3: Daughter of A",
                        "parent": "Level 2: A",
                        "children": []
                    }
                ]
            },
            {
                "name": "Level 2: B",
                "parent": "Top Level",
                "children": []
            }
        ]
    }
    context = {'data': treeData,
               'jsonData': json.dumps(jsonData)
               }

    return render(request, 'index1.html', context)


def get_data(request):
    treeData = {
        "name": "Top Level",
        "parent": "null",
        "children": [
            {
                "name": "Level 2: A",
                "parent": "Top Level",
                "children": [
                    {
                        "name": "Level 3: Son of A",
                        "parent": "Level 2: A",
                        "children": [
                            {
                                "name": "Level 4: Child",
                                "parent": "Level 3: Son of A",
                                "children": []
                            }
                        ]
                    },
                    {
                        "name": "Level 3: Daughter of A",
                        "parent": "Level 2: A"
                    }
                ]
            },
            {
                "name": "Level 2: B",
                "parent": "Top Level"
            }
        ]
    }

    return render(request, 'index1.html', {'data': treeData})


def genreList(request):
    all_stories = Story.objects.all()
    all_genres = Genres.objects.all()
    genre_dict = {}
    # import pdb;pdb.set_trace()
    for story in all_stories:
        gnr_id = str(story.genre_id.genre_id)
        temp = Genres.objects.get(genre_id=gnr_id)
        if (genre_dict.has_key(temp.genre_name)):
            genre_dict[temp.genre_name] = genre_dict[temp.genre_name] + 1
        else:
            genre_dict[temp.genre_name] = 1
    print genre_dict
    return render(request, 'GenreList.html')

    # ------------------------------------------------------------------------------------------
