from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from abc import ABC, abstractmethod
import time



class FormManage:

    def authorization(request):
        
        return render(request, 'autorization.html')
        

    def show_data(request):

        name = request.POST.get("name")
        lastname = request.POST.get("lastname")
        age = request.POST.get("age")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        adress = request.POST.get("adress")

        return render(request,'end.html', {"name": name,
                                           "lastname": lastname,
                                           "age": age,
                                           "email": email,
                                           "gender": gender,
                                           "adress": adress

                                            })
                       
