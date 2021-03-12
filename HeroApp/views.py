from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.core.files.storage import default_storage

from rest_framework.parsers import JSONParser

from .models import Departments, Heroes
from .serializers import DepartmentSerializer, HeroSerializer

# Create your views here.


@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)

        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)

        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer = DepartmentSerializer(department, data=department_data)
        
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)

        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def heroApi(request, id=0):
    if request.method == 'GET':
        name = request.GET.get('name', '')

        if id == 0 and name == '':
            heroes = Heroes.objects.all()
            heroes_serializer = HeroSerializer(heroes, many=True)
            return JsonResponse(heroes_serializer.data, safe=False)

        elif id > 0:
            hero = Heroes.objects.get(HeroId=id)
            hero_serializer = HeroSerializer(hero)
            return JsonResponse(hero_serializer.data, safe=False)

        elif name != '':
            heroes = Heroes.objects.filter(HeroName__contains=name)
            heroes_serializer = HeroSerializer(heroes, many=True)
            return JsonResponse(heroes_serializer.data, safe=False)

        


    elif request.method == 'POST':
        hero_data = JSONParser().parse(request)
        hero_serializer = HeroSerializer(data=hero_data)

        if hero_serializer.is_valid():
            hero_serializer.save()
            return JsonResponse("API: Added Successfully!!", safe=False)

        return JsonResponse("API: Failed to Add.", safe=False)

    elif request.method == 'PUT':
        hero_data = JSONParser().parse(request)
        hero = Heroes.objects.get(HeroId=hero_data['HeroId'])
        hero_serializer = HeroSerializer(hero, data=hero_data)
        
        if hero_serializer.is_valid():
            hero_serializer.save()
            return JsonResponse("API: Updated Successfully", safe=False)

        return JsonResponse("API: Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        hero = Heroes.objects.get(HeroId=id)
        hero.delete()
        return JsonResponse("API: Deleted Successfully", safe=False)

@csrf_exempt
def saveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)

