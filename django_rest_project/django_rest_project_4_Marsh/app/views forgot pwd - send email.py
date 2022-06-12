from http import client
from multiprocessing.connection import Client
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.db.models import Q
import win32com.client as win32
from .outlook import *
import json
# @api_view(['GET', 'POST'])
def hello(request):    
   return Response({"message" : "Hello world!"})

@csrf_exempt
def search_client_url(request):
    params = request.GET 
    password = params.get('password')
    clienturl = ClientUrl.objects.filter(
        clientpass=password
    )
    print("hello")
    result = []
    for u in clienturl:
        result.append({
            'client_name':u.clientname,
            'description':u.description,
            'client_url':u.clienturl,
        })
    return HttpResponse(json.dumps(result)) 
def search_staff_url(request):
    params = request.GET 
    password = params.get('password')
    clientname = params.get('clientname')
    year = params.get('year')
    clienturl = StaffUrl.objects.filter(
        staffpass=password,
    )
    if clientname:
        clienturl = clienturl.filter(
            clientname = clientname
        )
    if year:
        clienturl = clienturl.filter(
            year = year
        )
    print("hello")
    result = []
    for u in clienturl:
        result.append({
            'staff_name':u.staffname,
            'client_name':u.clientname,
            'description':u.description,
            'year':u.year,
            'client_url':u.staffurl
        })
    return HttpResponse(json.dumps(result))     
@csrf_exempt
def get_client_url(request):
    return render(request,'getclienturl.html')
# @api_view(['POST'])
@csrf_exempt
def reg(request):
    if request.method == 'POST':
        pwd = request.POST.get('password') 
        # pwds = ClientUrl.objects.filter(clientname = pwd)
        pwds = ClientUrl.objects.filter(clientpass = pwd)
        clientname = pwds.first()
        print(pwds)
        print(f'ket qua dau tien {clientname}')
        if not pwds:
            return HttpResponse({'password error': 'Thiếu sản phẩm trong danh mục hàng'}, status=500)
            # print(pwds)
        # if pwd == pwds.clientname:
        #     print(pwd)
        #     print("YES")
        # if pwd in pwds:
        #     print(request.POST.get('password'))
        #     # messages.add_message(request, messages.INFO, 'success')
        #     messages.info(request, 'success')
        else:
            if request.POST.get('phone') and request.POST.get('name') and request.POST.get('email'):
                post=Register1()
                post.phone= request.POST.get('phone')
                post.name= request.POST.get('name')
                post.email= request.POST.get('email')
                post.save()             
                # return render(request,'posts/reg.html')
                # return HttpResponse(request)   
                # return render(request, 'getclienturl.html', ) 
                # template =loader.get_template('getclienturl.html')
                context = {
                    'password':pwd,
                    'clientname':clientname
                }
                return render(request, 'getclienturl.html',context)
            else:
                print(request.POST.get('password'))
            # messages.add_message(request, messages.INFO, 'Wrong Password')
                messages.info(request, 'Wrong Password')
                return render(request,'posts/reg.html')
    else:
            return render(request,'posts/reg.html')
# @csrf_exempt
# def search_client_url(request):
#     params = request.GET 
#     password = params.get('password')
#     clienturl = ClientUrl.objects.filter(
#         clientpass=password
#     )
#     print("hello")
#     result = []
#     for u in clienturl:
#         result.append({
#             'client_name':u.clientname,
#             'description':u.description,
#             'client_url':u.clienturl,
#         })
#     return HttpResponse(json.dumps(result)) 
# @csrf_exempt
# def get_client_url(request):
#     return render(request,'getclienturl.html')
@csrf_exempt
def doc2html(request):
    return render(request, 'redirect.html')
@csrf_exempt
def search_user(request):
    params = request.GET 
    keyword = params.get('keyword')
    users = Register1.objects.all()
    print("hello")
    result = []
    for u in users:
        result.append({
            'phone':u.phone,
            'name':u.name,
            'email':u.email
        })
    return HttpResponse(json.dumps(result)) 
@csrf_exempt
def get_list_user(request):
    return render(request,'getlistuser.html')

