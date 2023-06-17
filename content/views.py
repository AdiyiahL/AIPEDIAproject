from django.shortcuts import render
from django.shortcuts import *
from django.views import generic
from content import models

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
        return render(request, "content/add_content.html")
    else:
        title = request.POST.get("title")
        level = request.POST.get("level")
        models.ContentLevel.objects.create(title = title,level = level)
    return redirect("/content/contentlevel/")

def delete_contentlevel(request):
    id = request.GET.get('id')
    models.ContentLevel.objects.filter(id = id).delete()
    return redirect("/content/contentlevel/")

def edit_contentlevel(request):
    if request.method == "GET":
        content_id = request.GET.get("id")
        content_object = models.ContentLevel.objects.filter(id=content_id).first()
        return render(request, 'content/edit_contentlevel.html', {"content_object":content_object})
    content_id = request.GET.get("id")
    title = request.POST.get("title")
    level = request.POST.get("level")
    models.ContentLevel.objects.filter(id = content_id).update(title = title, level = level)
    return redirect("/content/contentlevel/")

def spacy(request):
    return render(request, "content/Spacy.html")