from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.
def index(request):
    Medics=Medic.objects.all()
    Articles=Medic_Article.objects.all()
    Medicines=type_of_medicine.objects.all()
    try:
        Medic.objects.get(user__id=request.user.id)
        is_medic=True
    except:
        is_medic=False
    context={"Medics":Medics,"is_medic":is_medic,"Articles":Articles,"Medicines":Medicines}
    return render(request,"MedicPlace/index.html",context)

def login_view(request):
    if request.method=="POST":
        username=request.POST["Username"]
        password=request.POST["Password"]
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"MedicPlace/login.html",{"message":"Invalid username and/or password"})
    else:
        return render(request,"MedicPlace/login.html")        

def register_view(request):
    if request.method=="POST":
        username=request.POST["Username"]
        email=request.POST["Email"]
        password=request.POST["Password"]
        confirmation=request.POST["Confirmation"]
        First_Name=request.POST["First_name"]
        Last_Name=request.POST["Last_name"]
        age=request.POST["age"]
        is_dr=request.POST["is_dr"]
        if int(age)<18:
            return render(request,"MedicPlace/register.html",{"message":"Age must be 18 or more"}) 
        if  First_Name=="":
             return render(request,"MedicPlace/register.html",{"message":"Please fill all the fields"})
        if  Last_Name=="":
             return render(request,"MedicPlace/register.html",{"message":"Please fill all the fields"})
        if password != confirmation:
            return render(request,"MedicPlace/register.html",{"message":"Passwords must be the same"})

        try:
            NewUser=User.objects.create_user(username,email,password)
            
        except IntegrityError:
            return render(request,"MedicPlace/register.html",{"message":"Username already exist"})
        
        if is_dr=="Yes":
            if  request.POST["Clinic"]=="":
             return render(request,"MedicPlace/register.html",{"message":"Please fill the clinic field"})
            NewDr=Medic()
            NewDr.user=NewUser
            NewDr.First_Name=First_Name
            NewDr.Last_Name=Last_Name
            NewDr.Clinic=request.POST["Clinic"]
            NewDr.age=age
            NewDr.rate=0.0
            NewDr.save()
            NewUser.save()
        elif is_dr=="No":
            NewNormalUser=Normal_User()
            NewNormalUser.user=NewUser
            NewNormalUser.First_Name=First_Name
            NewNormalUser.Last_Name=Last_Name
            NewNormalUser.age=age
            NewNormalUser.save()
            NewUser.save()
        else:
            return render(request,"MedicPlace/register.html",{"message":"You must say if your a Dr or not"})
        
        login(request,NewUser)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request,"MedicPlace/register.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def data_sheet(request,id):
    Medics=Medic.objects.filter(user__id=id)
    Normal_Users=Normal_User.objects.filter(user__id=id)
    try:
        Medic.objects.get(user__id=request.user.id)
        is_medic=True
    except:
        is_medic=False
    if len(Medics)>0:
      data_sheet_user=Medics[0]
      Articles=Medic_Article.objects.filter(medic__id=data_sheet_user.id)
      Page_type="Medic"
      context={"data_sheet_user":data_sheet_user,"Page_type":Page_type,"is_medic":is_medic,"Articles":Articles}
      return render(request,"MedicPlace/data_sheet.html",context)
    elif len(Normal_Users)>0:
        data_sheet_user=Normal_Users[0]
        Page_type="Normal_User"
        context={"data_sheet_user":data_sheet_user,"Page_type":Page_type,"is_medic":is_medic}
        return render(request,"MedicPlace/data_sheet.html",context)

@csrf_exempt
def Rate_Dr(request,id):
    if request.method=="POST":
        DR=Medic.objects.get(id=id)
        New_rate=int(request.POST.get("value"))
        DR.promedio(New_rate)
        rate=DR.rate
        num_of_rates=DR.num_of_rates
        DR.save()
        return JsonResponse({'status':201,"rate":rate,"num_of_rates":num_of_rates})

def New_Article_view(request):
    Medics=Medic.objects.all()
    try:
        Medic.objects.get(user__id=request.user.id)
        is_medic=True
    except:
        is_medic=False
    if request.method=="POST":
        user_id=request.user.id
        medic=Medic.objects.get(user__id=user_id)
        title=request.POST["title"]
        content=request.POST["content"]
        Article=Medic_Article()
        Article.user=request.user
        Article.medic=medic
        Article.title=title
        Article.content=content
        Article.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request,"MedicPlace/New_Medic_article.html",{"is_medic":is_medic})


def Article_view(request,id):
    Get_Article=Medic_Article.objects.get(id=id)
    Medics=Medic.objects.all()
    Comments_article=Article_comment.objects.filter(article__id=id)
    try:
        Medic.objects.get(user__id=request.user.id)
        is_medic=True
    except:
        is_medic=False
    if Get_Article.user==request.user:
        is_owner=True
    else:
        is_owner=False
    if request.method=="POST":
        try:
            is_Delete=request.POST["Delete"]
            Get_Article.delete()
            return HttpResponseRedirect(reverse("index"))
        except:
            comment_content=request.POST["comment"]
            New_comment=Article_comment()
            New_comment.user=request.user
            New_comment.article=Get_Article
            New_comment.comment=comment_content
            New_comment.save()
            return HttpResponseRedirect(reverse("Article",kwargs={"id":id}))
    else:
        title=Get_Article.title
        content=Get_Article.content
        Dr_Article=Get_Article.medic.Last_Name
        Dr_Article_id=Get_Article.medic.user.id
        context={"title":title,"content":content,"Medic":Dr_Article,"Medic_id":Dr_Article_id,"Article_target":Get_Article,"is_medic":is_medic,"is_owner":is_owner,"comments":Comments_article}
        return render(request,"MedicPlace/Medic_article.html",context)

