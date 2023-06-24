from django.shortcuts import render
from django.shortcuts import *
from django.views import generic
from content import models
from .forms import NewContentForm
import re

# Create your views here.
def  contentlevel(request):
    #add
    # models.ContentLevel.objects.create(title="PyTorch", level=8)
    # models.ContentLevel.objects.create(title="Python", level=2)
    # models.ContentLevel.objects.create(title="Math", level=3)
    # models.ContentLevel.objects.create(title="Spacy", level=5)

    #query
    queryset = models.ContentLevel.objects.all().order_by("id")
    # for obj in queryset:
    #     print(obj.title,obj.level)
    # queryset = models.ContentLevel.objects.filter()

    #delete
    # models.ContentLevel.objects.filter(title="Python").delete()

    #update
    # models.ContentLevel.objects.filter(title="Python").update(level=10)
    return render(request, 'content/contentlevel.html', {"queryset":queryset})


def addContent(request):
    #add new content
    if request.method == "GET":
        form = NewContentForm()
        return render(request, "content/add_content.html", {'form': form})
    else:
        form = NewContentForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            what_area = form.cleaned_data.get('what_area')
            how_area = form.cleaned_data.get('how_area')
            example = form.cleaned_data.get('example')
            source = form.cleaned_data.get('source')
            try_area = form.cleaned_data.get('try_area')
            print("11111111")
            user_obj_id = request.user_session["id"]
            models.NewContent.objects.create(title=title,what_area=what_area,how_area=how_area,example=example,source=source,try_area=try_area,userId_id=user_obj_id)
            print("save success")
            return redirect("/content/content_list")
        else:
            print(form.errors)
            return render(request, 'content/add_content.html', {'form': form})

def delete_contentlevel(request):
    id = request.GET.get('id')
    models.ContentLevel.objects.filter(id = id).delete()
    return redirect("/content/contentlevel/")

def edit_contentlevel(request):
    if request.method == "GET":
        content_id = request.GET.get("id")
        content_object = models.ContentLevel.objects.filter(id=content_id).first()
        return render(request, "content/edit_contentlevel.html", {"content_object":content_object})
    content_id = request.GET.get("id")
    title = request.POST.get("title")
    level = request.POST.get("level")
    models.ContentLevel.objects.filter(id = content_id).update(title = title, level = level)
    return redirect("/content/contentlevel/")


def all_content(request):
    if request.method=="GET":
        content_id = request.GET.get("id")
        content_object = models.NewContent.objects.filter(id=content_id).first()
        # print(content_object)
        # ls=[]
        # path_type = content_object.path_type.replace("'", "").strip("[]").strip().split(',')
        # path = content_object.path.replace("'", "").strip("[]").strip().split(',')
        # do_type = content_object.do_type.replace("'", "").strip("[]").strip().split(',')
        # do = content_object.do.replace("'", "").strip("[]").strip().split(',')
        # for i in range(len(path_type)):
        #     my_data = {path_type[i]: path[i], do_type[i]: do[i]}
        #     ls.append(my_data)
        # print(ls)
        # how_area = content_object["how_area"]
        # steps = how_area.rsplit(";",3) #steps is a list
        steps = [1,2,3,4,5]
        print(content_object)
        return render(request, "content/all_content.html", {"content_object": content_object,"steps":steps})

def content_list(request):
    # query
    queryset = models.NewContent.objects.all().order_by("id")[:4]
    return render(request, 'content/content_list.html', {"queryset": queryset})

    return render(request,"content/all_content.html",)

def all_read_list(request):
    queryset = models.NewContent.objects.all().order_by("id")
    return render(request, 'content/all_read_list.html', {"queryset": queryset})

def play_list(request):
    return render(request,"content/play_list.html")
def spacy(request):
    return render(request, "content/Spacy.html")

def homePage(request):
    return render(request,"content/homePage.html")

def vuetest(request):
    return render(request,"content/vueTest.html")