@csrf_exempt
def checkins(request):
    body = request.POST 
    pwd = body.get('password')
    pwdlist = ['Baoviet','PTI','Generally']

    # TODO chế biến thêm khúc này 
    # NOTE bo het template ins vao folder posts\ins\ins html ... 
    
    #~~~~~~~~~~~~~~~

    if pwd in pwdlist:
        print("TRUE")
      #   messages.add_message(request, messages.INFO, 'success')        
        messages.info(request, 'success')        
        return render(request, 'posts/'+ pwd.lower() +'.html') 
    else:
        print(request.POST.get('password'))
      #   messages.add_message(request, messages.INFO, 'Wrong Password')
        messages.info(request, 'password is incorrect')
        return render(request,'posts/check.html')

@csrf_exempt
def datatable(request):
    return render(request,'tabledata.html')

@csrf_exempt
def checkstaff(request):
    if request.method == 'POST':
        pwd = request.POST.get('password') 
        # pwds = ClientUrl.objects.filter(clientname = pwd)
        username = request.POST.get('name')
        client_name = request.POST.get('clientname')
        year = request.POST.get('year')
        pwds = StaffUrl.objects.filter(staffpass = pwd)
        clientname = pwds.first()
        print(pwds)
        print(f'ket qua dau tien {clientname}')
        if not pwds:
            return HttpResponse({'password error': 'password error'}, status=500)
        else:           
            context = {
                    'password':pwd,
                    'name':clientname,
                    'year':year,
                    'clientname':client_name
            }
            return render(request, 'getstaff.html',context)
    else:
            return render(request,'posts/staff.html')
        
#~~~~~~~~~~~~~BAT
@csrf_exempt
def bat(request):
    if request.method == 'POST':
        pwd = request.POST.get('password') 
        # pwds = ClientUrl.objects.filter(clientname = pwd)
        email = request.POST.get('email')
        pwds = Bat.objects.filter(batpassword = pwd, batemail = email)
        clientname = pwds.first()
        print(pwds)
        print(f'ket qua dau tien {clientname}')
        if not pwds:
            return HttpResponse({'error': 'missing info'}, status=500)
            # print(pwds)
        # if pwd == pwds.clientname:
        #     print(pwd)
        #     print("YES")
        # if pwd in pwds:
        #     print(request.POST.get('password'))
        #     # messages.add_message(request, messages.INFO, 'success')
        #     messages.info(request, 'success')
        else:           
            context = {
                    'password':pwd,
                    'email':email
                }
            return render(request, 'getbat.html',context)
    else:
            return render(request,'posts/bat.html')
        
#~~~~~~~~~~~SEARCH BAT~~~~~~~~~~~~~~

def search_bat(request):
    params = request.GET 
    password = params.get('password')
    email = params.get('email')
    #year = params.get('year')
    clienturl = Bat.objects.filter(
        batpassword=password,
        batemail = email,
    )
    print("hello")
    result = []
    for u in clienturl:
        result.append({
            'batuser':u.batuser,
            'batemail':u.batemail,
            'batrelationship':u.batrelationship,
            'batdob':u.batdob,
            'batgender':u.batgender,
            'batid':u.batid
        })
    return HttpResponse(json.dumps(result))   

#DEFINE email password to user 
import pythoncom
import win32com.client as win32
def sendemail(email, password):
    template = '''
        <p>Hi <strong>Useremail</strong>,</p>
        <p><strong>You password is <span style="color: rgb(224, 62, 45);">password1</span></strong></p>
        <p>&nbsp;</p>
        <p><strong><span style="color: rgb(224, 62, 45);">Thank you for using our services</span></strong></p>
    '''
    template = template.replace('Useremail',email)
    template = template.replace('password1', password)
    outlook = win32.Dispatch('outlook.application' ,pythoncom.CoInitialize())
    mail = outlook.CreateItem(0)
    mail.To = email
    mail.Subject = 'Im your password assistant'
    # mail.Body = 'Message body'
    mail.HTMLBody = template #this field is optional
    mail.Send() 
#DEFINE forgot password function
@csrf_exempt
def forgot(request):
    if request.method == 'POST':
        # pwds = ClientUrl.objects.filter(clientname = pwd)
        email = request.POST.get('email')    
        pwds = Bat.objects.filter(batemail = email).first()
        print(pwds)    
        if not pwds:
            return HttpResponse({'error': 'email is incorrect'}, status=500)        
        else:
            # return HttpResponse({f'{pwds.batpassword}': f'{pwds.batpassword}'}, status=500) 
            sendemail(email,pwds.batpassword)
            return render(request,'posts/bat.html' )       
    else:       
        return render(request,'posts/forgot.html')