def Edit_Article_view(request,id):
    Get_Article=Medic_Article.objects.get(id=id)
    Medics=Medic.objects.all()
    try:
        Medic.objects.get(user__id=request.user.id)
        is_medic=True
    except:
        is_medic=False
    if Get_Article.user==request.user:
        is_owner=True
    else:
        is_owner=False

    if request.method=="POST":
        title=request.POST["title"]
        content=request.POST["content"]
        Get_Article.title=title
        Get_Article.content=content
        Get_Article.save()
        return HttpResponseRedirect(reverse("Article",kwargs={'id': id}))
    else:
        context={"title":Get_Article.title,"content":Get_Article.content,"id":id,"is_medic":is_medic,"is_owner":is_owner}
        return render(request,"MedicPlace/Edit_Medic_article.html",context)


@csrf_exempt
def Edit_Article_comment_view(request,id):
    if request.method=="POST":
        comment_id=request.POST.get("id")
        comment_content=request.POST.get("content")
        comment_target=Article_comment.objects.get(id=id)
        comment_target.comment=comment_content
        comment_target.save()
        comment_content2=""
        for line in comment_content.splitlines():
            comment_content2=comment_content2 + "\n" + line + "\n"
        return JsonResponse({'status':201,'content':comment_content2})

def Medicine_type_view(request,id):
    Medics=Medic.objects.all()
    try:
        Medic.objects.get(user__id=request.user.id)
        is_medic=True
    except:
        is_medic=False
    Medicine_target=type_of_medicine.objects.get(id=id)
    List_of_Medicine=medicine.objects.filter(type_of_medicine__id=id)
    if len(List_of_Medicine)<1:
        message="There is no medicine for this category yet!"
    else:
        message=""
    context={"Medicine_target":Medicine_target,"List_of_Medicine":List_of_Medicine,"message":message,"is_medic":is_medic}
    return render(request,"MedicPlace/Medicine_type.html",context)

def Medicine_view(request,id):
    Medics=Medic.objects.all()
    try:
        Medic.objects.get(user__id=request.user.id)
        is_medic=True
    except:
        is_medic=False
    Medicines=type_of_medicine.objects.all()
    Medicine_page=medicine.objects.get(id=id)
    Medicine_name=Medicine_page.Name
    Medicine_type=Medicine_page.type_of_medicine.Type
    Medicine_summary=Medicine_page.Summary
    Medicine_Active_ingredient=Medicine_page.Active_ingredient
    Medicine_medic=Medicine_page.medic.Last_Name
    Medicine_id=Medicine_page.id
    Medicine_medic_user=Medicine_page.medic.user
    context={"name":Medicine_name,"type":Medicine_type,"summary":Medicine_summary,
    "Active_ingredient":Medicine_Active_ingredient,"medic":Medicine_medic,
    "Medicine_id":Medicine_id,"Medicines":Medicines,"Medicine_medic_user":Medicine_medic_user,
    "is_medic":is_medic}
    return render(request,"MedicPlace/Medicine.html",context)

def New_Medicine_view(request):
    Medicines=type_of_medicine.objects.all()
    Medics=Medic.objects.all()
    try:
        Medic.objects.get(user__id=request.user.id)
        is_medic=True
    except:
        is_medic=False
    if request.method=="POST":
        Medicine_name=request.POST["name"]
        Medicine_type=type_of_medicine.objects.get(id=request.POST["type"])
        
        Medicine_summary=request.POST["summary"]
        Medicine_Active_ingredient=request.POST["active_ingredient"]
        Medicine_medic=Medic.objects.get(user__id=request.user.id)
        New_Medicine=medicine()
        New_Medicine.Name=Medicine_name
        New_Medicine.type_of_medicine=Medicine_type
        New_Medicine.Summary=Medicine_summary
        New_Medicine.Active_ingredient=Medicine_Active_ingredient
        New_Medicine.medic=Medicine_medic
        New_Medicine.save()
        return HttpResponseRedirect(reverse("Medicine",kwargs={'id':New_Medicine.id}))
    else:
        context={"Medicines":Medicines,"is_medic":is_medic}
        return render(request,"MedicPlace/New_Medicine.html",context)

@csrf_exempt
def Edit_medicine_view(request,id):
    if request.method=="POST":
        Medicine_entry=medicine.objects.get(id=id)
        name=request.POST.get("name")
        type_medicine=type_of_medicine.objects.get(id=request.POST.get("type_medicine"))
        active_ingredient=request.POST.get("active_ingredient")
        summary=request.POST.get("summary")
        Medicine_entry.Name=name
        Medicine_entry.type_of_medicine=type_medicine
        Medicine_entry.Active_ingredient=active_ingredient
        Medicine_entry.Summary=summary
        Medicine_entry.save()
        return JsonResponse({'status':201,'type_of_medicine':type_medicine.Type,
        'active_ingredient':active_ingredient,'summary':summary,"name":name})
