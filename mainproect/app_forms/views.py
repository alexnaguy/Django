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
    

    def auto(request):
        return render(request, 'my_form.html')
    

    def get_info(request):

        brand = request.POST.get("brand")
        model = request.POST.get("model")
        price_one = request.POST.get("price_one")
        price_two = request.POST.get("price_two")
        year_one = request.POST.get("year_one")
        year_two = request.POST.get("year_two")

        return render(request,'get.html', {"brand": brand,
                                           "model": model,
                                           "price_one": price_one,
                                           "price_two": price_two,
                                           "year_one": year_one,
                                           "year_two": year_two

                                            })
                       
