from http import client
from multiprocessing.connection import Client
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
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