from django.shortcuts import render
from django.shortcuts import *
from django.views import generic
from content import models
from users import models as user_models
from .forms import NewContentForm, NewCoursesForm
# import pwden
from django.http import JsonResponse
from django.core.files.base import ContentFile
import re

# Create your views here.
def  contentlevel(request):
    #add
    # models.ContentLevel.objects.create(title="PyTorch", level=8)
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
        form = NewContentForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            what_area = form.cleaned_data.get('what_area')
            how_area = form.cleaned_data.get('how_area')
            example = form.cleaned_data.get('example')
            source = form.cleaned_data.get('source')
            try_area = form.cleaned_data.get('try_area')
            image_data = request.FILES.get('image1')
            print(image_data)
            image_name = request.FILES.get('image1').name
            print(image_name)
            user_obj_id = request.user_session["id"]
            new = models.NewContent.objects.create(
                title=title,what_area=what_area,how_area=how_area,
                example=example,source=source,try_area=try_area,
                image_data=image_data,image_name=image_name,userId_id=user_obj_id)
            print("save success")
            return redirect("/content/content_list")
        else:
            print(form.errors)
            return render(request, 'content/add_content.html', {'form': form})

def addCourses(request):
    user_obj_id = request.user_session["id"]
    user_obj_name =  request.user_session["name"]
    admin_obj = user_models.AdminUser.objects.filter(id=user_obj_id).first()
    print(admin_obj)
    if admin_obj is None:
        return redirect("/users/choose_login/")
    admin_obj_name = user_models.AdminUser.objects.filter(id=user_obj_id).values('name')
    print(admin_obj_name)
    # print(user_obj_name[0])
    name1 = user_obj_name

    name2 = admin_obj_name[0]['name']
    print(name1)
    print(name2)

    if name1 != name2:
        return redirect("/users/choose_login/")
    #add new content
    if request.method == "GET":
        form = NewCoursesForm()
        level1_list = models.level_lable.objects.all().values("level1").distinct()
        print(level1_list)
        return render(request, "content/add_courses.html", {'form': form, 'level1_list': level1_list})
    else:
        form = NewCoursesForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print(request.POST)
            title = form.cleaned_data.get('title')
            contents = form.cleaned_data.get('contents')
            contents1 = form.cleaned_data.get('contents1')
            source = form.cleaned_data.get('source')
            level1 = request.POST.get('level1_name')
            level2 = request.POST.get('sel_level2')
            print(contents)
            user_obj_id = request.user_session["id"]
            models.NewCourses.objects.create(title=title,level1 = level1, level2=level2,contents=contents,contents1=contents1,source=source)
            print("save success")
            return redirect("/content/courses_list")
        else:
            print(form.errors)
            return render(request, 'content/add_courses.html', {'form': form})

def get_level2(request):
    if request.method =='GET':
        level1_name = request.GET.get('level1_name')
        print(level1_name)
        if level1_name:
            data = list(models.level_lable.objects.filter(level1=level1_name).values("level2"))
            print(data)
            return JsonResponse(data, safe=False)

def get_user_level(request):
    user_obj_id = request.user_session["id"]
    level = user_models.UserInfo.objects.filter(id=user_obj_id).first().level
    return JsonResponse(level,safe=False)

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
        steps = [1,2,3,4,5]
        print(content_object)
        return render(request, "content/all_content.html", {"content_object": content_object,"steps":steps})

def all_courses(request):
    content_id = request.GET.get("id")
    content_object = models.NewCourses.objects.filter(id=content_id).first()
    steps = [1, 2, 3, 4, 5]
    print(content_object)
    title = content_object.title
    print(title)
    questions = models.Questions.objects.filter(title=title).first()
    if request.method=="GET":
        return render(request, "content/all_courses.html", {"content_object": content_object,"questions":questions})
    else:
        op1 = request.POST.get('option1')
        op2 = request.POST.get('option2')
        op3 = request.POST.get('option3')
        count = 0
        if op1 == questions.answer1:
            count+=1
        if op2 == questions.answer2:
            count+=1
        if op3 == questions.answer3:
            count+=1
        user_obj_id = request.user_session["id"]
        user_obj = user_models.UserInfo.objects.filter(id = user_obj_id).first()
        user_level = user_obj.level
        new_user_level = user_level + 1
        user_models.UserInfo.objects.filter(id = user_obj_id).update(level=new_user_level)
        as1 = questions.answer1
        as2 = questions.answer2
        as3 = questions.answer3
        answers = {"as1":as1,"as2":as2,"as3":as3}
        return render(request, "content/all_courses.html", {"content_object": content_object, "questions": questions,"count":count,"answers":answers})


def content_list(request):
    # query
    queryset = models.NewContent.objects.all().order_by("id")
    return render(request, 'content/content_list.html', {"queryset": queryset})
    # return render(request,"content/all_content.html",)

def courses_list(request):
    # query
    queryset = models.NewCourses.objects.all().order_by("id")[0:10:3]
    return render(request, 'content/courses_list.html', {"queryset": queryset})

def all_read_list(request):
    queryset = models.NewContent.objects.all().order_by("id")
    return render(request, 'content/all_read_list.html', {"queryset": queryset})

def all_courses_list(request):
    queryset = models.NewCourses.objects.all().order_by("id")
    return render(request, 'content/all_courses_list.html', {"queryset": queryset})


def showcourses_labale1(request):
    if request.method == "GET":
        courses_lable = request.GET.get("lable")
        print(courses_lable)
        queryset = models.NewCourses.objects.all().filter(level1=courses_lable)
        print(queryset)
        return render(request, "content/showcourses_labale1.html", {"queryset":queryset})


    queryset = models.NewContent.objects.all().order_by("id")
    return render(request, 'content/all_read_list.html', {"queryset": queryset})

def ShowCourses(request):
    if request.method == "GET":
        courses_lable = request.GET.get("lable")
        print(courses_lable)
        queryset = models.NewCourses.objects.all().filter(level2=courses_lable)
        print(queryset)
        return render(request, "content/ShowCourses.html", {"queryset":queryset})


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

